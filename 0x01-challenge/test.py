#!/usr/bin/python3
""" Module for square class"""


class Square():
    """ Square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Function to inotialize instances"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Function to find area"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Function to find perimeter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Print objects in string format"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Create a square"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
