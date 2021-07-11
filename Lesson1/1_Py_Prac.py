"""
You can use this class to represent how classy someone
or something is.

"Classy" is interchangable with "fancy".

If you add fancy-looking items, you will increase
your "classiness".

Create a function in "Classy" that takes a string as
input and adds it to the "items" list.

Another method should calculate the "classiness"
value based on the items.

The following items have classiness points associated
with them:
    "tophat" = 2
    "bowtie" = 4
    "monocle" = 5

Everything else has 0 points.
Use the test cases below to guide you!"""

#####################################
# This is the function itself within the class "Classy"
# The functions are:
#   getClassiness()
#   addItem()
#####################################

class Classy:
    def __init__(self):
        self.items = []
        self.count = 0

    def getClassiness(self):
        return self.count

    def addItem(self, strng):
        self.items.append(strng)
        if strng == "tophat":
            self.count += 2
        elif strng == "bowtie":
            self.count += 4
        elif strng == "monocle":
            self.count += 5
        else:
            self.count += 0


#####################################
# Test Cases
#####################################

me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())
