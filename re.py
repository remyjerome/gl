import pickle
from Vol import *
a1 = Aeroport("Clermont", 001, [("Lyon"),("Toulouse"),("Lille")])
a2 = Aeroport("Lyon", 002, [("Nice"),("Paris"),("Agde")])
t1=Time(2015, 12,10,12,0)
t2=Time(2015, 12,10,15,30)
vol = Vol(a1,a2,t1(),t2(),"1234567890")
with open('donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(vol)