class InitTest:
    def __init__(self, name):
        # this function can not be used
        self.name = name

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_init(self):
        print "my name is {} age is {}".format(self.name, self.age)

init = InitTest("cc", 16)
init.print_init()
