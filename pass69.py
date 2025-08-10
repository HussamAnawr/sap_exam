# to check in github
import math

def find_nums_with_product(nums, target):
    
    for i, v in enumerate(nums):
        if target % v == 0:
            possible = target / v
            if possible in nums:
                return i, nums.index(possible)
    return None


print(find_nums_with_product([6, 8, 4, 2], 32))




###################################################
print(float('-inf'))

def find_divisor(num):
    divisors = [1]
    for i in range(2, int(num / 2) + 1):
        if num % i  == 0:
            divisors.append(i)
    return divisors + [num]

print(find_divisor(900))

def all_combinations(arr):
    result = []

    def backtrack(start, current):
        # Add to results if length >= 2
        if len(current) >= 2:
            result.append(current[:])

        # Generate further combinations
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)  # move to next index
            current.pop()  # backtrack

    backtrack(0, [])
    return result

def find_sigma_product(nums, target):
    all_divisier = find_divisor(target)
    target_divisor = [cd for cd in nums if cd in all_divisier]
    all_possbile_product = {}
    for comp in all_combinations(target_divisor):
        key = tuple(sorted(comp))
        if math.prod(key) == target:
            all_possbile_product[key] =  target
    
    return list(all_possbile_product.keys())




print(find_sigma_product([2, 3, 5 , 10, 1,7, 2, 16, 50], 50))

