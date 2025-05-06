#The circular import inheritance issue. Modules `a` and `d` import each other, and there is an inheritance relationship between them.

[case testSuperclassInImportCycle]
import a
import d
a.A().f(d.D())
[file a.py]
if 0:
    import d
class B: pass
class C(B): pass
class A:
    def f(self, x: B) -> None: pass
[file d.py]
import a
class D(a.C): pass