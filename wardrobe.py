from enum import Enum
from random import randint

class Material(Enum):
        WOOD = 'Wood'
        CARBONFIBER = 'CarbonFiber'
        GLASS = 'Glass'

class Wardrobe():
    def __init__(self,name='',material=Material.WOOD,location='Middle of nowhere'):
        self.name = name
        if isinstance(material,Material):
            self.material = material # wood carbonfiber glass
        else:
            raise TypeError("Input must be a material")
        self.closed = True
        self.in_wardrobe = False
        self.broken = False
        self.location = location

    def __str__(self):
        return self.name + ' ' + self.material.value + ' '  + str(self.closed)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def broken(self):
        return self._broken

    @broken.setter
    def broken(self,broken):
        self._broken = broken

    @property
    def closed(self):
        return self._closed

    @closed.setter
    def closed(self,closed):
        self._closed = closed

    @property
    def in_wardrobe(self):
        return self._in_wardrobe

    @in_wardrobe.setter
    def in_wardrobe(self,in_wardrobe):
        self._in_wardrobe = in_wardrobe

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self,location):
        self._location = location

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self,material):
        self._material = material

    def open(self):
        if self.broken:
            return "You already broke it dumbass! It's useless now"

        if not self.closed:
            return 'Door is already opened'

        self.closed = False
        return 'Opened the door'

    def close(self):
        if self.broken:
            return "You already broke it dumbass! It's useless now"

        if self.closed:
            return 'Door is already closed'

        self.closed = True
        return 'Closed the door'

    def get_in(self):
        if self.broken:
            return "You already broke it dumbass! It's useless now"

        if self.closed:
            return "Open the door first"

        if self.in_wardrobe:
            return 'You are already in the closet'

        self.in_wardrobe = True
        return "You've got in the closet. Now what?"

    def get_out(self):
        if not self.in_wardrobe:
            return "You were already out of the closet."

        self.in_wardrobe = False
        return "You've escaped out of the closet!"

    def kick(self):
        if self.in_wardrobe:
            return "Not enough room to kick it! Get out first"

        if self.material == Material.GLASS:
            self.broken = True
            return "You broke the closet!"
        elif self.material == Material.CARBONFIBER:
            return 'A little damaged, but not broken.'

        return "Whatever! Nothing happened"


class Lion():
    def __init__(self,spoken_to=False):
        self.spoken_to = spoken_to

    def __str__(self):
        return self.spoken_to

    @property
    def spoken_to(self):
        return self._spoken_to

    @spoken_to.setter
    def spoken_to(self,spoken_to):
        self._spoken_to = spoken_to

class Witch():
    def __init__(self,alive=True):
        self.alive = alive

    def __str__(self):
        return self._alive

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self,alive):
        self._alive = alive

    def fight(self,visits):
        randomint = randint(visits, 101)
        if(randomint == 101):
            self.alive = False
            return 'I won! That was easy!'

        return 'I lost and she is still alive :(. What the hell!'
