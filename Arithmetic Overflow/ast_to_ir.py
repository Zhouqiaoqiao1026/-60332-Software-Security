# ast_to_ir.py

import json

# Load the saved AST
with open("buggy_ast.json") as f:
    ast_data = json.load(f)

# Simple symbol table for variable types (you would expand this later)
symbol_table = {}

def process_node(node):
    """Recursively process AST nodes into a simple IR."""
    if node["_type"] == "Module":
        return [process_node(stmt) for stmt in node["body"]]

    elif node["_type"] == "Assign":
        # Simple assignment (assume one target for now)
        target = node["targets"][0]["id"]
        value = process_node(node["value"])
        symbol_table[target] = "uint8"  # Assume uint8 for simplicity
        return {
            "op": "assign",
            "target": target,
            "value": value
        }
    elif node["_type"] == "FunctionDef":
        body_ir = [process_node(stmt) for stmt in node["body"]]
        return {
            "op": "function",
            "name": node["name"],
            "args": [arg["arg"] for arg in node["args"]["args"]],
            "body": body_ir
        }

    elif node["_type"] == "Expr":
        # Typically an expression like a function call
        return process_node(node["value"])


    elif node["_type"] == "BinOp":
        left = process_node(node["left"])
        right = process_node(node["right"])
        op = node["op"]["_type"]
        ir_op = {
            "Add": "+",
            "Sub": "-",
            "Mult": "*",
            "Div": "/"
        }.get(op, op)  # Map Python ops to IR ops

        # Insert an overflow check if both sides are uint8
        if symbol_table.get(left, "") == "uint8" and symbol_table.get(right, "") == "uint8":
            return {
                "op": "binop_with_overflow_check",
                "left": left,
                "right": right,
                "operator": ir_op
            }
        else:
            return {
                "op": "binop",
                "left": left,
                "right": right,
                "operator": ir_op
            }

    elif node["_type"] == "Name":
        return node["id"]

    elif node["_type"] == "Constant":
        return node["value"]

    else:
        return {"unknown_node": node["_type"]}

# Process the root
ir = process_node(ast_data)

# Save the IR to a file
with open("output_ir.json", "w") as f:
    json.dump(ir, f, indent=2)

print("IR saved to output_ir.json")

