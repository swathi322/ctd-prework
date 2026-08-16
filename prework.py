#Buying 2BHK House within Budget 1500000 to 2500000

structure = str(input("House structure 1BHK/2BHK/3BHK/4BHK : "))
Budget = int(input("House Budget: "))

if structure == "2BHK" and (1500000 <= Budget <=2500000):
 print("Good Selection Happy to Buy home "+ structure + " within " + str(Budget))
 #   print: ("  2500000 you are able to buy a home" + structure)
else:
 print("Enter correct House structure within Budget")
  
