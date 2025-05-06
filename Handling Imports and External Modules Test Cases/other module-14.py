#Test importing the same module twice and there is a conflict in the module content

[case testIdenticalImportFromTwice]
from a import x, y, z
from b import x, y, z
[file a.py]
from common import x, y, z
[file b.py]
from common import x, y, z
[file common.py]
x = 3
def y() -> int: return 3
class z: pass
[out]