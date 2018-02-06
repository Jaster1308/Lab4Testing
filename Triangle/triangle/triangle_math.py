def area(base, height):

    if base < 0 or height < 0:
        raise ValueError('Base and height must be positive. Was given: {}, height {}'.format(base, height))

    area = base * height / 2
    return area