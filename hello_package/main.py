from colorit import Colors
from colorit import color


def greet(name, color_=None):
    print(color(f"Hello {name}", color_ or Colors.white))
