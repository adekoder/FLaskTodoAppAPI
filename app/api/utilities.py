import string
import random


def generate_random_string(size=10):
    """ Generate random string """
    chars = string.ascii_lowercase + string.digits
    random_string = ''.join((random.choice(chars) for x in range(size)))
    return random_string

