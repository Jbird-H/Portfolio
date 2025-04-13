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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
adventure_begins = input("You find yourself standing before a fork in the road, do you go left or right?\n")
if adventure_begins == "left" or adventure_begins == "Left":
    print('''     .-.                                    ,-.
  .-(   )-.                              ,-(   )-.
 (     __) )-.                        ,-(_      __)
  `-(       __)                      (_    )  __)-'
    `(____)-',                        `-(____)-'
  - -  :   :  - -
      / `-' 
    ,    |   .
         .                         _
                                  >')
               _   /              (\         (W)
              =') //               = \     -. `|'
               ))////)             = ,-      \(| ,-
              ( (///))           ( |/  _______\|/____
~~~~~~~~~~~~~~~`~~~~'~~~~~~~~~~~~~\|,-'::::::::::::::
            _                 ,----':::::::::::::::::
         {><_'c   _      _.--':MJP:::::::::::::::::::
__,'`----._,-. {><_'c  _-':::::::::::::::::::::::::::
:.:.:.:.:.:.:.\_    ,-'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:
.:.:.:.:.:.:.:.:`--'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.
.....................................................''')

else:
    print("You are attacked by a herd of rabid squirrels")
    print('''                   ______
                    .-"      "-.
                   /            
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/   jgs                              \_) ''')
    print("G A M E  O V E R")
    raise SystemExit
lake_choice = input("You wander down a tree covered lane reaching a small lake, do you swim across or wait for a boat?\n")
if lake_choice == "swim" or lake_choice == "swim across":
    print("You are instantly entangled in the lake grass and cannot get free.")
    print('''                   ______
                        .-"      "-.
                       /            
           _          |              |          _
          ( \         |,  .-.  .-.  ,|         / )
           > "=._     | )(__/  \__)( |     _.=" <
          (_/"=._"=._ |/     /\     \| _.="_.="\_)
                 "=._ (_     ^^     _)"_.="
                     "=\__|IIIIII|__/="
                    _.="| \IIIIII/ |"=._
          _     _.="_.="\          /"=._"=._     _
         ( \_.="_.="     `--------`     "=._"=._/ )
          > _.="                            "=._ <
         (_/   jgs                              \_) ''')
    print("G A M E  O V E R")
    raise SystemExit
else:
    print("You wait for what seems like forever until and old man with a boat arrives and invites you on board.")
    print("He takes you across the lake to a small island that has three fishing huts and not much else on it")
    print('''     _
        _|=|__________
       /              |
      /                |
     /__________________|
      ||  || /--\ ||  ||
      ||[]|| | .| ||[]||
    ()||__||_|__|_||__||()
   ( )|-|-|-|====|-|-|-|( )
jgs^^^^^^^^^^====^^^^^^^^^^^''')
    print("He urges you to choose one of the three huts to spend the night in")
fishing_hut_choice = input("Do you choose the blue, green or red roofed fishing hut?\n")
if fishing_hut_choice == "red" or fishing_hut_choice == "Red" or fishing_hut_choice == "red hut":
    print ("As you open the door you fail to notice the trip wire, setting off a large explosion")
    print('''                   ______
                           .-"      "-.
                          /            
              _          |              |          _
             ( \         |,  .-.  .-.  ,|         / )
              > "=._     | )(__/  \__)( |     _.=" <
             (_/"=._"=._ |/     /\     \| _.="_.="\_)
                    "=._ (_     ^^     _)"_.="
                        "=\__|IIIIII|__/="
                       _.="| \IIIIII/ |"=._
             _     _.="_.="\          /"=._"=._     _
            ( \_.="_.="     `--------`     "=._"=._/ )
             > _.="                            "=._ <
            (_/   jgs                              \_) ''')
    print("G A M E  O V E R")
    raise SystemExit
elif fishing_hut_choice == "blue" or fishing_hut_choice == "Blue" or fishing_hut_choice == "blue hut":
    print("You fail to notice that the floor is missing, dropping into a deep cenote you are unable to get out")
    print('''                   ______
                           .-"      "-.
                          /            
              _          |              |          _
             ( \         |,  .-.  .-.  ,|         / )
              > "=._     | )(__/  \__)( |     _.=" <
             (_/"=._"=._ |/     /\     \| _.="_.="\_)
                    "=._ (_     ^^     _)"_.="
                        "=\__|IIIIII|__/="
                       _.="| \IIIIII/ |"=._
             _     _.="_.="\          /"=._"=._     _
            ( \_.="_.="     `--------`     "=._"=._/ )
             > _.="                            "=._ <
            (_/   jgs                              \_) ''')
    print("G A M E  O V E R")
    raise SystemExit
elif fishing_hut_choice == "green" or fishing_hut_choice == "Green" or fishing_hut_choice == "green hut":
    print("You chose")
    print("...")
    print("wisely")
    print('''    __________
        /\____;;___|
       | /         /
       `. ())oo() .
        |\(%()*^^()^
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________| ''')
    print("You Win!!!")
else:
    print ("Your choices are suspect, so you are struck by lightning by the game gods")
    print('''                   ______
                           .-"      "-.
                          /            
              _          |              |          _
             ( \         |,  .-.  .-.  ,|         / )
              > "=._     | )(__/  \__)( |     _.=" <
             (_/"=._"=._ |/     /\     \| _.="_.="\_)
                    "=._ (_     ^^     _)"_.="
                        "=\__|IIIIII|__/="
                       _.="| \IIIIII/ |"=._
             _     _.="_.="\          /"=._"=._     _
            ( \_.="_.="     `--------`     "=._"=._/ )
             > _.="                            "=._ <
            (_/   jgs                              \_) ''')
    print("G A M E  O V E R")
    raise SystemExit
