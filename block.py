class Block():
    def __init__(self, xleft, yup, xvelocity, yvelocity, width, height, color):
        self.xleft = xleft
        self.yup = yup
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.width = width
        self.height = height
        self.color = color
        self.shoulddestroy = False

    def move(self):
        self.xleft += self.xvelocity
        self.yup += self.yvelocity

    def checkdestory(self):
        if self.yup > 700:
            self.shoulddestroy = True