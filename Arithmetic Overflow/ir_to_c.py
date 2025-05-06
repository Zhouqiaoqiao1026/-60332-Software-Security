# ir_to_c.py

import json

with open("output_ir.json") as f:
    ir = json.load(f)

lines = []
lines.append('#include <assert.h>')
lines.append('#include <stdint.h>')
lines.append('')
lines.append('int main() {')

tmp_count = 0  # Unique temp var names

for stmt in ir:
    if stmt["op"] == "assign":
        target = stmt["target"]
        value = stmt["value"]

        # Simple integer assignment
        if isinstance(value, int):
            lines.append(f'    int8_t {target} = {value};')  # Use int8_t for signed test

        # Unsigned overflow check
        elif isinstance(value, dict) and value["op"] == "binop_with_overflow_check":
            left = value["left"]
            right = value["right"]
            operator = value["operator"]
            tmp_var = f"tmp{tmp_count}"
            tmp_count += 1

            lines.append(f'    uint16_t {tmp_var} = {left} {operator} {right};')
            lines.append(f'    __ESBMC_assert({tmp_var} <= 255, "Unsigned overflow detected");')
            lines.append(f'    uint8_t {target} = {tmp_var};')

        # Signed overflow check
        elif isinstance(value, dict) and value["op"] == "binop_with_signed_overflow_check":
            left = value["left"]
            right = value["right"]
            operator = value["operator"]
            tmp_var = f"tmp{tmp_count}"
            tmp_count += 1

            lines.append(f'    int16_t {tmp_var} = (int16_t){left} {operator} (int16_t){right};')
            lines.append(f'    __ESBMC_assert({tmp_var} >= -128 && {tmp_var} <= 127, "Signed overflow detected");')
            lines.append(f'    int8_t {target} = {tmp_var};')

        # Regular binop
        elif isinstance(value, dict) and value["op"] == "binop":
            left = value["left"]
            right = value["right"]
            operator = value["operator"]
            lines.append(f'    int8_t {target} = {left} {operator} {right};')

    elif stmt["op"] == "function":
        lines.append(f'    // Function {stmt["name"]} not implemented')

lines.append('    return 0;')
lines.append('}')

with open("buggy.c", "w") as f:
    f.write('\n'.join(lines))

print("✅ C code generated in buggy.c with signed/unsigned overflow detection.")
