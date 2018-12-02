from rooms import rooms

HELP = """Commands:
  go <direction>   move around
  take <item>      pick something up
  inventory        show what you carry
  eat <item>       eat something
  look             describe the room again
  quit             give up
"""


def describe(room, inventory):
    if room.get("dark") and "lamp" not in inventory:
        print("It is too dark to see anything.")
        return
    print(room["desc"])
    if room["items"]:
        print("You see: " + ", ".join(room["items"]))


def main():
    current = "hall"
    inventory = []
    print("Welcome! Type 'help' for a list of commands.")
    describe(rooms[current], inventory)

    while True:
        words = input("> ").strip().lower().split()
        if not words:
            continue
        verb = words[0]
        noun = words[1] if len(words) > 1 else ""

        if verb == "quit":
            print("Bye!")
            break
        elif verb == "help":
            print(HELP)
        elif verb == "look":
            describe(rooms[current], inventory)
        elif verb == "eat":
            if noun in inventory:
                inventory.remove(noun)
                print("Yum. You feel stronger.")
            else:
                print("You don't have " + noun + ".")
        elif verb == "inventory":
            print("You carry: " + (", ".join(inventory) or "nothing"))
        elif verb == "take":
            if noun in rooms[current]["items"]:
                rooms[current]["items"].remove(noun)
                inventory.append(noun)
                print("Taken: " + noun)
            else:
                print("There is no " + noun + " here.")
        elif verb == "go":
            exits = rooms[current]["exits"]
            if noun not in exits:
                print("You can't go that way.")
                continue
            target = rooms[exits[noun]]
            if target.get("locked"):
                if "key" in inventory:
                    print("You unlock the door with the key and escape. You win!")
                    break
                print("The door is locked.")
                continue
            current = exits[noun]
            describe(rooms[current], inventory)
        else:
            print("I don't understand that.")


if __name__ == "__main__":
    main()
