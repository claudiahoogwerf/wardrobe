from random import randint
from wardrobe import Wardrobe, Material, Witch, Lion

class Narnia():

    def __init__(self,wardrobematerial=Material.WOOD):
        self.lion = Lion()
        self.witch = Witch()
        if isinstance(wardrobematerial,Material):
            self.wardrobematerial = wardrobematerial # wood carbonfiber glass
        else:
            raise TypeError("You're wardrobe material must be of type material")
        self.wardrobe = Wardrobe('My wardrobe',self.wardrobematerial)
        self._narnia_visits = 0

    @property
    def lion(self):
        return self._lion

    @lion.setter
    def lion(self,lion):
        self._lion = lion

    @property
    def witch(self):
        return self._witch

    @witch.setter
    def witch(self,witch):
        self._witch = witch

    @property
    def wardrobe(self):
        return self._wardrobe

    @wardrobe.setter
    def wardrobe(self,wardrobe):
        self._wardrobe = wardrobe

    def make_journey(self):
        while(not self.lion.spoken_to):
            print('Kicking:',self.wardrobe.kick())
            if self.wardrobe.broken:
                self.wardrobe = Wardrobe('My wardrobe',Material.WOOD)
                continue
            print('Opening:',self.wardrobe.open())
            print('Getting in:',self.wardrobe.get_in())
            randomint = randint(0, 100)
            # print("Trying if ", randomint, " is 7")
            if(randomint == 7):
                self.wardrobe.location = 'Narnia'
                self._narnia_visits += 1
                print('In Narnia bitches! Already visit #' + str(self._narnia_visits))
                print(self.witch.fight(self._narnia_visits))
                if not self.witch.alive:
                    self.lion.spoken_to = True
                    return "Spoken to the lion! Was that all?!"

            print('Getting out:',self.wardrobe.get_out())
            print('Closing:',self.wardrobe.close())


narnia = Narnia(Material.GLASS)
print(narnia.make_journey())
