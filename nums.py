import math


def gen_nums(n):
    return list(range(1, n))


def return_primes(nums):
    ret = []
    for i in nums:
        if i > 1:

            for j in range(2, math.ceil(math.sqrt(i))+1):

                if (i % j) == 0:
                    break
            else:
                ret.append(i)

        else:
            ret.append(i)
    return ret


def return_hex(nums):
    ret = []
    for x in nums:
        ret.append(hex(x))
    return ret


print(return_hex(return_primes(gen_nums(30))))
