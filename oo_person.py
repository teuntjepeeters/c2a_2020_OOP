class persoon:

    def __init__(self, oogkleur, haarkleur):
        self.__oogkleur = oogkleur
        self.__haarkleur = haarkleur

    def __str__(self):
        return "De kleur ogen zijn {} en de kleur haren zijn {}".\
            format(self.__oogkleur, self.__haarkleur)

    def setOogkleur(self, oogk):
        self.__oogkleur = oogk

    def getOogkleur(self):
        return self.__oogkleur

    def setHaarkleur(self, haark):
        self.__haarkleur = haark

    def getHaarkleur(self):
        return self.__haarkleur


if __name__ == '__main__':
    yade = persoon("bruin", "bruin")
    # yade.setOogkleur("bruin")
    print(yade.getOogkleur())
    yade.setHaarkleur("blond")
    print(yade.getHaarkleur())
    print(yade)

    # wieke = persoon()
    # wieke.setOogkleur("blauw")
    # print(wieke.getOogkleur())
    # wieke.setHaarkleur("groen en blond")
    # print(wieke.getHaarkleur())

    # hans = persoon()
    # print(hans.getOogkleur())