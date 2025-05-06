#Circular import dependency issues

[case testImportCycleStability1]
import x
[file x.py]
def f() -> str: return ''
class Base:
    attr = f()
def foo():
    import y
[file y.py]
import x
class Sub(x.Base):
    attr = x.Base.attr
[out]