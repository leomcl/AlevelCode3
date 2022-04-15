import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def emailCheck(value):
    if re.search(regex, value):
        return True
    else:
        return False


def intTypeCheck(value):
    if value.isdigit() is True:
        return True
    else:
        return False


def presenceCheck(value):
    if value == "":
        return False
    else:
        return True
