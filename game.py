#defining variables
room = "beginning"
loop_room = True
loop = 1
keys = 0
w_complete = False
n_complete = False
e_complete = False
choose = 0
arm_lost = False

#story begins
print("You find yourself in an unfamiliar environment.")
print("You are surrounded by trees, the forest greenery enveloping you.")
print("You seem to have forgotten your name.")
print("")
name = input("What would you like to call yourself? ")
print("Alright, " + name + ", try to have fun.")
print("")
print("To the west, there is a mysterious temple.")
print("To the east, there seems to be a small lake.")
print("To the north, there is a clearing.")
print("And to the south, there is simply a door.")

#gameplay loop
while loop == 1:
    print("")
    print("You find yourself in the beginning, where you started.")
    direction = input("Type w for temple, e for lake, n for clearing, or s for door. ")
    direction = direction.lower()
    while room == "beginning":
        if direction == "w":
            if w_complete == False:
                room = "temple"
            else:
                print("You have already been to the temple.")
                input("Type anything to choose a different direction.")
                break
                                
        elif direction == "e":
            if e_complete == False:
                room = "lake"
            else:
                print("You have already visited the lake.")
                input("Type anything to go back and choose a different direction.")
                break
                        
        elif direction == "n":
            room = "clearing"
                            
        elif direction == "s":
             room = "door"
                        
        else:
            print("Try again.")
            direction = input("Type in a direction this time.")
            
    while room != "beginning":
        if room == "temple":
            print("You find yourself inside a massive structure, although it is much more claustrophobic than you expected.")
            choose = input("Type 1 to continue, 2 to return. ")
            if choose == "1":
                choose = 0
                print("You continue.")
                print("There seems to be a door that has a glowing hand print on it.")
                print("You put your hand onto the print and the door grinds open.")
                input("Type anything to continue.")
                print("[WORLDBUILD AND STUFF STARTS TO FALL DOWN]")
                print("You happen to see a black cat that is about to be crushed by some stone.")
                choose = input("1 to save the cat, 2 to run back with the rock.")
                if choose == "1":
                    print("You saved the cat and ran back to the beginning with the glowing stone.")
                    print("However, your arm was lost to the rock in the process.")
                    keys += 1
                    room = "beginning"
                    arm_lost = True
                    w_complete = True
                    break
                elif choose == "2":
                    print("You run back to the beginning, and make it safely with the glowing piece of rock.")
                    print("However, your consience will always be scarred.")
                    keys += 1
                    arm_lost = False
                    room = "beginning"
                    w_complete = True
                    break
            elif choose == "2":
                print("You go back.")
                room = "beginning"
                break
            else:
                choose = input("Choose again. ")
        elif room == "lake":
            print("You go to the lake.")
            print("[WORLDBUILDING]")
            input("Type 1 to grab the crystal. ")
            keys += 1
            e_complete = True
            room = "beginning"
            break
        elif room == "clearing":
            if n_complete == True:
                print("You have already been to the clearing.")
                input("Type anything to go back to the beginning.")
                room = "beginning"
                break
            print("You go to the clearing.")
            print("[WORLDBUILDING]")
            input("1 to grab the crystal")
            keys += 1
            room = "beginning"
            n_complete = True
            break
        elif room == "door":
            if keys <= 2:
                print("")
                print("The door is a simple wooden door, the word '" + name + "' engraved at the top.")
                print("You notice that there are three faintly glowing indentations.")
                print("You try to rattle the handle of the door, but it is unyielding.")
                print("")
                input("Type 1 to go back. ")
                room = "beginning"
                break
            else:
                print("")
                print("You walk up to the door.")
                input("Type 1 to put the glowing rocks in the indentations. ")
                print("You put the rocks in their respective indentations.")
                choose = input("Open the door? (y/n) ")
                choose = choose.lower
                loop = 0
                print("Your choices never mattered anyway, " + name + ".")
                print(name + " swings the door open and leaves me here.")
                break
        else:
            print("Dang i messed something up!")
            room = "beginning"
            break
#end code
print("")
print("This is the end.")
print("I try to grab your arm to make you come back, but it is no use.")
print("Goodbye, " + name + ".")
print("")
if arm_lost == False:
    print("Thanks for playing!")
else:
    print("Thanks for playing!")
    print("Enjoy your lost arm!")
    