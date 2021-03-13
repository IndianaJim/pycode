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


