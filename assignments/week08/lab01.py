"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle :

    def __init__(self, legth , width ):
        self.__length = length
        self.__width  = width

    def getArea(self):
        area = self.__length * self.__width
        return f"Area = {area}"

    def getPerimeter(self):
        perimeter = 2 * (self.__length + self.__width)
        return f"Perimeter = {perimeter}"
    
    def isSquare(self):
        if self.__length == self.__width:
            return f"True"
        else :
            return f"False"        

rectangle = Rectangle(10,5)      
print(rectangle.getArea())  
rectangle.getPerimeter
print(rectangle.isSquare())
