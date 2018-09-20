from rooms import rooms

current = "hall"

while True:
    print(rooms[current]["desc"])
    cmd = input("> ").strip().lower()
    if cmd == "quit":
        break
    if cmd in rooms[current]["exits"]:
        current = rooms[current]["exits"][cmd]
    else:
        print("You can't go that way.")
