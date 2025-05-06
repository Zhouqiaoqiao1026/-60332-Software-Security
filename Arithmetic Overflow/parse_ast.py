# parse_ast.py

import ast
import json

with open("buggy.py","r") as f:
	code = f.read()

tree = ast.parse(code)

def ast_to_dict(node):
	if isinstance(node, ast.AST):
		return{
			"_type": type(node).__name__,
			**{field: ast_to_dict(getattr(node, field))for field in node._fields}
		}
	elif isinstance(node, list):
		return [ast_to_dict(item) for item in node]
	else:
		return node

ast_dict = ast_to_dict(tree)

with open("buggy_ast.json","w")as f:
	json.dump(ast_dict, f, indent=2)

print ("AST saved to buggy_ast.json")


