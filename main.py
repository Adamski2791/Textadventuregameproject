# FIX!!! After answering the questions in the quiz. I get sent back to the same place again that I entered the
# quiz_room. Fix!!!! Added coded in main(), and create a function to ask for your name and return it.
# secret_corridor if cork variable not working for leak.
# ad

import time

treasure_chest = ["diamonds", "gold", "crown", "sword", "cork", "chalice"]
backpack = []
queens_hand = ["key"]


# ACTIONS #
def you_died(why):
    """
    In: Passing in the string, showing player how they dies

    Result:
    Print's reason why the player died.
    Programme exits without error.
    """
    print("{}. That's a pity! You died!".format(why))

    # This exits the program entirely.
    exit(0)


def sail_home():
    """
    This is where you get your happy ending
    """
    print("""You are exhausted and your little boat exits the cave into a bright and sunny day.
            You think about you adventure, as the boat floats peacefully down the river and
            wonder when you next adventure might be? Sleep comes easily and you dream of
            monsters, treasure and magical places.""")
    exit(0)


def open_lock():
    """
    You free the dragon, who eats kali. You win.
    """
    print("""
    The lock opens and you look up. 
    You heart skips a beat as you see the monstrous figure of Kali approach. 
    He has his two bladed axe held high in the air. 
    You grab your shiny sword and face him, while still holding the dragon scale in your other hand. 
    Kali swings his axe and you attempt a parry. 
    His axe cuts through your blade like butter. You feel like this will be your last breath. 
    The large chain holding the dragon, slips across the floor. 
    Kali's foot gets caught in link and the dragon is upon him. 
    The great dragon tosses Kali back and forth, like a dog with a toy. 
    It then chews and you hear the armour and bones pop and crunch. 
    Kali is no more!
    You run from the room while the dragon is busy with his meal.
    """)
    time.sleep(10)
    you_win()


def you_win():
    """
    You have defeated Kali. The queen is grateful. You win.
    """
    print(""" 
    You make your way back to the Queen's chamber.
    You tell the queen about your adventure and she is most grateful. 
    She is as good as her word and she rewards you with treasure 
    and offers you lands and the title of defender of the realm.
    You accept these great honours and live an honoured life. 
    From humble beginnings there is nothing more
    that you could have wished for.You are the winner in this adventure.
    """)
    time.sleep(10)
    print("""
    The years pass by and the land enjoys it's longest peace in decades.
    You have been happy and wealthy, but as when you dream, you still dream of adventure.
    A scroll gets delivered by messenger from the Queen. 
    You read it and it tells of a darkness that is enveloping kingdoms to the south. 
    The Queen calls you her light and maybe you can defeat the darkness one more time?
    In the dark the light shines brightly. Are you willing to risk all that you have gained for adventure?
    
    >>>The End...of this chapter.
    """)
    exit(0)


# END ACTIONS #

# CHARACTERS #


def guard():
    """
    Encountering the guard, the player chooses to attack, check or sneak.
    - attack: player dies, and it is game over
    - check: sees what the guard is doing, but nothing else happens, and get 3 options again
    - sneak: player sneaks past the guard and wins the game
    """
    # Actions of the guard
    actions_dict = {
        "check": "You see the guard is still sleeping, you need to get to that door on the right of him. What are you "
                 "waiting for?",
        "sneak": "You approach the guard, he's still sleeping. Reaching for the door, you open it slowly and slip out.",
        "attack": "You swiftly run towards the sleeping guard and knock him out with the hilt of your shiny sword.\n"
                  "Unfortunately, it wasn't hard enough."}

    # While loop
    while True:
        action = input("What do you do? [attack | check | sneak] >").lower()
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "sneak":
                print("""
                You just slipped through the door before the guard realised it.\n
                You have entered a new room.\n
                """)
                print("""
                You enter a room, and you see a red door to your left and a blue door to your right.
                Or take the corridor.
                """)
                door_picked = input("Do you pick the red, blue or corridor? > ")

                # Pick a door, and we go to a room and something else happens
                if door_picked == "red":
                    red_door_room()
                elif door_picked == "blue":
                    blue_door_room()
                elif door_picked == "corridor":
                    secret_corridor()
                else:
                    print("""
                    Sorry, it's either 'red', 'blue' or 'corridor'
                    as the answer. You're the weakest link, goodbye!
                    """)
                    exit(0)
            elif action == "attack":
                you_died("""
                    The guard woke with a grunt, and reached for his dagger, and before you know it, 
                    the world goes dark and you just died. \n<GAME OVER>
                    """)


def dragon():
    """
    Encountering the dragon, the player chooses to attack, talk or sneak.
    - attack: player dies, and it is game over
    - talk: asks the dragon a question
    - sneak: player sneaks past the dragon and finds a passage
    """
    # Actions on the dragon
    dragon_actions_dict = {
        "talk": "You ask the dragon for directions. What's the worst that could happen?",
        "creep": "You approach the dragon on tip toes, he's watching but can't see you."
                 "Reaching for the door, you open it slowly and slip out.",
        "attack": "You swiftly run towards the dragon, waving your shiny sword. A blast of fire consumes you. "
                  "You are now a crispy critter."}

    # While loop
    while True:
        action = input("What do you do? [attack | creep | talk] >").lower()
        if action in dragon_actions_dict.keys():
            print(dragon_actions_dict[action])
            if action == "creep":
                print("""
                You just slipped through the door before the dragon realised it.\n
                You are now outside the dragon's lair.\n
                    """)
                return
            elif action == "attack":
                you_died("""
                    The dragon was too fast, and you got flamed grilled like a whopper
                    and you died. \n<GAME OVER>""")


def queen():
    """
    Encountering the queen, the player chooses to attack, check or sneak.
    - attack: player dies, and it is game over
    - check: sees what the guard is doing, but nothing else happens, and get 3 options again
    - sneak: player sneaks past the guard and wins the game
    """
    # Actions of the guard
    queen_actions_dict = {
        "talk": """
        You clear your throat and the queen turns around. She is beautiful.
        """,
        "sneak": "You turn away quietly. Reaching for the door and slip out.",
        "attack": "You swiftly run towards the queen and aim a blow with your shiny sword. "
                  "You don't see the guard, and he cuts you down, as you enter the room."}

    # While loop
    while True:
        action = input("What do you do? [attack | talk | sneak] >").lower()
        if action in queen_actions_dict.keys():
            print(queen_actions_dict[action])
            if action == "sneak":
                print("""
                You just slipped through the door before the queen realised it.\n
                You are back in the corridor
                """)
                secret_corridor()
            elif action == "talk":
                print("""
                You say, 'Hello.' and she looks at you, with a sorrowful expression.
                She is crying. You ask her how you can help.
                She says she is the Queen, but her crown has been stolen.
                She has been imprisoned here by an evil usurper calling himself the Dragon Master.
                He has taken her throne, along with her crown.
                Her people are being held in slavery.
                She can only take her throne again when she has her crown. 
                She asks, can you help her?
                You can't pass by a damsel in distress, so you say that you will help.
                """)
                time.sleep(10)

                if 'crown' in backpack:
                    print("""
                    Maybe I can help. Let me check in my backpack! 'I'm an adventurer and have 
                    discovered some glorious treasure today. One item was a crown, if it is yours you are welcome to 
                    have it. You pull the crown from your backpack and hand it to the queen.
                    The Queen is delighted. She places the crown on her head and is transformed.
                    She radiates elegance and glows with a power.
                    An aurora like light shimmers around her body.
                    She is the most beautiful person that you have ever seen.
                    """)
                    time.sleep(10)
                    print("""
                    When she speaks again her voice is like honey.
                    I will be forever grateful to you for what you have done for me.
                    I have a gift that will aid your quest and help both you and I.'
                    She hands you a key. It is long and the shaft is decorated with a dragon.
                    """)
                    time.sleep(10)
                    print("""
                    She says, 'Kali the Dragon master was able to take my kingdom, because he
                    imprisoned a mighty dragon. The dragon in chained in the Red room, and guards
                    a vast treasure. If you can release the dragon, the dragon master's reign 
                    will be ended. If you do this for me. I will make you richer than
                    you could ever imagine.You take the key and say, 
                    I would be happy to help in any way that I can.
                    """)
                    backpack.remove("crown")
                    queens_hand.append("crown")
                    queens_hand.remove("key")
                    backpack.append("key")
                    time.sleep(10)
                    print(f"""
                    You have placed {'key'} in your backpack and exit the chamber.
                    """)
                    dragons_lair()

                if 'crown' not in backpack:
                    print("""
                    I am but a humble man, but I will try to help in any way that I can. 
                    I will search for the crown and 
                    I will do all that I can to free you from your imprisonment.
                    You turn and leave the room with a new purpose. You return to the corridor.
                    """)
                    secret_corridor()


            elif action == "attack":
                you_died("""
                The guard was faster than anyone you had ever seen before, and his blade was true!
                Your head was separated from your shoulders, and you died. \n<GAME OVER>
                """)


def quiz_master():
    """
    Encountering the quiz_master, the player chooses to attack, answer or leave.
    - attack: player dies, and it is game over.
    - answer: answer the questions and hopefully continue the quest.
    - leave: player turns around and goes the way he came.
    """
    quiz_master_actions_dict = {
        "attack": """
        You swing your sword, like a flash. It's slices through the air and then into the ragged man.
        The old man is faster still, and he sinks his sharp teeth into your neck.
        He severs an artery, and you bleed out quickly, as he drinks your blood!
        """,
        "answer": "You decide to take the old man's quiz.",
        "leave": "You turn away. Reach for the door and head back the way you came, feeling like a coward.",
    }
    # While loop
    while True:
        action = input("What do you do? [attack | answer | leave] >").lower()
        if action in quiz_master_actions_dict.keys():
            print(quiz_master_actions_dict[action])
            if action == "leave":
                print("""
                You turn tail. There is something evil in this room, and your skin crawls.
                You can't leave quick enough, and you feel that you have saved your skin. \n
                """)
                red_door_room()
            elif action == "answer":
                print("""
                You are wary of the man, but you are smart and like a gamble.
                You say, 'Ask your questions demon. You do not scare me!
                """)
                quiz()
            elif action == "attack":
                print(you_died("""                    
                The man was lightening quick!
                His razor sharp teeth were in your neck before you could blink.
                You feel the life seeping from your body. \n<GAME OVER.
                """))


# END CHARACTERS #


# ROOMS #
def blue_door_room():
    """
    The player finds a treasure chest, options to investigate the treasure chest or guard.

    If player chooses
    - Treasure chest: show its contents; option to take treasure or ignore it (proceeds to guard)
    - Guard: After checking treasure chest, ignoring treasure chest to check guard, it calls guard() function
    - Quiz room: Answer questions or die.
    """
    # So, our treasure_chest list contains 6 items.
    # treasure_chest = ["diamonds", "gold", "crown", "sword", "cork", "chalice"]
    print("""
    You see a room with a wooden treasure chest on the left, 
    and a sleeping guard on the right in front of the door.
    """)

    # Ask player what to do.
    action = input("What do you do? Left or Right? > ")

    # This is a way to see if the text typed by the player is in the list
    if action.lower() in ["treasure", "chest", "left", "l"]:
        print("""
        Ooh, treasure!
        Open it? Press '1'
        Leave it alone. Press '2'
        """)
        choice = input("> ")

        if choice == "1":
            print("""
            Let's see what's in here... /grins
            The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!
            You find some
            """)

            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_chest list, print the treasure.
            for treasure in treasure_chest:
                print(treasure)

            # So much treasure, what to do? Take it or leave it.
            print("What do you want to do?")
            # Get number of items in treasure chest with len))
            len(treasure_chest)

            print(f"""
            Take the treasure, press '1'
            Leave it, press '2'
            """)

            treasure_choice = input("> ")
            if treasure_choice == "1":
                treasure_chest.remove("sword")
                backpack.append("sword")
                print("""
                Your crappy sword is dull and rusty. 
                You decide that it would be wise to take the new one.
                You take the shinier sword from the treasure chest. It does look exceedingly shiny.
                Woo-hoo! Bounty and a shiny new sword. 
                You drop your crappy sword in the empty treasure chest.
                You try to take all the loot, but it won't fit.
                Your backpack is pretty small, and you can only fit 3 more items.
                Which items should you take?
                """)
                print(f"There is still {treasure_chest} in the chest.")
                treasure_chest.append("crappy sword")
                while len(backpack) <= 4:
                    item = input("Enter item : ")
                    treasure_chest.remove(item)
                    backpack.append(item)
                    print(f"You have placed {item} in your backpack")
                    print(f"There is still {treasure_chest} in the chest.")
                    print(f"You have {backpack} in your backpack")
                    if len(backpack) == 4:
                        print("Do you want to 'check the guard', go 'back' the way you came or 'move on'?")
                        action = input("What do you do? Check guard, move back or move on? > ")
                        if action.lower() in ["check guard", "guard", "g"]:
                            guard()
                        elif action.lower() in ["go back", "move back", "back", "b"]:
                            start_adventure()
                        elif action.lower() in ["move on", "on", "forward", "f", "on"]:
                            quiz_room()

            elif treasure_choice == "2":
                print("It will still be here (I hope), right after I get past this guard")
        elif choice == "2":
            print("Who needs treasure, let's get out of here. What about the guard though? ")
    elif action.lower() in ["guard", "right", "r"]:
        print("Let's have fun with the guard.")
        guard()
    else:
        print("Well, not sure what you picked there, let's poke the guard cos it's fun!")
    guard()


def secret_corridor():
    """
    The player finds a secret corridor.

    If player chooses
    - Left is a lake. There is a boat. If they take the boat, they can exit
    - Right, enters the Queens chamber.
    """

    # Ask player what to do.
    action = input("""
    You have entered the corridor.
    What do you do now? 
    'Left' to the boat or 'Right' through the door or 'Back'> 
    """)

    # This is a way to see if the text typed by player is in the list
    if action.lower() in ["left", "lake", "boat"]:
        print("""
        This might be a way out?
        Get in the boat? Press '1'
        Go to the door? Press '2'
        Go back? Press '3'
        """)
    if action.lower() in ["right", "door", "r"]:
        print("""
        Feeling a bit nosey?
        Let's go in!
        """)
        queens_chamber()
    if action.lower() in ["back", "blue", "b"]:
        print("""
        You go back to the blue door room.
        """)
        blue_door_room()

    choice = input("1 for boat, 2 for door or 3 for back > ")
    if choice == "1":
        print("""
        You climb inside the boat, and push the boat from the shore.
        You notice a leak. Your feet are getting wet. 
        It's only now that you realise that the boat is getting too heavy to paddle.
        If only you had a way to plug the hole?
        You have a look inside you backpack.
        """)
        print(f"You have {backpack} in your backpack")

        if 'cork' in backpack:
            print("""
            Aren't you glad you kept that cork!
            You take the cork from your backpack and plug the hole.
            The cork fits the hole perfectly, and you stop the leak.
            There is still a lot of water in the boat. 
            If you have the chalice, you use that to bail the water out,
            If not you have to dump you backpack over the side, or the boat will sink.""")

        if 'chalice' in backpack:
            print("""
            You bail the excess water with the chalice and head across the lake, to freedom.
            The water level in the boat lowers enough and you use you hands to paddle
            toward the light.You leave with your riches and live to fight another day!
            Well done!
            """)

            sail_home()

        else:
            print("""
            You paddle and paddle, to no avail, the boat is too heavy.
            With a heavy heart, you decide that your life is more precious
            than some treasure or an old backpack, so you drop it over the
            side. You'll be happy to get out of this mess.
            Now that the boat is lighter and the water level in the boat 
            lowers enough and you use you hands to paddle
            toward the light. Unfortunately the boat keeps sinking
            and you never make it out.
            """)

            you_died("""
            If you only had something to bail the water.
             \n<GAME OVER>
            """)

        if choice == "2":
            print("The door swings open with a creak.")
            queens_chamber()

        if choice == "3":
            print("You go back the way you came.")
            blue_door_room()


def red_door_room():
    """
    The red door room contains a red dragon.
    If a player types "flee" as an answer, the player returns to the room with two doors,
    otherwise, the player dies.
    if 'key' in backpack: open lock and kill Dragon master dragon flies away, and you win fortune.

    """
    print("""
    There you see a great red dragon. It is gigantic.
    You have never seen a dragon before and it is both beautiful and terrifying.
    It's head is the size of a wagon and it's body is larger than a house.
    When it breaths you can see smoke escape from it's mighty nostrils.
    The dragon is lying on a bed of gold and jewels.
    It would be hard to imagine a greater treasure.
    There is a chain that it locked to the dragon's leg
    and you can see a large pad lock.
    The dragon stares at you through one narrowed eye.
    A shiver goes down you spine.
    """)

    print("""
    You look around in a panic. The dragon starts to inhale.
    You know what's coming next.
    """)
    print("""
    Do you 'flee' for your life or 'stay'?            
    You see a way out, a corridor to the left or small alcove 
    to the right almost hidden by old dragon scales.
    They are as big as you.
    """)

    next_move = input("> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        print("""
        You run from the dragon and stumble into a secret corridor.
        You walk down the creepy corridor. There are stalactites and a constant dripping of water 
        A rat scurries past your feet, making you almost drop your sword.
        You come to a T-junction, to the left is a lake and on the shore, is a small and battered looking wooden 
        boat. To the right, is a strong wooden door. It is slightly ajar and there is light coming from inside.
        """)
        secret_corridor()
    else:
        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
        you_died("It eats you. Well, that was tasty!")


def dragons_lair():
    """
    The red door room contains a red dragon.
    If a player types "flee" as an answer, the player returns to the room with two doors,
    otherwise, the player dies.
    if 'key' in backpack: open lock and kill Dragon master dragon flies away, and you win fortune.

    """
    print("""
    You see a great red dragon. It is gigantic.
    You have never seen a dragon before and it is both beautiful and terrifying.
    It's head is the size of a wagon and it's body is larger than a house.
    When it breaths you can see smoke escape from it's mighty nostrils.
    The dragon is lying on a bed of gold and jewels.
    It would be hard to imagine a greater treasure.
    There is a chain that it locked to the dragon's leg
    and you can see a large pad lock.
    A shiver goes down you spine.
    """)
    time.sleep(10)
    print("""
    You hide behind a rock and wait. You don't have to wait long.
    A large figure enters the room. He is easily twice the size of anyone
    that you have ever seen. His armour and helmet are decorated with the crest of the dragon.
    This is Kali the usurper. 
    You watch as he enters the room and walks arrogantly before the dragon.
    You remember that his armour can resist the hottest fires and you wonder
    """)
    time.sleep(10)
    print("""
    You can see the lock to free the dragon, but it's out in the open. You will be exposed
    if you try to reach it. There are 2 dangers now, Kali and the dragon.
    You look around for ideas. You pick up a couple of old dragon scales.
    Do you throw one as a diversion or use one as a shield.
    """)

    next_move = input("throw or shield> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "throw" in next_move:
        print("""
              The scale is light, but almost as big as you are.
              You decide to toss it like a frisbee. It floats quietly across the room.
              Until it lands with a clatter on the opposite side.
              Kali turns around and faces away from both you and the lock.
              You run to the lock and are sliding the key in as he turns around to face you.
              This is the first time that you see his eyes. They are pits of black with flames
              glowing as pupils. His eyes grow brighter and you can feel the heat, as you turn the key.
               """)
        time.sleep(10)
        open_lock()
    else:
        print("""
                 You run to the lock, using the scale as a shield. The dragon and Kali both see you
                 at the same time. The dragon inhales deeply and exhales a mighty flame, but as you hoped
                 the scales are flame proof and you are alive. You reach for the lock while 
                 holding your fireproof shield. You reach for the lock, but it is hot from the fire.
                 As you fumble to get the key in the lock, Kali knocks the scale from your hands.
                 You are transfixed by his flaming eyes.     
                       """)
        you_died("Kali swings his axe and your head rolls on the floor.")


def queens_chamber():
    print("""
    You look inside and the room looks like a sleeping chamber.
    It is very plush, with ornate carvings and paintings on the wall.
    A woman has her back to you and is brushing her hair, while looking in the mirror.
    You notice a sceptre sitting on the table beside her. This must be the queen!
    """)
    time.sleep(10)
    queen()


def quiz_room():
    """
    The player finds a room.
    A wrinkly old man asks some riddles.

    If player chooses
    - To leave and go
    Or answer questions to pass through and gain a prize.
    """

    print("""
        You enter a room. At first, you think it's empty. There are a pile of rags in a heap on the ground.
        A strange noise like a banshees wail and wind starts swirling. 
        The rags get caught in the wind and start to rise.
        The wind begins to ebb, and you are standing face to face, with the oldest man that you have ever seen.
        He looks through you and his eyes start to burn like embers.
        The wind and the wailing subside and the man addresses you with a deep and rasping voice
        If you answer my riddles, you may leave with your heart's desires. 
        """)
    time.sleep(10)

    # Ask player what to do.
    action = input("What do you do? leave or stay > ")

    # This is a way to see if the text typed by the player is in the list
    if action.lower() in ["leave", "go", "back"]:
        print("""
        You turn round.
        Leave the way you came.
        """)
        blue_door_room()
    if action.lower() in ["answer", "in", "stay"]:
        print("""
        You can do this!
        You enter with caution and approach the old man.
        """)
        quiz_master()


def quiz():
    riddles = {
        1:
            {"question": """ 
            What can bring back the dead; make you cry, make you laugh, make you young; is born in an 
            instant, yet lasts a lifetime.
            """, "answer": "Memories"},
        2: {
            "question": """
            This thing devours all things: birds, beasts, trees, flowers; gnaws iron, bites steel; grinds
            hard stones to the meal.
            """, "answer": "Time"},
        3: {
            "question": """
            Some try to hide, some try to cheat; but time will show, we always will meet. Try as you might
            to guess my name.
            """, "answer": "Death"},
        4: {
            "question": """
            As small as your thumb, I am light in the air. You may hear me before you see me, 
            but trust that I'm here.
            """, "answer": "Hummingbird"},
        5: {
            "question": """
            I'm alive, but without breath; I'm as cold in life as in death; I'm never thirsty, 
            though I always drink.
            """, "answer": "Fish"}
    }

    def check_ans(quest, ans, att, total):
        """
        Takes the arguments, and confirms if the answer provided by user is correct.
        Converts all answers to lower case to make sure the quiz is not case-sensitive.
        """
        if riddles[quest]['answer'].lower() == ans.lower():
            print(f"Correct Answer! \nYour score is {total + 1}!")
            return True
        else:
            print(f"Wrong Answer :( \nYou have {att - 1} left! \nTry again...")
            return False

    def quiz_intro_message():
        """
        Introduces the user to the quiz and rules, and takes an input from the customer to start the quiz.
        Returns true regardless of any key pressed.
        """
        print("""
        In my lair, you'll answer me.
        These 5 questions, and you'll see?
        Count your chances, 1, 2, 3.
        If you fail, your blood feeds me.
        Press Enter to start the trial! 
        """)
        return True

    # python project.py
    quiz_intro_message()
    while True:
        score = 0
        for question in riddles:
            attempts = 3
            while attempts > 0:
                print(riddles[question]['question'])
                answer = input("Enter Answer : ")
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1
        if score < 5:
            print("""
            You have failed your mission, and now I will devour you!
            This is the last thing that you ever heard.
            """)
            you_died("""
            You weren't smart enough.
            The old man flies at you and you have no time to react. 
            The old man is a cannibal and starts eating your face.
            """)
        else:
            print(f"Your final score is {score}!\n\n")
            print("You have bested me. Your wisdom is boundless. Pass in peace.")
            print("You see a red door and a blue door.")
            door_picked = input("""
            Do you pick the red door, blue door? or corridor > 
            """)

            if door_picked == "red":
                red_door_room()
            elif door_picked == "blue":
                blue_door_room()
            elif door_picked == "corridor":
                secret_corridor()
            else:
                print("Sorry, it's either 'red', 'blue' or 'corridor'. You're the weakest link, goodbye!")
                exit(0)


# END ROOMS #


def get_player_name():
    """
    Gets player's name, may or may not be renamed depending on player's choice.
    Returns: Player name back (altered or unaltered)
    """
    # LOCAL VARIABLES
    # The player enters their name and gets assigned to a variable called "name"
    name = input("What's your name? > ")

    # This is just an alternative name that the game wants to call the player
    alt_name = "Rainbow Unicorn"
    answer = input(f"Your name is {alt_name.upper()}, is that correct? [Y|N] > ")

    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print(f"You are fun, {name.upper()}! Let's begin our adventure!")

    elif answer.lower() in ["n", "no"]:
        print(f"Ok, picky. {name.upper()} it is. Let's get started on our adventure.")
    else:
        print("Trying to be funny? Well, you will now be called {alt_name.upper()} anyway.")
        name = alt_name

    # Now notice that we are returning the variable called name.
    # In main(), it doesn't know what the variable "name" is, as it only exists in
    # get_player_name() function.
    # This is why indentation is important, variables declared in this block only exists in that block
    return name


def start_adventure():
    """
    This function starts the adventure by allowing two options for
    players to choose from: red or blue door

    Chosen option will print out the door chosen.
    """
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you pick the red door or blue door? > ")

    # Pick a door, and we go to a room and something else happens
    if door_picked == "red":
        red_door_room()
    elif door_picked == "blue":
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")


def main():
    """
    Gets the player's name by calling get_player_name() before starting the adventure.
    """
    player_name = get_player_name()

    ####################################################################
    # ACTIVITIES
    #
    # Read some of the best practices when writing Python code
    #   http://legacy.python.org/dev/peps/pep-0008/
    # Main thing is if you are using tabs, make sure it's 4-spaces,
    # most editors will convert it (check preferences/settings).
    #
    # Modify the code
    # - add taunting the guard or talking
    # - sword fight with the guard, and keep track of health points (HP)
    # - puzzles like 1+2 during an encounter
    # - modify blue_door_room()'s if statement,
    #   so it takes into account player typing "right" or "guard"
    #   Hint: Add another elif before the else statement
    #
    # So many if statements, this can be made simpler and easier to
    # maintain by using Finite State Machine (FSM)
    # You can find info about it, but it will mainly be touching
    # object-orient programming, which is another lesson for another day.
    #
    #####################################################################

    start_adventure()

    print("\nthe end\n")
    print(f"Thanks for playing, {player_name.upper()}")


if __name__ == '__main__':
    main()
