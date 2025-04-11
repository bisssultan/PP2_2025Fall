class toUpper:
    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

string = toUpper()
string.getString()
string.printString()
