import profile
import random


def random_sort(n):
    return sorted([random.random() for i in range(n)])


profile.run("random_sort(2000000)")