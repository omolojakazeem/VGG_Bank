#Question 1 - Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def get_upper_case(word):
    global new_upper_word
    for upper in word:
        if upper.isupper():
            new_upper_word += upper
    return new_upper_word
    

def get_lower_case(word):
    global new_lower_word
    for lower in word:
        if lower.islower():
            new_lower_word += lower
    return new_lower_word

my_word = input("Enter the word: ")
new_upper_word = ''
new_lower_word = ''
upper_case_xter = get_upper_case(my_word)
lower_case_xter = get_lower_case(my_word)
print(f"The Upper Case Character in the word ({my_word}) is ({upper_case_xter}) and the length is {len(upper_case_xter)}")
print(f"The Lower Case Character in the word ({my_word}) is ({lower_case_xter}) and the length is {len(lower_case_xter)}")

#Question 2 - Write a Python function to find the Max of three numbers

def max_number(*args):
    for i in range(1,length+1):
        numbers = int(input(f"Enter the number in position {i}: "))
        lister.append(numbers)
    return max(lister)


lister = []
length = int(input("Enter how many numbers?: "))
print(max_number(lister))


#Question 3 - Write a Python function that takes a number as a parameter and check the number is prime or not.

def prime_number(number):
    for x in range(2,number):
        if (number%x) == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
    return number


while True:
    try:
        my_number = int(input("Enter the Number: "))
        if my_number < 1:
            print("Enter a number greater than 1")
        else:
            prime_number(my_number)
    except ValueError:
        print("Invalid Number")
