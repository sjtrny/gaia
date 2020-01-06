# Update apt
apt-get -y update

apt-get -y install -y i2c-tools

# Create virtual env and install requirements
apt-get -y install python3-venv
python3 -m venv venv
source venv/bin/activate
venv/bin/python3 -m pip install -r requirements.txt

# Enable and run gaia service
cp gaia.service /etc/systemd/system
systemctl enable gaia
systemctl start gaia
