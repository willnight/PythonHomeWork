def isfloat(v):
    try:
        float(v)
    except ValueError:
        return False
    except TypeError:
        return False
    return True


def isint(v):
    try:
        int(v)
    except ValueError:
        return False
    except TypeError:
        return False
    return True
