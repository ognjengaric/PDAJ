import math
import re
from collections import Counter


def gen_nums(n):
    return list(range(1, n))


def return_primes(nums):
    return [x for x in nums if is_prime(x)]


def is_prime(num):
    if num > 1:

        for i in range(2, math.ceil(math.sqrt(num)) + 1):

            if (num % i) == 0:
                return False
        else:
            return True

    else:
        return True


def return_hex(nums):
    return [hex(x) for x in nums]


def reformat_hex(nums):
    return [x[2:] for x in nums]


def nums_from_hex(hex_nums):
    nums = []

    temp_nums = [re.findall("[0-9]", x) for x in hex_nums]
    [nums.extend(el) for el in temp_nums]
    return Counter(nums)



def main():
    x = 30
    x = gen_nums(x)
    x = return_primes(x)
    x = return_hex(x)
    x = reformat_hex(x)
    x = nums_from_hex(x)

    print(x)


if __name__ == "__main__":
    main()


