from dataclasses import dataclass

# Name constants
NAME = "Test_name"
NAME_NONE = None
NAME_LONG = NAME * 100

# Email constants
EMAIL_BASE = 'email'
EMAIL = "email@email.com"
EMAIL_INCORRECT = "emailemail.com"
EMAIL_LONG = EMAIL_BASE * 100 + '@email.com'
EMAIL_NONE = None

# Ico constants
ICO = "27074358"  # default test ico from ARES
ICO_NONE = None
ICO_INCORRECT = "27074350"
ICO_LONG = ICO + "000"

MAX_LENGTH = 255
MAX_LENGTH_ICO = 8

DATA_VALID = {'name': NAME,
              'email': EMAIL,
              'ico': ICO}


def update_dict(key, value):
    data = DATA_VALID.copy()
    data.update({key: value})
    return data


@dataclass
class FormUtils:
    DATA_INVALID_NAME = update_dict('name', NAME_NONE)
    DATA_LONG_NAME = update_dict('name', NAME_LONG)
    DATA_INVALID_EMAIL = update_dict('email', EMAIL_INCORRECT)
    DATA_EMAIL_NONE = update_dict('email', EMAIL_NONE)
    DATA_LONG_EMAIL = update_dict('email', EMAIL_LONG)
    DATA_INVALID_ICO = update_dict('ico', ICO_INCORRECT)
    DATA_INVALID_ICO_NONE = update_dict('ico', ICO_NONE)
    DATA_LONG_ICO = update_dict('ico', ICO_LONG)


@dataclass
class TextError:
    FIELD_REQUIRED = 'This field is required.'
    FIELD_UNIQUE = 'Form with this Ico already exists.'
    NAME_FIELD_LONG = 'Ensure this value has at most 255 characters (it has 900).'
    EMAIL_FIELD_LONG = 'Ensure this value has at most 255 characters (it has 510).'
    ICO_FIELD_LONG = 'Ensure this value has at most 8 characters (it has 11).'
    INVALID_EMAIL = 'Enter a valid email address.'
    INVALID_ICO = 'Enter a valid ico.'
