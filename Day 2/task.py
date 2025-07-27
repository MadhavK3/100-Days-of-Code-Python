# subscripting
print("Hello"[4])

print("Hello"[-1])

#string
print("123" + "456")     # Concatination takes place her as both are string

# Integers
print(123 +456)

# large integers
print(1_23_45_678)  # we can use such spaces for more understanding for the reader

#float
print(5.55)

len("Hello")

# to know type of data type
print(type("hello"))
print(type(123))
print(type(43.49))
print(type(True))


#type casting
print("123" +"456")  # here concatination 👍

# to do maths
print(int("123") + int("456"))

# some different case for this
# print(int("123") + int("abc"))        this gives error


# Different function
int()
float()
str()
bool()


# To Do
print("Number of letters in your name: " + str(len(input("Enter your name:-  "))))


print("My age: " + str(12))
print(123+456)
print(7-3)
print(3*3)
print(6/3)
print(6//3)       # this is useful to take only integers not decimal as "/" gives decimal values

print(8**2)  # for power

# pedmas
#
# ()
# **
# * or /
# +  or -

print(3 * 3 + 3 / 3 - 3)

# for adjusting for 3 I just added the bracket
print(int(3 * (3 + 3) / 3 - 3))

bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))

# for rounding of the function is as follows
print(round(bmi))

# it is used for no of digits as we want

print(round(bmi,3))       # 3 digits after decimal



# Assignment Operators
score = 0
print(score)
score=+1
print(score)

print("Your Score is " + str(score))



# TO increase efficiency without type conversion use print(f{})

print(f"Your Score Is {score}")