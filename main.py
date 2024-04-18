

def von_neuman(in_seed, in_n):
    seed = in_seed
    list_random = []
    for i in range(in_n):
        value = seed ** 2
        string_value = str(value)

        delta = 8 - len(string_value)
        if  delta > 0 :
            string_value = delta * '0' + string_value

        init = (len(string_value) - 4) // 2
        seed = int(string_value[init:init + 4])

        list_random.append(seed)

    return list_random

def lcg(in_a, in_c, in_m, in_seed, in_n):
    """
    IBM RANDU: in_a = 2**16 + 3, c = 0, m = 2**31
    Park and Miller: in_a = 2**7, c = 0, m = 2**31 - 1
    Park, Miller and Stockmeyer: in_a = 48271 + 3, c = 0, m = 2**31 - 1
    """

    seed = in_seed
    list_random = []

    for i in range(in_n):
        seed = (in_a * seed + in_c) % in_m

        list_random.append(seed / in_m)

    return list_random


if __name__ == '__main__':
    # List of 10 random numbers using the Linear congruential generator (LCG) algorithm
    print(von_neuman(4321, 10))

    # List of 10 random numbers in the range [0, 1] using the Von Neuman algorithm.
    # This example uses the Park and Miller parameters
    print(lcg(2**7, 0, 2**31 - 1, 1, 10))


    # List of 10 random numbers in the range [0, 100] using the Von Neuman algorithm.
    values = lcg(2**7 + 3, 0, 2**31 - 1, 1, 10)
    for item in values:
        print(item * 100)

    print('END')