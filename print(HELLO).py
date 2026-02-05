class Reverse:
    def __init__(self, S=""):
        self.S = S
    
    def reversing(self):
        return "".join(reversed(self.S))

the_S = input("Enter a string you want to make reversed: ")
def_S = Reverse(the_S)
print(def_S.reversing())