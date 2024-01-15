#! usr/bin/python3


"""

A unittest module for the square class

Unittest Classes:
    TestSquare_init
    TestSquare_width
    TestSquare_height
    TestSquare_x
    TestSquare_y
    TestSquare_Initialization_order
    TestSquare_area
    TestSquare_stdout
    TestSquare_update_args
    TestSquare_update_kwargs
    TestSquare_to_dictionary
"""

import unittest
import sys
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare_init(unittest.TestCase):
    """Unittests to test the initialization of the Square class"""

    def test_is_a_child(self):
        self.assertIsInstance(Square(5), Base)
        self.assertIsInstance(Square(5), Rectangle)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(5)
        s2 = Square(6)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(2, 4)
        s2 = Square(5, 6)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(1, 2, 3)
        s2 = Square(5, 6, 7)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.id, 4)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 20)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            Square(1, 4, 3, 5).__size

    def test_size_getter(self):
        s1 = Square(2, 4, 6, 8)
        self.assertEqual(s1.size, 2)

    def test_size_setter(self):
        s1 = Square(2, 4, 6, 8)
        s1.size = 6
        self.assertEqual(s1.size, 6)

    def test_width_getter(self):
        s1 = Square(2, 4, 6, 8)
        self.assertEqual(s1.width, 2)

    def test_width_setter(self):
        s1 = Square(2, 4, 6, 8)
        s1.width = 6
        self.assertEqual(s1.width, 6)

    def test_height_getter(self):
        s1 = Square(2, 4, 6, 8)
        self.assertEqual(s1.height, 2)

    def test_height_setter(self):
        s1 = Square(2, 4, 6, 8)
        s1.height = 6
        self.assertEqual(s1.height, 6)

    def test_x_getter(self):
        s1 = Square(2, 4, 6, 8)
        self.assertEqual(s1.x, 4)

    def test_x_setter(self):
        s1 = Square(2, 4, 6, 8)
        s1.x = 5
        self.assertEqual(s1.x, 5)

    def test_y_getter(self):
        s1 = Square(2, 4, 6, 8)
        self.assertEqual(s1.y, 6)

    def test_y_setter(self):
        s1 = Square(2, 4, 6, 8)
        s1.y = 3
        self.assertEqual(s1.y, 3)


class TestSquare_size(unittest.TestCase):
    """Unittests to test the initialization of the Square's size"""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.3)

    def test_NaN_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size")

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b"invalid size")

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b"invalid size"))

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b"invalid size"))

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2])

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2))

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2})

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2}))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"invalid dict": 2})

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(4))

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(3))

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)


class TestSquare_x(unittest.TestCase):
    """Unittests to test the initialization of the Square's x coordinate"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, None)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 9.5)

    def test_NaN_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, float('nan'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, float('inf'))

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "invalid x")

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, b"invalid x")

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, bytearray(b"invalid x"))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, memoryview(b"invalid x"))

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, [1, 2])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, (1, 2))

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, {1, 2})

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, frozenset({1, 2}))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, {"invalid dict": 2})

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, range(4))

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, True)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, complex(3))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -10)


class TestSquare_y(unittest.TestCase):
    """Unittests to test the initialization of the Square's y coordinate"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, None)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 5, 9.5)

    def test_NaN_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, float('nan'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, float('inf'))

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, "invalid y")

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, b"invalid y")

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, bytearray(b"invalid y"))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, memoryview(b"invalid y"))

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, [1, 2])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, (1, 2))

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, {1, 2})

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, frozenset({1, 2}))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, {"invalid dict": 2})

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, range(4))

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, True)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, complex(3))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 5, -10)


class Test_Initialization_order(unittest.TestCase):
    """
    Unittests to test the order of initialization of
    the Square's attributes
    """

    def text_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 5, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "invalid x", "invalid y")


class TestSquare_area(unittest.TestCase):
    """Unittests to test the area of the square"""

    def test_small_area(self):
        self.assertEqual(Square(3).area(), 9)

    def test_large_area(self):
        a1 = Square(9999999999).area()
        self.assertEqual(a1, 99999999980000000001)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            a1 = Square(3).area(3)

    def test_attribute_changed(self):
        s1 = Square(3)
        s1.size = 5
        self.assertEqual(s1.area(), 25)


class TestSquare_stdout(unittest.TestCase):
    """Unittest to test the display of the square"""

    @staticmethod
    def capture_from_stdout(square, method):
        """Capture the output from the stdout to use it in testing

        Args:
            square (Square): A square instance
            method (str): The method to apply on the square

        Returns:
            The captured value from stdout
        """
        capture = StringIO()
        sys.stdout = capture
        if method == "print":
            print(square)
        elif method == "display":
            square.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_size(self):
        s = Square(2)
        output = self.capture_from_stdout(s, "display").getvalue()
        self.assertEqual("##\n##\n", output)

    def test_display_size_x(self):
        s = Square(2, 1)
        output = self.capture_from_stdout(s, "display").getvalue()
        self.assertEqual(" ##\n ##\n", output)

    def test_display_size_y(self):
        s = Square(2, 0, 1)
        output = self.capture_from_stdout(s, "display").getvalue()
        self.assertEqual("\n##\n##\n", output)

    def test_display_width_height_x_y(self):
        s = Square(2, 1, 2)
        output = self.capture_from_stdout(s, "display").getvalue()
        self.assertEqual("\n\n ##\n ##\n", output)

    def test_display_changed_attribute(self):
        s = Square(2)
        s.size = 3
        output = self.capture_from_stdout(s, "display").getvalue()
        self.assertEqual("###\n###\n###\n", output)

    def test_display_one_arg(self):
        with self.assertRaises(TypeError):
            Square(4).display(3)

    def test_str_print_size(self):
        s = Square(2)
        actual = self.capture_from_stdout(s, "print").getvalue()
        expected = "[Square] ({}) 0/0 - 2\n".format(s.id)
        self.assertEqual(expected, actual)

    def test_str_size_x(self):
        s = Square(2, 4)
        self.assertEqual("[Square] ({}) 4/0 - 2".format(s.id), str(s))

    def test_str_size_x_y(self):
        s = Square(2, 6, 8)
        self.assertEqual("[Square] ({}) 6/8 - 2".format(s.id), str(s))

    def test_str_size_x_y_id(self):
        s = Square(2, 6, 8, 10)
        self.assertEqual("[Square] (10) 6/8 - 2", str(s))

    def test_str_changed_attribute(self):
        s = Square(2, 6, 8, 10)
        s.size = 3
        self.assertEqual("[Square] (10) 6/8 - 3", str(s))

    def test_str_one_arg(self):
        with self.assertRaises(TypeError):
            Square(4, 5).__str__(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittest to test updating the square attributes"""

    def test_update_no_args(self):
        s = Square(2, 6, 8, 10)
        s.update()
        self.assertEqual("[Square] (10) 6/8 - 2", str(s))

    def test_update_one_arg(self):
        s = Square(2, 6, 8, 10)
        s.update(12)
        self.assertEqual("[Square] (12) 6/8 - 2", str(s))

    def test_update_two_args(self):
        s = Square(2, 6, 8, 10)
        s.update(12, 5)
        self.assertEqual("[Square] (12) 6/8 - 5", str(s))

    def test_update_three_args(self):
        s = Square(2, 6, 8, 10)
        s.update(12, 5, 7)
        self.assertEqual("[Square] (12) 7/8 - 5", str(s))

    def test_update_four_args(self):
        s = Square(2, 6, 8, 10)
        s.update(12, 5, 7, 9)
        self.assertEqual("[Square] (12) 7/9 - 5", str(s))

    def test_update_more_than_four_args(self):
        s = Square(2, 6, 8, 10)
        s.update(12, 5, 9, 11, 7)
        self.assertEqual("[Square] (12) 9/11 - 5", str(s))

    def test_update_with_None(self):
        s = Square(2, 6, 8, 10)
        s.update(None)
        self.assertEqual("[Square] ({}) 6/8 - 2".format(s.id), str(s))

    def test_update_with_None_and_more(self):
        s = Square(2, 6, 8, 10)
        s.update(None, 3, 7)
        self.assertEqual("[Square] ({}) 7/8 - 3".format(s.id), str(s))

    def test_update_twice(self):
        s = Square(2, 6, 8, 10)
        s.update(1, 3, 7, 9)
        s.update(12, 5, 9, 11)
        self.assertEqual("[Square] (12) 9/11 - 5", str(s))

    def test_update_invalid_size_type(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(12, "invalid size")

    def test_update_size_zero(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(12, 0)

    def test_update_size_negative(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(12, -3)

    def test_update_invalid_x_type(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(12, 3, "invalid x")

    def test_update_x_negative(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(12, 3, -3)

    def test_update_invalid_y_type(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(12, 3, 7, "invalid y")

    def test_update_y_negative(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(12, 3, 7, -3)

    def test_update_args_size_before_x(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(12, "invalid size", "invalid x")

    def test_update_args_size_before_y(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(12, "invalid size", 3, "invalid y")

    def test_update_args_x_before_y(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(12, 3, "invalid x", "invalid y")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittest to test updating the square attributes using keys"""

    def test_update_id_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(id=3)
        self.assertEqual("[Square] (3) 6/8 - 2", str(s))

    def test_update_size_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(size=3)
        self.assertEqual("[Square] (10) 6/8 - 3", str(s))

    def test_update_x_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(x=3)
        self.assertEqual("[Square] (10) 3/8 - 2", str(s))

    def test_update_y_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(y=3)
        self.assertEqual("[Square] (10) 6/3 - 2", str(s))

    def test_update_two_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(size=3, x=5)
        self.assertEqual("[Square] (10) 5/8 - 3", str(s))

    def test_update_three_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(size=3, y=5, x=7)
        self.assertEqual("[Square] (10) 7/5 - 3", str(s))

    def test_update_four_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(size=3, id=5, x=7, y=9)
        self.assertEqual("[Square] (5) 7/9 - 3", str(s))

    def test_update_None_id_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(id=None)
        self.assertEqual("[Square] ({}) 6/8 - 2".format(s.id), str(s))

    def test_update_None_id_and_more_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(id=None, size=3, y=5)
        self.assertEqual("[Square] ({}) 6/5 - 3".format(s.id), str(s))

    def test_update_kwarg_twice(self):
        s = Square(2, 6, 8, 10)
        s.update(size=3)
        s.update(size=5)
        self.assertEqual("[Square] (10) 6/8 - 5", str(s))

    def test_update_invalid_size_kwarg(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid size")

    def test_update_zero_size_kwarg(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_negative_size_kwarg(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-5)

    def test_update_invalid_x_kwarg(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid x")

    def test_update_negative_x_kwarg(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_invalid_y_kwarg(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid y")

    def test_update_negative_y_kwarg(self):
        s = Square(2, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_kwarg_skipped(self):
        s = Square(2, 6, 8, 10)
        s.update(3, 5, x=7)
        self.assertEqual("[Square] (3) 6/8 - 5", str(s))

    def test_update_wrong_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(a=3, b=5)
        self.assertEqual("[Square] (10) 6/8 - 2", str(s))

    def test_update_some_wrong_kwarg(self):
        s = Square(2, 6, 8, 10)
        s.update(a=3, size=9, b=5, y=3, id=13)
        self.assertEqual("[Square] (13) 6/3 - 9", str(s))


class TestSquare_to_dictionary(unittest.TestCase):

    def test_dictionary_one_arg(self):
        with self.assertRaises(TypeError):
            Square(3).to_dictionary(3)

    def test_to_dict_output(self):
        actual = Square(10, 1, 9, 1).to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'size': 10}
        self.assertEqual(actual, expected)

    def test_to_dict_changed_attribute(self):
        r1 = Square(10, 1, 9)
        r2 = Square(3, 5, 7)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
