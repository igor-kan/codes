def radix_sort(arr):
    if not arr: return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_exp(arr, exp)
        exp *= 10
    return arr

def counting_sort_exp(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10
    for n in arr: count[(n // exp) % 10] += 1
    for i in range(1, 10): count[i] += count[i-1]
    for n in reversed(arr):
        idx = (n // exp) % 10
        output[count[idx] - 1] = n
        count[idx] -= 1
    return output
