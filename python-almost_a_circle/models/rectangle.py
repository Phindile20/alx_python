"""Class rectangle inherits from Base class"""
from .base import Base

class Rectangle(Base):
    """Class rectangle inherits from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor to initialize rectangle."""
        super().__init__(id)
        if type(width) is not int:
              raise TypeError("width must be an integer")
        if width <= 0:
              raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
              raise TypeError("height must be an integer")
        if height <= 0:
              raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
              raise TypeError("x must be an integer")
        if x < 0:
              raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
              raise TypeError("y must be an integer")
        if y < 0:
              raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
         """Getter method for width attribute."""
         return self.__width
     
    @width.setter
    def width(self,value):
         """Setter method for width attribute."""
         if type(value) is not int:
              raise TypeError("width must be an integer")
         if value <= 0:
              raise ValueError("width must be > 0")
         self.__width = value

    @property
    def height(self):
         """Getter method for height attribute."""
         return self.__height
     
    @height.setter
    def height(self,value): 
        """Setter method for width attribute.""" 
        if type(value) is not int:
              raise TypeError("width must be an integer")
        if value <= 0:
              raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """Setter method for width attribute."""
        return self.__x
     
    @x.setter
    def x(self,value):
         """Setter method for width attribute."""
         if type(value) is not int:
              raise TypeError("x must be an integer")
         if value < 0:
              raise ValueError("x must be >= 0")
         self.__x = value

    @property
    def y(self):
         """Setter method for width attribute."""
         return self.__y
     
    @y.setter
    def y(self, value):
         """Setter method for width attribute."""
         if type(value) is not int:
              raise TypeError("y must be an integer")
         if value < 0:
              raise ValueError("x must be >= 0")
         self.__x = value

