import random

class Hider:
    """Code for Hiter"""

    def __init__(self):
        """Variable holder"""
        self.location = random.randint(1, 1000)
        self.distance = [0, 0]
    
    
    def watch(self, location):
        """Keeps track of the location of the Seeker compared to the Hider"""
        distance = abs(self.location - location)
        self.distance.append(distance)



    def get_hint(self):
        """Gives hints dependinf on how close of far the seeker is."""
        if self.distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self.distance[-1] > self.distance[-2]:
            hint = "(^.^) Getting Colder!"
        elif self.distance[-1] < self.distance[-2]:
            hint = "(>.<) Getting warmer!"
        return hint
        
# TODO: Define the Hider class here