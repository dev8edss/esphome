#include "max9744.h"
#include "esphome/core/helpers.h"
#include "esphome/core/log.h"

namespace esphome {
namespace max9744 {

static const char *const TAG = "max9744";

void MAX9744::dump_config() {
  ESP_LOGCONFIG(TAG, "MAX9744 Output:");
  LOG_I2C_DEVICE(this);
}

void MAX9744::write_state(float state) {
  const uint8_t value = remap(state, 0.0f, 1.0f, 0, 63);
  this->write_byte(0, value);
  ESP_LOGCONFIG(TAG, "MAX9744 Output:");
  LOG_I2C_DEVICE(this);
}

}  // namespace max9744
}  // namespace esphome
