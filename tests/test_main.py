from unittest import mock

import pytest
from colorit import Colors
from colorit import color

from hello_package.main import greet


@pytest.mark.parametrize(["name", "color_"], [("Mark", Colors.red), ("Jeff", None)])
def test_greet(name, color_):
    with mock.patch("builtins.print") as print_mock:
        greet(name, color_)

    print_mock.assert_called_with(color(f"Hello {name}", color_ or Colors.white))
