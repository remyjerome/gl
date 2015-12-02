class A(object):
    def __init__(self):
        self._B = None
    def addB(self, B):
        self._B = B
        self._B.setA(self)
    @property
    def B(self):
        return self._B
    @B.setter
    def setB(self, B):
        self._B = B
    def __call__(self):
        return self
    def __str__(self):
        return "Objet A : B {}".format(self._B)

class B(object):
    def __init__(self):
        self._A = None
    def addA(self, A):
        self._A = A
        self._A.setB(self)
    @property
    def A(self):
        return self._A
    @A.setter
    def setA(self, A):
        self._A = A
    def __call__(self):
        return self
    def __str__(self):
        return "Objet B : A {}".format(self._A)
if __name__ == '__main__':
    a = A()
    b = B()
    a.addB(b)
    b.addA(a)
    print a
    print b