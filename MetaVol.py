def Meta(nom, param) :
    class MetaVol(object) :
        __name__ = nom
        attr_de_classe = param

        def __init__(self, attr) :
            self.attr = attr

        def foo(self) :
            return ’foo’ + self.attr_de_classe + self.attr
    return LaClasse
MaClasse = Meta(’Toto’, ’bar’)
instance = MaClasse(’baz’) # c’est une instance de Toto ! :)
instance.foo() # retourne ’foobarbaz’
instance2 = MaClasse(’egg’) instance2.foo() # retourne ’foobaregg’