

# 1) Accept two user ages as inputs and give us the difference between them. (The Answer should always be a positive output)


age1 = int(input("Please give me your age: "))
age2 = int(input("Please give me the next age: "))

if age1 > age2:
    print("The difference is: " + str(age1 - age2))
else:
    print("The difference is: " + str(age2 - age1))


# 2) Accept 3 user inputs for variables named noun, verb and adjective. Print out a formatted string using the outputs.

noun = input("Please give me a noun: ")
verb = input("please give me a verb: ")
adjective = input("Please give  me an adjective: ")

print(noun.title(),verb,adjective)


# 3) Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors


age = int(input("Please  tell me your age?? "))
if age <= 17:
        print("You're still a kid!")
elif age >= 18:
        print("You are an adult!")
else:
        print("You are a senior!")


# 4) Take in a number from a user input, output the number squared.

numsq = int(input("Enter a number to be squared:  "))
result = numsq **  2
print(result)


# 5) Check the below variables' length. If the length of the word is greater than 5 output True, if it is less than 5, output False


word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

def wordlen(variable):
    if len(variable) > 5:
        print(True)
    else:
        print(False)

wordlen(word1)
wordlen(word2)
wordlen(word3)
wordlen(word4)
wordlen(word5)