#!/usr/bin/python3
""" Module for Square class"""


class Square():
    """ Class representing a square """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes instances of the Square class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Computes the area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Computes the perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns a string representation of the Square object """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Creates an instance of the Square class and performs calculations """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
