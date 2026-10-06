#Section 1: Variables and Types::

Name = "Swathi"
Age = 32
Height = 5.1
Are_you_Under_40 = True


print("enter a Name", type(Name ))
print("Enter an Age", type(Age))
print("Enter a Height", type(Height))
print("True", type(Are_you_Under_40))

Name = input("what is your Name" )
print("welcome to Code the Dream", Name)

#Section 2: User Input and Math::

name=str(input("Please enter your name: "))
bornyear=int(input("Please enter your born year : "))
age= 2026-bornyear
print(f" Hi, {name}! You are approximately {age} years old")

#Section 3: Type Conversion and f-strings::
#16.6 × 4.6 = 30.02
#float
a = float(input("Enter a first number"))
b = float(input("Enter a second number"))
c = (a*b)
print(f"first number is {a} and second number is {b} Multiplication {c}")

#Section 4: Formatted Receipt::

a = "Science Book"
b = 45.45
c = 5
d = b*c

print("===========================")
print("         RECEIPT         ")
print("===========================")
print("Item:     " + str(a))
print("Price:    $" + str(float(b)))
print("Quantity:  " + str(int(c)))
print("---------------------------")
print("Total:    "+ str(float(d)))
print("===========================")


#Mini-Project — Profile Card

profile = str(input("Enter profile name: "))
hometown = str(input("Enter a hometown: "))
favoritehobby =str(input("Enter a favoritehobby: "))
funfact = str(input("Enter a funfact: "))
bornyear = int(input("Enter a bornyear: "))
currentyear =2026
age = currentyear-bornyear

print("╔══════════════════════════════╗")
print(f"PROFILE:        {profile} ")
print("╚══════════════════════════════╝")
print(f"Hometown:       {hometown}")
print(f"Favoritehobby:  {favoritehobby}")
print(f"Fun fact:       {funfact}")
print(f"Age:            {age}")
