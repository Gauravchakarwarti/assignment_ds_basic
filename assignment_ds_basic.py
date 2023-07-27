# 1. Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

# Solution:

def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num

        if complement in seen:
            pairs.append((num, complement))

        seen.add(num)

    return pairs


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10

result = find_pairs_with_sum(arr, target_sum)
print("Pairs with sum {}:".format(target_sum))
print(result)


# 2. Q2. Write a program to reverse an array in place? 
#        In place means you cannot create a new array. You have to update the original array.

# Solution

def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        
        arr[left], arr[right] = arr[right], arr[left]

       
        left += 1
        right -= 1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original array:", arr)

reverse_array_in_place(arr)
print("Reversed array:", arr)


# 3.  Write a program to check if two strings are a rotation of each other?

# Solution:

def are_strings_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concatenated_str = str1 + str1

    if str2 in concatenated_str:
        return True
    else:
        return False


string1 = "zabcde"
string2 = "cdezab"

if are_strings_rotations(string1, string2):
    print("Yes, {} and {} are rotations of each other.".format(string1, string2))
else:
    print("No, {} and {} are not rotations of each other.".format(string1, string2))



# 4. Write a program to print the first non-repeated character from a string

# Solution:

def first_non_repeated_character(input_string):
    char_count = {}

    
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

   
    for char in input_string:
        if char_count[char] == 1:
            return char

   
    return None


input_str = "aabbcdeeffg"
result = first_non_repeated_character(input_str)

if result:
    print("The first non-repeated character is:", result)
else:
    print("No non-repeated character found in the string.")


# 5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

# Solution:

def tower_of_hanoi(n, source, destination, intermediate):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, intermediate, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, intermediate, destination, source)


num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')


# 6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# soluton:

def is_operator(char):
    return char in "+-*/"

def postfix_to_prefix(postfix_expr):
    stack = []

    for char in postfix_expr:
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expr = char + operand1 + operand2
            stack.append(prefix_expr)

    return stack[0]


postfix_expr = "342*+15+-"
prefix_expr = postfix_to_prefix(postfix_expr)
print("Prefix Expression:", prefix_expr)


# 7. Write a program to convert prefix expression to infix expression.

# Solution:

def is_operator(char):
    return char in "+-*/"

def prefix_to_infix(prefix_expr):
    stack = []

    for char in reversed(prefix_expr):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expr = f"({operand1}{char}{operand2})"
            stack.append(infix_expr)

    return stack[0]


prefix_expr = "-+*34215"
infix_expr = prefix_to_infix(prefix_expr)
print("Infix Expression:", infix_expr)
