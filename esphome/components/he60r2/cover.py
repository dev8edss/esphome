import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import cover, uart
from esphome.const import (
    CONF_CLOSE_DURATION,
    CONF_ID,
    CONF_OPEN_DURATION,
)

he60r2_ns = cg.esphome_ns.namespace("he60r2")
HE60r2Cover = he60r2_ns.class_("HE60r2Cover", cover.Cover, cg.Component)

CONFIG_SCHEMA = (
    cover.COVER_SCHEMA.extend(uart.UART_DEVICE_SCHEMA)
    .extend(cv.COMPONENT_SCHEMA)
    .extend(
        {
            cv.GenerateID(): cv.declare_id(HE60r2Cover),
            cv.Optional(
                CONF_OPEN_DURATION, default="15s"
            ): cv.positive_time_period_milliseconds,
            cv.Optional(
                CONF_CLOSE_DURATION, default="15s"
            ): cv.positive_time_period_milliseconds,
        }
    )
)

FINAL_VALIDATE_SCHEMA = uart.final_validate_device_schema(
    "he60r2",
    baud_rate=1200,
    require_tx=True,
    require_rx=True,
    data_bits=8,
    stop_bits=1,
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await cover.register_cover(var, config)
    await uart.register_uart_device(var, config)

    cg.add(var.set_close_duration(config[CONF_CLOSE_DURATION]))
    cg.add(var.set_open_duration(config[CONF_OPEN_DURATION]))
