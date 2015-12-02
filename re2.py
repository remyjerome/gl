import pickle
from Vol import *
with open('donnees', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
    print score_recupere