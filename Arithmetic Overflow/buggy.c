#include <assert.h>
#include <stdint.h>

int main() {
    int8_t a = 120;
    int8_t b = 10;
    int16_t tmp0 = (int16_t)a + (int16_t)b;
    __ESBMC_assert(tmp0 >= -128 && tmp0 <= 127, "Signed overflow detected");
    int8_t c = tmp0;
    return 0;
}