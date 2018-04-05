import unittest
from wardrobe import Wardrobe
import logging

class WardRobeTest(unittest.TestCase):
    """Wardrobe class

    Test the functions of the wardrobe.

    """

    def setUp(self):
        """Setup the test environment."""
        glass_wardrobe = Wardrobe('my glass wardrobe',Material.GLASS)
        wooden_wardrobe = Wardrobe('my wooden wardrobe',Material.WOOD)
        carbonfiber_wardrobe = Wardrobe('my carbon wardrobe',Material.CARBONFIBER)

    def rename_wardrobe(self):
        """Test renaming of the wardrobe.
        """
        newname = 'my carbonfiber wardrobe'
        carbonfiber_wardrobe.name(newname)
        self.assertEquals(carbonfiber_wardrobe.name,newname)

    def kick_wardrobe(self):
        """Test kicking of the wardrobe."""
        carbonfiber_wardrobe.kick()
        self.assertEquals(carbonfiber_wardrobe.broken,True)

    if __name__ == '__main__':
           unittest.main(verbosity=3)
