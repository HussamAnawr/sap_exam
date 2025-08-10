def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_2nd_highest_num(arr):
    arr_copy = sorted(set(arr))
    return arr_copy[-2] if len(arr_copy) >= 2 else None

print(find_2nd_highest_num([45,11,25,98,74,88,125,15,46,32,78,98,96,99,11,23]))