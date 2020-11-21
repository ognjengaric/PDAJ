import math
import re


def gen_nums(n):
    return list(range(1, n))


def return_primes(nums):
    ret = []
    for i in nums:
        if is_prime(i):
            ret.append(i)
    return ret


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
    ret = []
    for x in nums:
        ret.append(hex(x))
    return ret


def nums_from_hex(nums):
    ret = {}
    for x in nums:
        x = x[2:]
        m = re.findall("[0-9]", x)

        for y in m:
            if y in ret:
                ret[y] += 1
            else:
                ret[y] = 1

    return ret


def main():
    x = 30
    x = gen_nums(x)
    x = return_primes(x)
    x = return_hex(x)
    x = nums_from_hex(x)

    print(x)


if __name__ == "__main__":
    main()


