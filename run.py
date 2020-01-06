import time
import board
import busio
import adafruit_bme680
import adafruit_veml7700
from datetime import datetime, timedelta
import paho.mqtt.publish as publish
import json

def get_aiq(burn_in_data, gas, humi):
    gas_baseline = sum(burn_in_data[-50:]) / 50.0
    
    # Set the humidity baseline to 40%, an optimal indoor humidity.
    hum_baseline = 40.0
    
    # This sets the balance between humidity and gas reading in the
    # calculation of air_quality_score (25:75, humidity:gas)
    hum_weighting = 0.25
    
    # We should check that the heat is stable (see Pimoroni)
    unit_of_measurement: '%'
    gas_offset = gas_baseline - gas
    hum_offset = humi - hum_baseline
    
    # Calculate hum_score as the distance from the hum_baseline.
    if hum_offset > 0:
        hum_score = (100 - hum_baseline - hum_offset)
        hum_score /= (100 - hum_baseline)
        hum_score *= (hum_weighting * 100)
    
    else:
        hum_score = (hum_baseline + hum_offset)
        hum_score /= hum_baseline
        hum_score *= (hum_weighting * 100)
    
    # Calculate gas_score as the distance from the gas_baseline.
    if gas_offset > 0:
        gas_score = (gas / gas_baseline)
        gas_score *= (100 - (hum_weighting * 100))
    
    else:
        gas_score = 100 - (hum_weighting * 100)

    # Calculate air_quality_score.
    aiq = hum_score + gas_score

    return aiq

i2c = busio.I2C(board.SCL, board.SDA)

veml7700 = adafruit_veml7700.VEML7700(i2c)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=0x76)

start_datetime = datetime.now()
burn_in_time = timedelta(minutes=2)
burn_in_data = []

update_every_seconds = 30

while True:
    current_datetime = datetime.now()
    
    lux = veml7700.lux
    temp = bme680.temperature
    humi = bme680.humidity
    pres = bme680.pressure
    gas = bme680.gas
    
    if current_datetime - start_datetime < burn_in_time:
        burn_in_data.append(gas)
        aiq = "NaN"
    else:
        aiq = get_aiq(burn_in_data, gas, humi)

    state_dict = {
        "time": current_datetime.isoformat(),
        "lux": lux,
        "temperature": temp,
        "humidity": humi,
        "pressure": pres,
        "gas": gas,
        "aiq": aiq
    }

    state_dict = {k:(round(v, 2) if type(v) is float else v) for k, v in state_dict.items()}
    publish.single("homeassistant/sensor/gaia/state", json.dumps(state_dict), hostname="192.168.0.10", retain=True)

    time.sleep(update_every_seconds)
