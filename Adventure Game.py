print('''
          _______  _        _______  _______  _______  _______   _________ _______   _________          _______        
|\     /|(  ____ \( \      (  ____ \(  ___  )(       )(  ____ \  \__   __/(  ___  )  \__   __/|\     /|(  ____ \       
| )   ( || (    \/| (      | (    \/| (   ) || () () || (    \/     ) (   | (   ) |     ) (   | )   ( || (    \/       
| | _ | || (__    | |      | |      | |   | || || || || (__         | |   | |   | |     | |   | (___) || (__           
| |( )| ||  __)   | |      | |      | |   | || |(_)| ||  __)        | |   | |   | |     | |   |  ___  ||  __)          
| || || || (      | |      | |      | |   | || |   | || (           | |   | |   | |     | |   | (   ) || (             
| () () || (____/\| (____/\| (____/\| (___) || )   ( || (____/\     | |   | (___) |     | |   | )   ( || (____/\       
(_______)(_______/(_______/(_______/(_______)|/     \|(_______/     )_(   (_______)     )_(   |/     \|(_______/       
                                                                                                                       
 _______  ______            _______  _       _________          _______  _______    _______  _______  _______  _______ 
(  ___  )(  __  \ |\     /|(  ____ \( (    /|\__   __/|\     /|(  ____ )(  ____ \  (  ____ \(  ___  )(       )(  ____ \
| (   ) || (  \  )| )   ( || (    \/|  \  ( |   ) (   | )   ( || (    )|| (    \/  | (    \/| (   ) || () () || (    \/
| (___) || |   ) || |   | || (__    |   \ | |   | |   | |   | || (____)|| (__      | |      | (___) || || || || (__    
|  ___  || |   | |( (   ) )|  __)   | (\ \) |   | |   | |   | ||     __)|  __)     | | ____ |  ___  || |(_)| ||  __)   
| (   ) || |   ) | \ \_/ / | (      | | \   |   | |   | |   | || (\ (   | (        | | \_  )| (   ) || |   | || (      
| )   ( || (__/  )  \   /  | (____/\| )  \  |   | |   | (___) || ) \ \__| (____/\  | (___) || )   ( || )   ( || (____/\
|/     \|(______/    \_/   (_______/|/    )_)   )_(   (_______)|/   \__/(_______/  (_______)|/     \||/     \|(_______/
                                                                                                                       
''')



first_choice = input("You wake up in an unfimiliar place, unsure of how you got there. "
"As you look around you notice that you are in a clearing with paths "
"going 'North', 'South' and 'East'. Which direction do you go?\n").lower()

if first_choice == "north":
    second_choice = input("You see that the northern path looks overgrown and seldom walked on so you very cautiously "
                            "proceed along the path. After walking for what seems like hours you reach what appears to be "
                            "a small river. Do you jump in and 'Swim' across, or do you try to find a shallow spot and 'Walk'?\n").lower()
    if second_choice == "swim":
        print("The river was shallow, you should have checked first. You have sprained your ankle and must go home.")
        print("GAME OVER")
    elif second_choice == "walk":
        third_choice = input("Crossing the shallow river easily, you wonder why you even considered swiming. Oh well, on you go. "
                             "On the other side of the river you see before you a dark path leading up to a cave on the hill side."
                             "Do you 'enter' the cave, or do you 'look around' first?\n").lower()
        if third_choice == "look around" or third_choice == "look":
            print("While caution is important, this time that moment of hesitation cost you. You are struck by a bolt of lightening.")
            print("GAME OVER")    
        elif third_choice == "enter":
            fourth_choice = input("Rain begins falling the moment you step into the cave, good thing you didn't dillydally outside "
                                  "or you would be soaked. You glance around the cave and see that it appears someone else has been here "
                                  "before you. Their possesions are scattered about, including what looks to be a large treasure chest. "
                                  "Do you 'open' the chest, or do you simply 'sit' down and warm yourself by the fire?").lower()
            if fourth_choice == "sit" or fourth_choice == "sit down":
                print("'What a good kid you are' booms a voice from behind you. You look up as a giant enters the cave and makes herself at home. "
                      "'it's cold out there, so I'm glad you started the fire,' she continues. 'We've had a real theft problem recently and my temper "
                      "has been on edge, so this is nice.' 'For such a good kid as you, I have a reward.'\n"
                      "The giant hands you her golden toothpick. It may not look like much but it's so heavy you can barely lift it. You are set for life!")
                print("You Win!!!!")
            elif fourth_choice == "open":
                print("'THIEF' you hear someone scream, followed by a bonecrushing pain and nothing more.")
                print("GAME OVER")
            else:
                print("And you were doing so good too. Well, time to start over")
                print("GAME OVER")
        else:
            print("It appears too many choices has driven you mad to make a choice like that, sadly we don't offer compensation for mental damages.")
            print("GAME OVER")
    else:
        print("The options before you were too confusing, but the fickle minded programer doesn't care about your struggles.")
        print("GAME OVER")
        
elif first_choice == "south":
    print("You see a well trodden path heading downhill. As you walk for about an hour it comes to a bustling village. "
        "You have reached safety and the end of your adventure.")
    print("GAME OVER")
elif first_choice == "east":
    print("You head in the direction of the rising sun, but alas with the sun in your eyes you don't notice the path end. "
          "You continue on, but the path does not. You have reached the bottom of a cliff, quickly.")
    print("GAME OVER")
else:
    print("Your answer is invalid, confusing the narrator so much he rage quit")
    print("GAME OVER")



