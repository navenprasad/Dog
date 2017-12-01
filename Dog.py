class Dog:
    def __init__(self):
        self.pos_y = 0
        self.pos_x = 0

    def moveUp(self):
        self.pos_y = self.pos_y + 1

    def getPos(self):
        print str(self.pos_y)
        print str(self.pos_x)

doggy = Dog()   
