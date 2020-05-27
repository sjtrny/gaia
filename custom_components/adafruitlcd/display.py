import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import display
from esphome.const import CONF_ID, CONF_LAMBDA

adafruitlcd_ns = cg.esphome_ns.namespace('adafruitlcd')
AdafruitLCDComponent = adafruitlcd_ns.class_('AdafruitLCDComponent', cg.PollingComponent)
                                          
CONFIG_SCHEMA = display.BASIC_DISPLAY_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(AdafruitLCDComponent),
}).extend(cv.polling_component_schema('1s'))

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)

    if CONF_LAMBDA in config:
        lambda_ = yield cg.process_lambda(config[CONF_LAMBDA],
                                          [(AdafruitLCDComponent.operator('ref'), 'it')],
                                          return_type=cg.void)
        cg.add(var.set_writer(lambda_))

