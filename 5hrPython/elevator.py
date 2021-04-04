#practice python    
# elevator 

request = input("Elevator is moving, type 'out' to exit elevator, or floor # desired (1-10)")

while int(request) in range(1,11,1):
    print(f"You are on floor {request}")
    floor = request
    request = '100'
    while (int(request) not in range(1,11,1)):
        request = input("Elevator is moving, type 'out' to exit elevator, or floor # desired (1-10)")
        if request == 'out':
            break
    if request == 'out':
        break
    
print(f"Floor number {floor}, Doors opening... Have a nice day")
