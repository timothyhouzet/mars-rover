class Rover:
    """Sets the rovers initial bounds
        Args:
            bounds (str): A string of the upper-right coords of the grid, e.g. '5 5'

    """

    # Direction
    compass = ['N','E','S','W']

    # Constructor
    def __init__(self,bounds):
        self.bounds = bounds

    # Public position(coords)
    def position(self,coords):
        """Sets the rovers initial position
        Args:
            coords (str): A string of the rovers current coords and orientation, e.g. '1 2 N'

        """
        self.coords = coords

    # Public explore(path)
    def explore(self,path):
        """Move a rover to a new location
        Args:
            path (str): A string of instructions to direct the rovers path, e.g. 'LMRMMMLR'

        """
        self.path = path

        # Move and rotate the rover
        for p in self.path.lower():
            # print(p)
            if p == 'm': # move 1 grid point in current direction [N, E, S, W]
                self._forward()
            elif p == 'l': # Rotate 90 degrees left
                self._rotate('l')
            elif p == 'r': # rotate 90 degrees right
                self._rotate('r')


    # Private _forward()
    def _forward(self):
        """Attempts to move the rover forward by 1 grid point in the current direction

        """
        x,y,o = self._convert_coords()

        # Move North
        if o == 'N': y += 1
        # Move East
        if o == 'E': x += 1
        # Move South
        if o == 'S': y -= 1
        # Move West
        if o == 'W': x -= 1

        # Only update self.coords if the attempted move is not out of bounds
        if self._safe(x,y):
            self.coords = ' '.join([str(x),str(y),o])


    # Private _rotate(direction) 
    def _rotate(self,direction):
        """Rotates the rover either left of right by 90 degrees
        Args:
            direction (str): A string of the direction in which to rotate, e.g. 'l' for left, 'r' for right

        """
        x,y,o = self._convert_coords()

        compass = self.compass
        if direction == 'l': # reverse the compass if turning left
            compass = self.compass[::-1]

        for i, d in enumerate(compass):
            if d == o:
                try:
                    o = compass[i + 1]
                except:
                    o = compass[0]
                break

        # Update self.coords
        self.coords = ' '.join([str(x),str(y),o])


    # Private _safe(x,y)
    def _safe(self,x,y):
        """Checks that a rovers position is not out of bounds
        Args:
            x (int): An integer of a potential x coord, e.g. 1
            y (int): An integer of a potential y coord, e.g. 2
        Returns:
            bool: False if out of bounds and True if within bounds

        """
        try:
            xb,yb = list(map(int, self.bounds.split(' ')))
        except:
            exit("Invalid bounds, expected str 'X Y'")

        return (x <= xb) and (y <= yb) and (x >= 0) and (y >= 0)

    # Private _convert_coords()
    def _convert_coords(self):
        """Converts a str of coords and orientation into a list of coords and orientation
        Returns:
            coords (list): A list of the rovers current coords and orientation

        """
        try:
            coords = self.coords.split(' ')
            x = int(coords[0])
            y = int(coords[1])
            if len(coords[2]):
                o = str(coords[2]).upper()
            else:
                exit()
        except:
            exit("Invalid position, expected str 'X Y O'")

        return [x,y,o]