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

    def test_set_location_of_wardrobe(self):
        """Test renaming of the wardrobe.
        """
        newlocation= 'Londen'
        self.carbonfiber_wardrobe.location = newlocation
        self.assertEqual(self.carbonfiber_wardrobe.location,newlocation)

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

    def test_open(self):
        """Test opening the wardrobe.
        Test if you can't open it when already open or when you broke it
        Test if you have a open wardrobe afterwards"""
        # Check if the wardrobe is closed
        self.assertTrue(self.glass_wardrobe.closed)
        # Open wardrobe and check if the wardrobe is closed
        self.glass_wardrobe.open()
        self.assertFalse(self.glass_wardrobe.closed)
        # Open wardrobe again and get message that it is already opened. Check if still open
        self.assertEquals(self.glass_wardrobe.open(),'Door is already opened')
        self.assertFalse(self.glass_wardrobe.closed)
        # Break the wardrobe and try opening it again. Show the error
        self.glass_wardrobe.kick()
        self.assertEquals(self.glass_wardrobe.open(),"You already broke it dumbass! It's useless now")

    def test_get_in(self):
        """Test getting in the wardrobe.
        Test if you can't get in when the door is closed or you are already in
        Test if you otherwise are in the closet afterwards"""
        # Check if the wardrobe is closed
        self.assertTrue(self.glass_wardrobe.closed)
        # Open wardrobe and check if the wardrobe is closed
        self.glass_wardrobe.open()
        self.assertFalse(self.glass_wardrobe.closed)
        # Open wardrobe again and get message that it is already opened. Check if still open
        self.assertEquals(self.glass_wardrobe.open(),'Door is already opened')
        self.assertFalse(self.glass_wardrobe.closed)

if __name__ == '__main__':
    unittest.main(verbosity=2)
