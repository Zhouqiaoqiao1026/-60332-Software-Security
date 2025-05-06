import json

# ---------- CFG Node ----------
class CFGNode:
    def __init__(self, id, statements=None):
        self.id = id
        self.statements = statements or []
        self.successors = []

    def add_successor(self, node):
        self.successors.append(node)

# ---------- Global Helpers ----------
node_counter = 0

def new_node(statements=None):
    global node_counter
    node = CFGNode(f"n{node_counter}", statements or [])
    node_counter += 1
    return node

# ---------- CFG Builder ----------
def build_cfg_from_ir(ir_list):
    global node_counter
    node_counter = 0

    entry_node = new_node()
    current_node = entry_node
    nodes = [entry_node]

    for stmt in ir_list:
        if stmt["op"] == "if":
            cond_node = new_node([{"op": "if_condition", "condition": stmt["condition"]}])
            current_node.add_successor(cond_node)
            nodes.append(cond_node)

            then_nodes = build_cfg_from_ir(stmt["then"])
            else_nodes = build_cfg_from_ir(stmt.get("else", []))
            cond_node.add_successor(then_nodes[0])
            cond_node.add_successor(else_nodes[0])

            merge_node = new_node()
            then_nodes[-1].add_successor(merge_node)
            else_nodes[-1].add_successor(merge_node)
            nodes.extend(then_nodes + else_nodes + [merge_node])
            current_node = merge_node
        else:
            current_node.statements.append(stmt)

    return nodes

# ---------- Export to .dot ----------
def export_cfg_to_dot(nodes, filename="cfg.dot"):
    with open(filename, "w") as f:
        f.write("digraph CFG {\n")
        f.write("  node [shape=box];\n")

        for node in nodes:
            label = "\\n".join([str(stmt) for stmt in node.statements]) or "empty"
            f.write(f'  {node.id} [label="{node.id}\\n{label}"];\n')
            for succ in node.successors:
                f.write(f"  {node.id} -> {succ.id};\n")

        f.write("}\n")

    print(f"✅ CFG written to {filename}")

# ---------- Main ----------
if __name__ == "__main__":
    with open("output_ir.json") as f:
        ir = json.load(f)

    cfg_nodes = build_cfg_from_ir(ir)
    export_cfg_to_dot(cfg_nodes, "cfg.dot")
