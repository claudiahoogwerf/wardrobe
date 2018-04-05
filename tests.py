import unittest
from wardrobe import Wardrobe, Material, Witch, Lion

class WardrobeTest(unittest.TestCase):
    """Wardrobe class

    Test the functions of the wardrobe.

    """

    def setUp(self):
        """Setup the test environment."""
        self.glass_wardrobe = Wardrobe('my glass wardrobe',Material.GLASS)
        self.wooden_wardrobe = Wardrobe('my wooden wardrobe',Material.WOOD)
        self.carbonfiber_wardrobe = Wardrobe('my carbon wardrobe',Material.CARBONFIBER)

    def test_rename_wardrobe(self):
        """Test renaming of the wardrobe.
        """
        newname = 'my carbonfiber wardrobe'
        self.carbonfiber_wardrobe.name = newname
        self.assertEqual(self.carbonfiber_wardrobe.name,newname)

    def test_illegal_material_throws_error(self):
        """Test if illegal material throws error
        """
        with self.assertRaises(TypeError):
            unknownmaterial_wardrobe = Wardrobe('my weird wardrobe','ik verzin zelf wel wat')

    def test_kick_wardrobe(self):
        """Test kicking of the wardrobe.
        Test if glass breaks and the rest doesnt break"""
        self.carbonfiber_wardrobe.kick()
        self.glass_wardrobe.kick()
        self.wooden_wardrobe.kick()
        self.assertFalse(self.carbonfiber_wardrobe.broken)
        self.assertFalse(self.wooden_wardrobe.broken)
        self.assertTrue(self.glass_wardrobe.broken)

if __name__ == '__main__':
    unittest.main(verbosity=2)
