print("You see a door with a red light coming from behind it.")
print("Do you go through? YES or NO")

do = input(":: ")
if do == "YES":                                                  
    print("You see an immense pit after opening the door and looking in!")
    print("Do you JUMP in or WALK away?")

    do = input(":: ")
    if do == "WALK":                                          
        print("You immediatly leave, not looking back.")
        print("END")
    
    if do == "JUMP":                                            
        print("Are you sure? You can't even see the bottom! JUMP or LEAVE")

        do = input(":: ")
        if do == "JUMP":                                           
            print("You jump in, falling for what feels like forever. Eventually you hit the bottom seeing that you are in Hell!")
            print("Seeing this you have a choice to make. Try to ESCAPE or STAY?")

            do = input(":: ")
            if do == "ESCAPE":                                      
                print("Good choice considering this is literal Hell.")
                print("You see two possible ways to go, how do you want to try to escape? STAIRS or HIGHWAY")

                do = input(":: ")
                if do == "STAIRS":                                   
                    print("Good. The stairs lead up into heaven!")
                    print("You have a huge frat party and party for eternity!")
                    print("END")

                if do == "HIGHWAY":                                  
                    print("Bad choice!")
                    print("Everyone knows that the highway leads further into Hell! Stupid.")
                    print("But you can try and go fight demons and the Devil Himself!")
                    print("Do you try to FIGHT or ACCEPT your fate?")
                        
                    do = input(":: ")
                    if do == "FIGHT":
                        print("Hell yeah! You travel to a nearby guard station.")
                        print("Do you FIGHT them or ASK them for info?")

                        do = input(":: ")
                        if do == "ASK":
                            print("You ask the guards for directions to the Devil, saying you wish to speak with him.")
                            print("They say that you need to make two LEFT turns and then a RIGHT.")
                            print("Which way do you turn? LEFT or RIGHT?")
                            
                            do = input(":: ")
                            if do == "LEFT":
                                print("On the right track!")
                                print("Now do you turn LEFT or RIGHT?")
                            
                                do = input(":: ")
                                if do == "LEFT":
                                    print("Still on the right track!")
                                    print("Do you turn LEFT or RIGHT?")

                                    do = input(":: ")
                                    if do == "RIGHT":
                                        print("You end up in the Devil's office!")
                                        print("Do you want to TALK to him or ATTACK him?")

                                        do = input(":: ")
                                        if do == "TALK":
                                            print("You speak up and the Devil sees you. He burns you to a crisp.")
                                            print("END")
                                        
                                        if do == "ATTACK":
                                            print("You sneak up behind him and hit him over the head with a rock. He keels over dead on the floor. You see a exit to the surface after you beat him.")
                                            print("You leave and go home hoping to forget everything thats just happened.")
                                            print("END")
                                    
                                    if do == "LEFT":
                                        print("You just did a big circle stupid!")
                                        print("You stay in Hell forever because you can't follow simple directions.")
                                        print("END")

                                if do == "RIGHT":
                                    print("You have found a voidwalker who traps you in it's abyss forever.")
                                    print("END")    

                            if do == "RIGHT":
                                print("You have made a wrong turn and find a pit fiend that stabs you as soon as it sees you.")
                                print("END")

                        if do == "FIGHT":
                            print("The guards beat you senseless and take you to a cell, where you rot away for the rest of eternity!")
                            print("END")
                    if do == "ACCEPT":
                        print("You continue down the highway until you reach your designated circle of Hell.")
                        print("END")

            if do == "STAY":
                print("Ok you pyschopath stay in Hell if you want to!")
                print("END")

        if do == "LEAVE":                                          
            print("Okay wuss.")
            print("END")

if do == "NO":                                               
    print("You decide that's probably a bad idea.")
    print("You go home for the night leaving the door behind.")
    print("You do not know what was behind the door, but it's probably best you don't ever find out.")
    print("END")