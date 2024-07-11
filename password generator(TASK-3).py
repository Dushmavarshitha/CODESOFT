import random
import string

def generate_password(length):
    chars= string.ascii_letters + string.digits + string.punctuation #the combination of chars to establish the wanted length of string
    password = ''.join(random.choices(chars, k=length))#to get random numbers and chars and symbols for perfect password
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Length must be greater than zero.")
        else:
            password = generate_password(length)
            print(f"the {length} length genarated Password is: {password}")
    except ValueError:
        print("input is invalid. please enter a valid integer.") #this is for when we enter any thing instead of number

if __name__ == "__main__":
    main()
