# Tested on Python 3.7
import unittest
from rover import Rover

# Example:
# Remember to import rover.py into your script using: from rover import Rover

# bounds = '5 5'

# rover = Rover(bounds)

# rover1 = Rover(bounds)
# rover1.position('1 2 N')
# rover1.explore('LMLMLMLMM')

# print(f'Rover 1 coords: {rover1.coords}')

# rover2 = Rover(bounds)
# rover2.position('3 3 E')
# rover2.explore('MMRMMRMRRM')

# print(f'Rover 2 coords: {rover2.coords}')

class TestRover(unittest.TestCase):
    
    def test_rover1(self):
        rover = Rover('5 5')
        rover.position('1 2 N')
        rover.explore('LMLMLMLMM')
        result = rover.coords
        self.assertEqual(result, '1 3 N')
    
    def test_rover2(self):
        rover = Rover('5 5')
        rover.position('3 3 E')
        rover.explore('MMRMMRMRRM')
        result = rover.coords
        self.assertEqual(result, '5 1 E')

    def test_rover3(self):
        rover = Rover('100 100')
        rover.position('99 99 N')
        rover.explore('MMMMMMMM')
        result = rover.coords
        self.assertEqual(result, '99 100 N')

if __name__ == '__main__':
    unittest.main()