class bird:
    def __init__(self):
        print("Bird is ready!")
    def whoisthis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")

class penguin(bird):
    def __init__(self):
        print("Penguin is ready!")
        super().__init__()
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("Run faster")

object1=penguin()
object1.whoisthis()
object1.swim()
object1.run()
    