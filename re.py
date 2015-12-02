class A(object):
    def __init__(self, B):
        self._B = None
    def addB(self, B):
        if(B is None):
            if(B.getA is None):
                B.getA.setB(None)
            self.setB(B)
            B.setA(this)
    @property
    def getB(self):
        return self._B
    @property
    def setB(self, B):
        self._B = B
    def __call__(self):
        pass
    def __str__(self):
        pass

class B(object):
    def __init__(self, A):
        self._A = None
    def addA(self):
        if(A is None):
            if(A.getB is None):
                A.getB.setA(None)
            self.setA(A)
            A.setB(this)
    @property
    def getA(self):
        return self._A
    @property
    def setA(self, B):
        self._A = A
    def __call__(self):
        pass
    def __str__(self):
        pass