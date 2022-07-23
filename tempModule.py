def kelToCel(deg):
    return '{}°C'.format(round(int(float(deg)) - 273.15))

def celToKel(deg):

    return '{}K'.format(round(273.15 + int(float(deg))))


def kelToFahren(deg):
    return '{}°F'.format(round(1.8 * (int(float(deg)) - 273.15) + 32))


def fahrenToKel(deg):
    return '{}K'.format(round((int(float(deg)) - 32) * 5 / 9 + 273.15))


def celToFahren(deg):
    return '{}°F'.format(round((int(float(deg)) * 9 / 5) + 32))


def fahrenToCel(deg):
    return '{}°C'.format(round((int(float(deg)) - 32) * 5 / 9))
