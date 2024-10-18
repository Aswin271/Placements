import math

def count_permutation(strings):
    vowel_list = []
    const_list = []
    str = strings.lower()
    str_list = list(str)

    for i in str_list:
        if i.isalpha():  # Only consider alphabetic characters
            if i in 'aeiou':
                vowel_list.append(i)
            else:
                const_list.append(i)

    len_cons = len(const_list)
    return math.factorial(len_cons)

answer = count_permutation("CDF")
print(answer)  # Output should be 6
