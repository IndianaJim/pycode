import random

a = 5 > 4
b = 'John' != 'john'
print(a)
print(b)

grade_john = 70
if grade_john > 70:
    print("Congrats! you've passed")
else:
    print("sorry you have not passed")
print("good luck in the next exam")

student_name = "john michael"
is_snowing = False
is_raining = True
is_badweather = is_snowing or is_raining
# and
# or
# not
print(is_badweather)

if is_snowing:
    print(f"""
    Hi {student_name.title()},
    Since it is snowing today,
    school is cancelled.
    """)
elif is_raining:
    print(f"""
    Hi {student_name.title()},
    Since it is only raining today,
    school is open.
    """)
else:
    print(f"""
    Hi {student_name.title()},
    Since it is not snowing today,
    school is open.
    """)

person1 = "Allen"
person2 = "Michael"
person3 = "John"
person4 = "Ben"

people = ["Allen", "Michael","John", "Ben"]
print(people)
print(people[0])
print(people[len(people) - 1])
print(people[-1])
print(people[1:3]) # pulls 1 and 2, ignores 3
print(people[1:]) # pulls from 1 forward
print(people[:2]) # pulls first 2 only
# people.append("Jim")
# people.remove("Allen") 
# people.pop(0) #remove item 0
# people.sort() # default is alphanumeric

print(people)
#myRandNum = random.randint(0,(len(people) - 1))
#print(myRandNum)
chosenperson = random.choice(people)
print(f"chosen: {chosenperson}")
#people.append("Jim")
print(people)
#print(f"{people[myRandNum]} will be removed.")
#people.pop(myRandNum)
people.remove(chosenperson)
print(people)
