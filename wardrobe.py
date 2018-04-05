from enum import Enum

class Material(Enum):
        WOOD = 'Wood'
        CARBONFIBER = 'CarbonFiber'
        GLASS = 'Glass'

class Wardrobe():
    def __init__(self,name='',material=Material.WOOD):
        #Course labels.
        self.name = name
        if isinstance(material,Material):
            self._material = material # wood carbonfiber glass
        else:
            raise TypeError("Input must be a material")
        self._closed = True
        self._in_wardrobe = False
        self.broken = False

    def __str__(self):
        return self._name + ' ' + self._material.value + ' '  + str(self._closed)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def broken(self):
        return self._broken

    @name.setter
    def broken(self,broken):
        self._broken = broken

    def open(self):
        if self._broken == True:
            return "You already broke it dumbass! It's useless now"
        else:
            if self._closed == False:
                return 'Door is already opened'
            else:
                self._closed = False
                return 'Opened the door'

    def close(self):
        if self._broken == True:
            return "You already broke it dumbass! It's useless now"
        else:
            if self._closed == True:
                return 'Door is already closed'
            else:
                self._closed = True
                return 'Closed the door'

    def get_in(self):
        if self._broken == True:
            return "You already broke it dumbass! It's useless now"
        else:
            if self._in_wardrobe == True:
                return 'You are already in the closet'
            else:
                self._in_wardrobe = True
                return "You've got in the closet. Now what?"

    def get_out(self):
        if self._in_wardrobe == False:
            return "You were already out of the closet."
        else:
            self._in_wardrobe = False
            return "You've escaped out of the closet!"

    def kick(self):
        if self._in_wardrobe == True:
            return "Not enough room to kick it! Get out first"
        else:
            if self._material == Material.GLASS:
                self._broken = True
                return "You broke the closet!"
            elif self._material == Material.CARBONFIBER:
                return 'A little damaged, but not broken.'
            else:
                return "Whatever! Nothing happened"
