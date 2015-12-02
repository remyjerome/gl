from Vol import *
def MetaVol(nom, param) :
    class Vol2(object) :
        __name__ = nom
        attr_de_classe = param

        def __init__(self, aeroportDepart, aeroportArrivee, dateDepart, dateArrivee, numeroVol) :
            self._numeroVol = numeroVol
            self._aeroportDepart = aeroportDepart
            self._aeroportArrivee = aeroportArrivee
            self._etatVol = True #Le vol est de base ouvert aux reservation
            try:
                self._dateDepart = dateDepart
                self._dateArrivee = dateArrivee
                if(dateDepart > dateArrivee):
                    raise ValueError("les dates saisies sont invalides")
            except ValueError:
                print("Erreur : Les Dates saisies sont invalides(la date de depart doit-etre inferieure a la date d'arrivee)")
                raise
            self._duree = dateArrivee - dateDepart

        def ouvrirReservation(self):
            self._etatVol = True
            print ("Le vol %s est maintenant ouvert au reservations"%(self._numeroVol.numero))
        def fermerReservation(self):
            self._etatVol = False
            print ("Le vol %s est maintenant ferme au reservations"%(self._numeroVol.numero))
        def _get_numeroVol(self):
            return self._numeroVol
        def _get_etatVol(self):
            if self._etatVol:
                print ("Le vol est ouvert aux reservations.")
            else:
                print("Le vol est ferme aux reservations")
        def __call__(self):
            print(self._numeroVol)
        def __str__(self):
            return "Vol numero {} en provenance de {} et a destination de {} depart prevu a {} et arrivee prevu a {}".format(self._numeroVol, self._aeroportDepart, self._aeroportArrivee, self._dateDepart, self._dateArrivee)
        numeroVol=property(_get_numeroVol)
        etatVol=property(_get_etatVol)

    return Vol

if __name__ == '__main__':
    #Creation des objet Aeroport et Time
    a1 = Aeroport("Clermont", 001, [("Lyon"),("Toulouse"),("Lille")])
    a2 = Aeroport("Lyon", 002, [("Nice"),("Paris"),("Agde")])
    a3 = Aeroport("Nantes", 003,[("Anger"),("Marseille"),("Auxerre")])
    t1=Time(2015, 12,10,12,0)
    t2=Time(2015, 12,10,15,30)
    #Creation d'une meta classVol
    Vol2 = MetaVol('VolGenerique', 'test')
    #Exemple 1 d'instanciation de Vol
    instance = Vol2(a1,a2,t1(),t2(),"1234567890")
    print instance
    #Exemple 2 d'instanciation de Vol
    instance2 = Vol2(a1,a2,t1(),t2(),"1234567893")
    print instance2
