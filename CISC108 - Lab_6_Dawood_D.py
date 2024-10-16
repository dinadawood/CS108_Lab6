"""
Course: CISC108
Assignment: Lab 06
Author: Dina Dawood
"""

from cisc108 import assertEqual

# Question 1:

inventory = {
    'gold': 500,
    'pouch': ['flint','twine','gemstone'],
    'backpack': ['xylophone','dagger','bedroll','breadloaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['gold'] += 50

# Question 2:

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for key in prices:
    print(key)
    print("price: ", prices[key])
    
# Question 3:

def alphabet(string):
    '''
    Consumes a string from user & prints table of letters with # of occurrence
    Parameters:
        string: (str) - random string given by user
    Returns:
        None
    '''
    alpha = {}
    for letter in string:
        if letter not in alpha:
            alpha[letter] = 1
        else:
            alpha[letter] += 1
    for char in range(97, 123):
        letter = chr(char)
        if letter not in alpha:
            pass
        else:
            print(letter, ": ", alpha[letter])
            
user_str = str(input("Enter a string: ").lower())
alphabet(user_str)
    
# Question 4:

def Erle():
    '''
    Consumes no parameters/returns; reads file and displays it then finds
    frequency of occurrence for each word and displays total number.
    Parameters:
        None
    Returns:
        None
    '''
    Erle = {}
    file_handle = open(file_name)
    txt = file_handle.read()
    file_handle.close()
    
    for word in txt.split():
        if word not in Erle:
            Erle[word] = 1
        else:
            Erle[word] += 1
    print(len(Erle))
    print(Erle)

file_name = input("Enter name of file: ")
Erle()

# Question 5:
'''
Completed program attached in other file
-> process_csv_file.py
'''
    
# Question 6:

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        ''' 
        Consumes four arguments; creates class Triangle and produces sides and angles
        Parameters:
            self
            angle1: (int) - angle 1 of triangle
            angle2: (int) - angle 2 of triangle
            angle3: (int) - angle 3 of triangle
        Returns:
            check_angles: (bool)
        '''
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    number_of_sides = 3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False


my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

# Question 7:

class Car(object):
    def __init__(self, color, style):
        ''' 
        Consumes three args; creates class Car & produces decription & color change
        Parameters:
            self
            color: (str) - string of color of car
            style: (str) - string of style of car
        Returns:
            None
        '''
        self.color = color
        self.style = style
    wheels = 4
    
    def showDescription(self):
        ''' 
        Consumes one arg; produces decription
        Parameters:
            self
        Returns:
            None
        '''
        print("This car is a", self.color, self.style)
        
    def changeColor(self, s):
        ''' 
        Consumes one arg; produces color change
        Parameters:
            self
        Returns:
            None
        '''
        self.color = s
        
my_car = Car("Red", "Murano")
my_car.showDescription()
my_car.changeColor("Black")
my_car.showDescription()


if __name__ == "__main__":
    pass