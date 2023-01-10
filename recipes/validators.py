from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError

import pint

valid_unit_measurements = ['pounds', 'lbs', 'oz', 'gram']

def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as message:
        raise ValidationError(f"{message}")
    except:
        raise ValidationError(f"{value} is not a valid unit of measure")
    # if value not in valid_unit_measurements:
    #     raise ValidationError(f"{value} is not a valid unit of measure")