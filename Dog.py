class Dog:
    def __init__(self):
        self.pos_y = 0
        self.pos_x = 0
        self.name = ""

    def moveUp(self):
        self.pos_y = self.pos_y + 1

    def setName(self, this_name):
        self.name = this_name

    def getPos(self):
        print str(self.pos_y)
        print str(self.pos_x)
        print self.name

doggy = Dog()
doggy.setName("Scooby")
doggy.getPos()
