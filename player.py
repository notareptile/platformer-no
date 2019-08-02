from block import Block

class Player(Block):
    size = 20
    def __init__(self, color):
        super().__init__(10, 10, 0, 0, self.size, self.size, color)
    def applygravity(self, gravity):
        self.yvelocity += gravity
    def jump(self, distance):
        self.yvelocity = distance*-1
        self.yup += self.yvelocity
    def checkdestory(self):
        if False: #add stuff here
            self.shoulddestroy = True