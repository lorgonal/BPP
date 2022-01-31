import pdb

# pdb.set_trace()

sample = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
sample2 = [3, 4, 8, 5, 5, 22, 13]


def get_max(lists):
    max_list = [max(lis) for lis in lists]
    return max_list


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


def filter_prime(lis):
    return list(filter(is_prime, lis))


print(filter_prime(sample2))

print(get_max(sample))
