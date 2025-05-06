This folder contains the following files:
buggy.py 
	A Pyhon test file that will caused a arithmetic Overflow error 
parse_ast.py
	A Python file that converts the test file into a readable ast.json file
buggy_ast.json
	A converted ast.json file 
ast_to_ir.py
	A Python file that converts ast.json to a readable IRep.json file
output_ir.json
	A json file that is in Irep format
ir_to_c.py
	Converts Irep format json file to a .C file to be tested by ESBMC 
buggy.c 
	.c file to be verifed
GeneralCFG.py
	A Python file that prduces cfg
cfg.dot & cfg.png
	A primitive version of the cfg as well as the graph
