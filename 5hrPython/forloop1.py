friends = ["Allen", "Ben", "John"]

for friend in friends:
    print(f"{friend} is my friend")

best_friend = "Jim"
count = 0

for friend in friends:
    count = count + 1
    if friend == best_friend:
        print(f"best friend {friend} is in the list")
    elif count == len(friends):
        print(f"best friend {best_friend} is NOT in the list.")

