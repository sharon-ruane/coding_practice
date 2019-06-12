# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2 digit numbers is 9009 = 99*91
# Find the largest palindrome made from the product of two 3-digit numbers.

# 3 digit numbers = 100 to 999

# x = 'abcdefghi'
# print(x[0])
# print(x[-1])
# for c in range(len(x)//2):
#     print(c, x[c], x[-(c+1)])

# so this way is a bit brute force
palindromes = []
for x in range(10,99):
    for y in range(10,99):
        if y != x:
            val = x*y
            letters = str(val)
            if all(letters[c] == letters[-(c+1)] for c in range(len(letters)//2)):
                print(letters)
                palindromes.append([int(letters), x, y])

palindromes = sorted(palindromes, key=lambda x: x[0])
print("Largest pallindrome is {} = {} * {}".format(palindromes[-1][0], palindromes[-1][1], palindromes[-1][2]))



# makes more sense to start at 99 and work down

num1 = 99
num2 = 98
checker = True
while num1 > 10:
    while num2 > 10:
        val = num2 * (num1)
        # print(num1, num2, val)
        letters = str(val)
        if all(letters[c] == letters[-(c+1)] for c in range(len(letters)//2)):
            checker = True
            print("Largest pallindrome is {} = {} * {}".format(letters, num1, num2))
            break
        else:
            num2 = num2 - 1
    if checker == True:
        break
    num1 = num1 - 1