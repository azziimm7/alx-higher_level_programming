#! usr/bin/python3


"""

A unittest module for the rectangle class

Unittest Classes:
    TestRectangle_init
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_y
    Test_Initialization_order
    TestRectangle_area
    TestRectangle_stdout
    TestRectangle_update_args
    TestRectangle_update_kwargs
"""

import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_init(unittest.TestCase):
    """Unittests to test the initialization of the Rectangle class"""

    def test_is_a_child(self):
        self.assertIsInstance(Rectangle(5, 6), Base)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_two_args(self):
        r1 = Rectangle(2, 4)
        r2 = Rectangle(5, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(5, 6, 7)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 20).id, 20)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__width

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__height

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__x

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__y

    def test_width_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.width, 2)

    def test_width_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.width = 6
        self.assertEqual(r1.width, 6)

    def test_height_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.height, 4)

    def test_width_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.height = 6
        self.assertEqual(r1.height, 6)

    def test_x_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.x, 6)

    def test_x_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.x = 5
        self.assertEqual(r1.x, 5)

    def test_y_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.y, 8)

    def test_y_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.y = 6
        self.assertEqual(r1.y, 6)


class TestRectangle_width(unittest.TestCase):
    """Unittests to test the initialization of the Rectangle's width"""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.3, 5)

    def test_NaN_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 5)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 5)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 5)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b"invalid width", 5)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b"invalid width"), 5)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b"invalid width"), 5)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2], 5)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 5)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2}, 5)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2}), 5)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"invalid dict": 2}, 5)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(4), 5)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 5)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(3), 5)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 5)


class TestRectangle_height(unittest.TestCase):
    """Unittests to test the initialization of the Rectangle's height"""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 5.3)

    def test_NaN_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('nan'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('inf'))

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "invalid height")

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, b"invalid height")

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, bytearray(b"invalid height"), 5)

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, memoryview(b"invalid height"))

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, [1, 2])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, (1, 2))

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {1, 2})

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, frozenset({1, 2}))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {"invalid dict": 2})

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, range(4))

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, True)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, complex(3))

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, 0)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -10)


class TestRectangle_x(unittest.TestCase):
    """Unittests to test the initialization of the Rectangle's x coordinate"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, None)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, 9.5)

    def test_NaN_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, float('nan'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, float('inf'))

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, "invalid x")

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, b"invalid x")

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, bytearray(b"invalid x"))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, memoryview(b"invalid x"))

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, [1, 2])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, (1, 2))

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, {1, 2})

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, frozenset({1, 2}))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, {"invalid dict": 2})

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, range(4))

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, True)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, complex(3))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 5, -10)


class TestRectangle_y(unittest.TestCase):
    """Unittests to test the initialization of the Rectangle's y coordinate"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, None)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 8, 9.5)

    def test_NaN_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, float('nan'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, float('inf'))

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, "invalid y")

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, b"invalid y")

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, bytearray(b"invalid y"))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, memoryview(b"invalid y"))

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, [1, 2])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, (1, 2))

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, {1, 2})

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, frozenset({1, 2}))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, {"invalid dict": 2})

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, range(4))

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, True)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 8, complex(3))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 8, -10)


class Test_Initialization_order(unittest.TestCase):
    """
    Unittests to test the order of initialization of
    the Rectangle's attributes
    """

    def text_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def text_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 5, "invalid x")

    def text_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 5, 8, "invalid y")

    def text_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "invalid height", "invalid x")

    def text_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "invalid height", 8, "invalid y")

    def text_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests to test the area of the rectangle"""

    def test_small_area(self):
        self.assertEqual(Rectangle(3, 5).area(), 15)

    def test_large_area(self):
        a1 = Rectangle(9999999999, 9999999999).area()
        self.assertEqual(a1, 99999999980000000001)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            a1 = Rectangle(3, 5).area(3)

    def test_attribute_changed(self):
        r1 = Rectangle(3, 5)
        r1.height = 3
        self.assertEqual(r1.area(), 9)


class TestRectangle_stdout(unittest.TestCase):
    """Unittest to test the display of the rectangle"""

    @staticmethod
    def capture_from_stdout(rect, method):
        """Capture the output from the stdout to use it in testing

        Args:
            rect (Rectangle): A rectangle instance
            method (str): The method to apply on the rectangle

        Returns:
            The captured value from stdout
        """
        capture = StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        elif method == "display":
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_width_height(self):
        r = Rectangle(2, 4)
        output = self.capture_from_stdout(r, "display").getvalue()
        self.assertEqual("##\n##\n##\n##\n", output)

    def test_display_width_height_x(self):
        r = Rectangle(2, 4, 1)
        output = self.capture_from_stdout(r, "display").getvalue()
        self.assertEqual(" ##\n ##\n ##\n ##\n", output)

    def test_display_width_height_y(self):
        r = Rectangle(2, 4, 0, 1)
        output = self.capture_from_stdout(r, "display").getvalue()
        self.assertEqual("\n##\n##\n##\n##\n", output)

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 1, 2)
        output = self.capture_from_stdout(r, "display").getvalue()
        self.assertEqual("\n\n ##\n ##\n ##\n ##\n", output)

    def test_display_changed_attribute(self):
        r = Rectangle(2, 4)
        r.width = 3
        r.height = 3
        output = self.capture_from_stdout(r, "display").getvalue()
        self.assertEqual("###\n###\n###\n", output)

    def test_display_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 5).display(3)

    def test_str_print_width_height(self):
        r = Rectangle(2, 4)
        actual = self.capture_from_stdout(r, "print").getvalue()
        expected = "[Rectangle] ({}) 0/0 - 2/4\n".format(r.id)
        self.assertEqual(expected, actual)

    def test_str_width_height_x(self):
        r = Rectangle(2, 4, 6)
        self.assertEqual("[Rectangle] ({}) 6/0 - 2/4".format(r.id), str(r))

    def test_str_width_height_x_y(self):
        r = Rectangle(2, 4, 6, 8)
        self.assertEqual("[Rectangle] ({}) 6/8 - 2/4".format(r.id), str(r))

    def test_str_width_height_x_y_id(self):
        r = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual("[Rectangle] (10) 6/8 - 2/4", str(r))

    def test_str_changed_attribute(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.width = 3
        r.height = 3
        self.assertEqual("[Rectangle] (10) 6/8 - 3/3", str(r))

    def test_str_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 5).__str__(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittest to test updating the rectangle attributes"""

    def test_update_no_args(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 6/8 - 2/4", str(r))

    def test_update_one_arg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(12)
        self.assertEqual("[Rectangle] (12) 6/8 - 2/4", str(r))

    def test_update_two_args(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(12, 5)
        self.assertEqual("[Rectangle] (12) 6/8 - 5/4", str(r))

    def test_update_three_args(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(12, 5, 7)
        self.assertEqual("[Rectangle] (12) 6/8 - 5/7", str(r))

    def test_update_four_args(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(12, 5, 7, 9)
        self.assertEqual("[Rectangle] (12) 9/8 - 5/7", str(r))

    def test_update_five_args(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(12, 5, 7, 9, 11)
        self.assertEqual("[Rectangle] (12) 9/11 - 5/7", str(r))

    def test_update_more_than_five_args(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(12, 5, 7, 9, 11, 13)
        self.assertEqual("[Rectangle] (12) 9/11 - 5/7", str(r))

    def test_update_with_None(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(None)
        self.assertEqual("[Rectangle] ({}) 6/8 - 2/4".format(r.id), str(r))

    def test_update_with_None_and_more(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(None, 3, 5, 7)
        self.assertEqual("[Rectangle] ({}) 7/8 - 3/5".format(r.id), str(r))

    def test_update_twice(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(1, 3, 5, 7, 9)
        r.update(12, 5, 7, 9, 11)
        self.assertEqual("[Rectangle] (12) 9/11 - 5/7", str(r))

    def test_update_invalid_width_type(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(12, "invalid width")

    def test_update_width_zero(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(12, 0)

    def test_update_width_negative(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(12, -3)

    def test_update_invalid_height_type(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(12, 3, "invalid height")

    def test_update_height_zero(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(12, 5, 0)

    def test_update_height_negative(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(12, 5, -3)

    def test_update_invalid_x_type(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(12, 3, 5, "invalid x")

    def test_update_x_negative(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(12, 3, 5, -3)

    def test_update_invalid_y_type(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(12, 3, 5, 7, "invalid y")

    def test_update_y_negative(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(12, 3, 5, 7, -3)

    def test_update_args_width_before_height(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(12, "invalid width", "invalid height")

    def test_update_args_width_before_x(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(12, "invalid width", 3, "x")

    def test_update_args_width_before_y(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(12, "invalid width", 3, 5, "invalid y")

    def test_update_args_height_before_x(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(12, 3, "invalid height", "invalid x")

    def test_update_args_height_before_y(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(12, 3, "invalid height", 5, "invalid y")

    def test_update_args_x_before_y(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(12, 3, 5, "invalid x", "invalid y")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittest to test updating the rectangle attributes using keys"""

    def test_update_id_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(id=3)
        self.assertEqual("[Rectangle] (3) 6/8 - 2/4", str(r))

    def test_update_height_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(height=3)
        self.assertEqual("[Rectangle] (10) 6/8 - 2/3", str(r))

    def test_update_width_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(width=3)
        self.assertEqual("[Rectangle] (10) 6/8 - 3/4", str(r))

    def test_update_x_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(x=3)
        self.assertEqual("[Rectangle] (10) 3/8 - 2/4", str(r))

    def test_update_y_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(y=3)
        self.assertEqual("[Rectangle] (10) 6/3 - 2/4", str(r))

    def test_update_two_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(width=3, height=5)
        self.assertEqual("[Rectangle] (10) 6/8 - 3/5", str(r))

    def test_update_three_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(width=3, height=5, x=7)
        self.assertEqual("[Rectangle] (10) 7/8 - 3/5", str(r))

    def test_update_four_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(width=3, height=5, x=7, y=9)
        self.assertEqual("[Rectangle] (10) 7/9 - 3/5", str(r))

    def test_update_five_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(width=3, height=5, x=7, y=9)
        self.assertEqual("[Rectangle] (10) 7/9 - 3/5", str(r))

    def test_update_None_id_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(id=None)
        self.assertEqual("[Rectangle] ({}) 6/8 - 2/4".format(r.id), str(r))

    def test_update_None_id_and_more_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(id=None, width=3, y=5)
        self.assertEqual("[Rectangle] ({}) 6/5 - 3/4".format(r.id), str(r))

    def test_update_kwarg_twice(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(width=3)
        r.update(width=5)
        self.assertEqual("[Rectangle] (10) 6/8 - 5/4", str(r))

    def test_update_invalid_width_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid width")

    def test_update_zero_width_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_negative_width_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_invalid_height_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid height")

    def test_update_zero_height_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_negative_height_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_invalid_x_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid x")

    def test_update_negative_x_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_invalid_y_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid y")

    def test_update_negative_y_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_kwarg_skipped(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(3, 5, height=7)
        self.assertEqual("[Rectangle] (3) 6/8 - 5/4", str(r))

    def test_update_wrong_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(a=3, b=5)
        self.assertEqual("[Rectangle] (10) 6/8 - 2/4", str(r))

    def test_update_some_wrong_kwarg(self):
        r = Rectangle(2, 4, 6, 8, 10)
        r.update(a=3, width=9, b=5, y=3, id=13)
        self.assertEqual("[Rectangle] (13) 6/3 - 9/4", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):

    def test_dictionary_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 5).to_dictionary(3)

    def test_to_dict_output(self):
        actual = Rectangle(10, 2, 1, 9, 1).to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(actual, expected)

    def test_to_dict_changed_attribute(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(3, 5, 7)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
