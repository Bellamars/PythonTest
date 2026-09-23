#Definite= We know how many times we want it to run 
#Indefinite = We don't know how manny times it will run 

for i in range (100,110,2):
    print (i)  

age = int(input("How old are you?"))

while age < 0:
    print("You can't be negative years old") 
    age = int(input("How old are you?"))

    if(age== -16):
        break 

#Day 1, Appointment 1
#Day 2, Appointment 2
#...
#Day 1, Appointment 5 
#Day 2, Appointment 1 
#...
#Day 3, Appointment 5

for i in range(1,4):
    for j in range (1,6):
        print(f"Day {i}, Appointment {j}")
