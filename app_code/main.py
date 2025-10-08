"""
main.py - Base Converter APK
Version: 0.1
Author: Moses Runanu
Release Date: October 2025

Program Documentation:
This module defines the main Kivy application for the Base Converter APK.
It provides a graphical user interface (GUI) to convert numbers between
Decimal (Base 10), Binary (Base 2), Octal (Base 8), and Hexadecimal (Base 16).

Modules:
- kivy.app.App: Base class for Kivy applications.
- kivy.uix.boxlayout.BoxLayout: Layout class for arranging widgets vertically/horizontally.
- Converter: Contains the logic function `convert_n` for number system conversion.

Classes:
- ConverterLayout: Manages the main app layout and conversion actions.
- ConverterApp: Initializes and runs the Kivy application.

Usage:
1. Run this module to launch the Base Converter app.
2. Enter a number in the input field.
3. Click button holding the source and target number systems to see result.


Dependencies:
- Python 3.x
- Kivy framework
- Converter.py (contains conversion logic)
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from Converter import convert_n  # import logic



class ConverterLayout(BoxLayout):
    """
    The main layout class for the Base Converter app.

    Provides methods to safely convert numbers and update the GUI.

    Methods:
    - safe_convert(num, from_base, to_base): Converts a number safely, handling errors.
    - convert_number(num, from_base, to_base): Converts a number and updates the result label.
    """
      
    def safe_convert(self, num, from_base, to_base):
        """
        Wraps convert_n so errors don't crash the app.
        Returns a result string or an error message.
        """
        try:
            return convert_n(num, from_base, to_base)
        except ValueError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"

    def convert_number(self, num, from_base, to_base):#calls safe convert to make conversions 
        """
        Calls safe_convert and updates the result label in the GUI.

        Args:
            num (str): The number to convert (as string input).
            from_base (int): The base of the input number.
            to_base (int): The base to convert the number into.
        """
        result = self.safe_convert(num, from_base, to_base)
        self.ids.result_label.text = f"Result: {result}"


class ConverterApp(App):
    """
    The main Kivy application class for Base Converter.

    Methods:
       build(): Initializes and returns the ConverterLayout instance.
    """
    def build(self):
        """Builds and returns the main app layout."""
        return ConverterLayout()


if __name__ == "__main__":
    """Runs the Base Converter app."""
    ConverterApp().run()
