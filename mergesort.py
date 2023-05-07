def merge(s1, s2, s):
    i, j = 0, 0
    while i + j < len(s):
        if (s1[i] < s2[j] and i < len(s1)) or j == len(s2):
            s[i+j] = s1[i]
            i = i + 1
        else:
            s[i+j] = s2[j]
            j += 1

def divide(data):
    n = len(data)
    if n > 1:
        mid = n // 2
        data_left = data[:mid]
        data_right = data[mid:n]
        divide(data_left)
        divide(data_right)
        merge(data_left, data_right, data)
    return data

unsorted_numbers = [16,10,21,45]
print(divide(unsorted_numbers))
