print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the DAY 3 Life Island.")
print("Your mission is to find the treasure.")
people = input("Would you like to go ALONE or with a PARTY?")
if people == "alone" or people == "Alone" or people == "ALONE":
    print("You got lost on the trail without someone to help you navigate")
elif people == "party" or people == "Party" or people == "PARTY":
    print("You made it to a river\n")
    river_decision = input("should you WAIT or try to BUILD a raft")
    if river_decision == "build" or river_decision == "Build" or river_decision == "BUILD":
        print("You made it across in one piece after many failed raft attempts\nYou approach a sign post pointing in three directions")
        direction = input("Do you follow the DISC path, the IDLE path, or the REGRE path")
        if direction == "disc" or direction == "Disc" or direction == "DISC":
            print("Congratulations, you made the correct choices on your life island and have earned the treasure!")
        elif direction == "idle" or direction == "Idle" or direction == "IDLE":
            print("You ventured onto the wrong road, one that keeps looping in on itself. You and your party become trapped forever")
        elif direction == "regre" or direction == "Regre" or direction == "REGRE":
            print("You ventured onto the path that you didn't truly think was right for you, and you ended up having to go home after finding no treasure")
        else:
            print("Invalid Option")
    elif river_decision == "wait" or river_decision == "Wait" or river_decision == "WAIT":
        print("Nobody came, you and your party starved")
    else:
        print("Invalid Option")
else:
    print("Invalid Option")