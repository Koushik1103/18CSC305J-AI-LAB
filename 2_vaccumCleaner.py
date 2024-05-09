def GoForward(rooms, pos):
    while pos != len(rooms):
        if rooms[pos] == False:
            rooms[pos] = True
            print("Room {} is dirty, Clean and moving forward".format(pos+1))
            pos += 1
        else:
            print("Room {} is clean, moving forward".format(pos+1))
            pos += 1
        print("Reached the End, so turning back")


def GoBackward(rooms, pos):
    while pos >= 0:
        if rooms[pos] == False:
            rooms[pos] = True
            print("Room {} is dirty, Clean and moving back".format(pos+1))
            pos -= 1
        else:
            print("Room {} is clean, moving back".format(pos+1))
            pos -= 1
        print("Reached the start, so turning back")


n = int(input("Enter Number of Rooms: "))
rooms = []
for i in range(n):
    x = int(input("Enter 1 for Clean and 0 for dirty for room {} : ".format(i+1)))
    if x == 1:
        rooms.append(True)
    else:
        rooms.append(False)
pos = int(input("Enter Initial position of the vacuum cleaner (1-{})".format(n)))
pos -= 1
while rooms != [True for i in range(n)]:
    GoForward(rooms, pos)
    GoBackward(rooms, pos)
print("All Rooms are cleaned")
