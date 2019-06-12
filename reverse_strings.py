# for or while loop seems most obvious
def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1
# print(reverse_for_loop("test"))

def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1   # can't have length just be len(s) as the list will count from zero and final spot is s[len(s)-1]
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1
# print(reverse_while_loop("test"))

# apparently you can reverse slice a list
# Python slice string syntax is:
# str_object[start_pos:end_pos:step]
# minus runs it backwards
def reverse_slicing(s):
    return s[::1]
# print(reverse_slicing('test'))


# can also do with recursion
# is collecting the s[0] term from each loop and solving the function each time in position
def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]
# print(reverse_recursion("test"))