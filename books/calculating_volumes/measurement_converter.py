import pandas as pd
import numpy as np

UNIT_TABLE = {
    "length": {
        "meter": {"symbol": "m", "value": 1, "base": "meter"},
        "kilometer": {"symbol": "km", "value": 1000, "base": "meter"},
        "centimeter": {"symbol": "cm", "value": 0.01, "base": "meter"},
        "millimeter": {"symbol": "mm", "value": 0.001, "base": "meter"},
        "mile": {"symbol": "mi", "value": 1609.34, "base": "meter"},
        "yard": {"symbol": "yd", "value": 0.9144, "base": "meter"},
        "foot": {"symbol": "ft", "value": 0.3048, "base": "meter"},
    },
    "mass": {
        "kilogram": {"symbol": "kg", "value": 1, "base": "kilogram"},
        "gram": {"symbol": "g", "value": 0.001, "base": "kilogram"},
        "milligram": {"symbol": "mg", "value": 0.000001, "base": "kilogram"},
        "ton": {"symbol": "t", "value": 1000, "base": "kilogram"},
        "pound": {"symbol": "lb", "value": 0.453592, "base": "kilogram"},
        "ounce": {"symbol": "oz", "value": 0.0283495, "base": "kilogram"},
    },
    "volume": {
        "liter": {"symbol": "L", "value": 1, "base": "liter"},
        "milliliter": {"symbol": "mL", "value": 0.001, "base": "liter"},
        "cubic_meter": {"symbol": "m³", "value": 1000, "base": "liter"},
        "gallon": {"symbol": "gal", "value": 3.78541, "base": "liter"},
        "quart": {"symbol": "qt", "value": 0.946353, "base": "liter"},
        "pint": {"symbol": "pt", "value": 0.473176, "base": "liter"},
    },
    "temperature": {
        "celsius": {"symbol": "°C", "value": 1, "base": "celsius"},
        "fahrenheit": {"symbol": "°F", "value": (1/1.8), "base": "celsius"},
        "kelvin": {"symbol": "K", "value": 1, "base": "kelvin"},
    },
    "area": {
        "square_meter": {"symbol": "m²", "value": 1, "base": "square_meter"},
        "hectare": {"symbol": "ha", "value": 10000, "base": "square_meter"},
        "acre": {"symbol": "ac", "value": 4046.86, "base": "square_meter"},
        "square_kilometer": {"symbol": "km²", "value": 1000000, "base": "square_meter"},
    }
}



def convert_unit(from_unit, to_unit, value):

    if from_unit == to_unit:
        return value

    

    pass

def convert_area():
    pass

def convert_volume():
    pass

def main():
    pass