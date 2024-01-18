#pragma once

#include "esphome/components/i2c/i2c.h"
#include "esphome/components/output/float_output.h"
#include "esphome/core/component.h"

namespace esphome {
namespace max9744 {

class MAX9744 : public Component, public output::FloatOutput, public i2c::I2CDevice {
 public:
  void dump_config() override;
  void write_state(float state) override;
};

}  // namespace max9744
}  // namespace esphome
