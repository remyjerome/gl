from Vol import *
import re
import datetime
import pickle
class Reference(object):
    def __init__(self, reference):
        try:
            self._reference = reference
            if re.match(r"^[a-zA-Z0-9_]{3}$", reference) == None:
                raise ValueError("la reference saisi est invalide")
        except ValueError:
            print("Erreur : La valeur saisie est invalide(la reference doit contenir 3 carracteres de type apha numerique)")
            raise
    @property
    def reference(self):
        return self._reference
    def __call__(self):
        return(self)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __str__(self):
        return "{}".format(self._reference)
class Client(object):
    def __init__(self,nom, prenom, adresse, ref) :
        self._nom = nom
        self._prenom = prenom
        self._adresse = adresse
        self._ref = Reference(ref)
        self._listeReservations = []
    def reserverVol(self, numero, passager, numeroVol, companie):
        date = datetime.datetime.now()
        reservation = Reservation(date, numero, passager, numeroVol, companie)
        self._listeReservations.append(reservation)
        print ("Reservation cree pour le client :\n %s" %(self))
    def listeVols(self, companie):
        """Methode qui permet de recuperer la liste de vol"""
        with open(companie, 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            vols_recupere = mon_depickler.load()
            print vols_recupere
            return vols_recupere
    def __call__(self):
        return self
    def __str__(self):
        return "Nom {}\n Prenom {}\n Adresse {}\n Reference {}".format(self._nom, self._prenom, self._adresse, self._ref)
class Reservation(object):
    def __init__(self, date, numero, passager, numeroVol, companie) :
        self._date = date
        self._numero = numero
        self._passager = passager
        self._etat = None
        self._companie = companie
    def annuler(self):
        self._etat = False
        print ("Reservation numero %s annulee."%(self._numero))
    def confirmer(self):
        self._etat = True
        print ("Reservation numero %s conformee."%(self._numero))
    def __call__(self):
        return self
    def __str__(self):
        return "Reservation numero {} le {}\n Client :\n Passager {}".format(self._numero, self._date, self._client, self._passager)
class Passager(object):
    def __init__(self, nom, prenom) :
        self._nom = nom
        self._prenom = prenom
        print ("Passager : %s %s cree"%(self._nom, self._prenom))
    def __call__(self):
        return self
    def __str__(self):
        return "Nom {} Prenom {}".format(self._nom, self._prenom)
if __name__ == '__main__':
    c1 = Client("Remy", "Jerome", "rue 25 pasteur ", "111")
    p1 = Passager("Remy","Jerome")
    c1.reserverVol("123",p1,"0123456789","air france")
