# list = []
# tuple = () are static, cannot remove or append
import random
people = ['allen','ben']
people.remove("allen")
print(people)

days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
days[2]
print(days[2])

friend = {
    "name":"Jim",
    "age":25,
    "gender":"male",
    "weight":175
}

print(friend)
print(friend["name"])
print(friend.get("name"))



