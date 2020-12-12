import math
import re
from collections import Counter
from multiprocessing import Pool


def gen_nums(n):
    return (x for x in range(1, n))


def is_prime(num):
    if num > 1:

        for i in range(2, math.ceil(math.sqrt(num)) + 1):

            if (num % i) == 0:
                continue
        else:
            return return_hex(num)

    else:
        return return_hex(num)


def return_hex(num):
    hex_num = hex(num)
    return reformat_hex(hex_num)


def reformat_hex(num):
    temp = num[2:]
    return nums_from_hex(temp)


def nums_from_hex(hex_num):
    num = re.findall("[0-9a-zA-Z]", hex_num)
    return num


def append_arrays(arr):
    nums = []
    [nums.extend(x) for x in arr]
    return nums


def main():
    x = 1000000
    x = gen_nums(x)

    with Pool() as pool:
        nums = pool.map(is_prime, x)

    nums = append_arrays(nums)
    nums = Counter(nums)

    print(nums)


if __name__ == "__main__":
    main()
