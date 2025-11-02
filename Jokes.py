import random

# Use a dictionary to store topic names and their corresponding joke lists.
# This makes it easy to add, remove, or modify joke topics without
# changing the core logic of the `get_topics` function.
# The keys are 1-based to align with user input display.
joke_categories = {
    1: {
        "name": "Technology Jokes",
        "jokes": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to the doctor? It had a virus!",
            "Why was the mobile phone wearing glasses? Because it lost its contacts.",
            "Why did the PowerPoint presentation cross the road? To get to the other slide.",
            "What happens when a hard drive gets into a fight? It asks for a back-up!",
            "What do you call a computer that sings? A Dell.",
            "Why did the computer catch a cold? It had too many windows open.",
            "Why was the smartphone wearing glasses? It lost all its contacts.",
            "I changed my password to “incorrect.” So, whenever I forget it, my computer says, “Your password is incorrect.”",
            "Why do Java developers wear glasses? Because they don't C#.",
            "Why did the boy get fired from his keyboard factory job? Because he was not doing enough shifts.",
            "What do you call an iPhone that sleeps too much? Dead Siri-ous.",
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why was the website bring a ladder? Because it wanted to reach the top of the search results.",
            "Why were the horses struggling to use the internet? Because they were not able to find any stable connections.",
            "What is another name for apple juice? iPhone chargers.",
            "Why did the computer go to art school? It wanted to learn to draw in Paint.",
            "What does a baby computer call its father? Data!",
            "Why was 'beef stew' not used as a computer password? Because it was not strong-anoff.",
            "How do robots pay for things? With cache.",
        ],
    },
    2: {
        "name": "Programming Jokes",
        "jokes": [
            "Why did the programmer quit his job? Because he didn't get arrays.",
            "You are the ; to my statements.",
            "What did the Java Code say to the C code? You’ve got no class.",
            "A programmer puts two glasses on his bedside table before going to sleep. A full one, in case he gets thirsty, and an empty one, in case he doesn’t.",
            "Things aren’t always #000000 and #FFFFFF.",
            "Why do Java programmers have to wear glasses? Because they don’t C#.",
            "A programmer is heading out to the grocery store, so his wife tells him “get a gallon of milk, and if they have eggs, get a dozen.” He returns with 13 gallons of milk.",
            "Programmer: An organism that turns coffee into software.",
            "There’s no place like 127.0.0.1.",
            "Why do programmers take so long in the shower? They read the directions on the shampoo bottle and follow them to the letter: Lather, rinse, and repeat.",
            "If at first you don’t succeed, call it version 1.0.",
            "My mind is like an internet browser, 19 tabs open, 3 of them are frozen, ads popping up everywhere, I have no idea where the music is coming from.",
            "while (alive) { eat(); sleep (); code ();}",
            "What do you call a programmer who vomits at IHOP? A stack overflow.",
            "Computers will never fully replace humans until they learn to laugh at the boss’s jokes.",
            "All programmers are playwrights, and all computers are lousy actors.",
            "Algorithm: words used by programmers when they don’t want to explain what they did.",
            "When in doubt // it out.",
            "What do cats and programmers have in common? When either one is unusually happy and excited, it’s because they found a bug.",
            "[“hip”,”hip”] (hip hip array!)",
        ],
    },
    3: {
        "name": "Math Jokes",
        "jokes": [
            "Hey, have you ever noticed what's odd? Every other number!",
            "Do you know what mathematicians do after it snows? They make snow angles!",
            "Which tool is best for math? The multi-pliers.",
            "Swimmers love one kind of math more than all others, what is it? Dive-ision!",
            "Once there was a hen who counted her own eggs. She was a mathemachicken!",
            "Why was six afraid of seven? Because seven, eight, nine!",
            "Did you know that there are three kinds of people in the world? People who can count and people who can’t.",
            "Do you know why the two 4s didn’t go to the cafeteria for lunch? They already 8!",
            "What is a math teacher’s favorite season? SUMmer.",
            "What do you call a snake that solves math equations? An adder.",
            "Why won’t Goldilocks drink a glass of water with 8 pieces of ice in it? It’s too cubed.",
            "Why did the student do multiplication problems on the floor? The teacher told him not to use tables.",
            "What tool is best suited for math? Multi-pliers.",
            "Why do plants hate math? Because it gives them square roots.",
            "What’s a swimmer’s favorite math? Dive-ision.",
            "Why was Mr. Gilson’s class so noisy? He liked to practice gong division.",
            "Why did the girl wear glasses during math class? It improved di-vision.",
            "What do you get when you cross a math teacher with a clock? Times tables.",
            "Why did the student stop doing their long division homework? Because it had used up the remainder of their patience.",
        ],
    },
    4: {
        "name": "Science Jokes",
        "jokes": [
            "What did one tectonic plate say when he bumped into the other? Sorry! My fault.",
            "What did the biologist wear to impress his date? Designer genes.",
            "What did the stamen say to the pistil? I like your style!",
            "What type of fish is made out of two sodium atoms? 2 Na.",
            "Why are chemists excellent for solving problems? They have all the solutions.",
            "What did the femur say to the patella? I knee'd you!",
            "Where did the chemist have his lunch? On a periodic table.",
            "Why is combining a proton and an electron to make a neutron so popular? Because it's free of charge.",
            "I lost an electron! Are you positive?",
            "Why did the amoeba fail its math test? Because it multiplied by dividing.",
            "Why do plants hate algebra so much? Because it gives them square roots.",
            "Why did the physicist break up with the biologist? Because there was no chemistry.",
            "What’s a geologist's favorite type of music? Rock.",
            "Why did Mickey Mouse decide to go to space? To see Pluto!",
            "What did one ion say to another? I've got my ion you.",
            "Did you hear about the new theory on inertia? It doesn't seem to be gaining momentum.",
            "What is a snake's favorite subject? Hiss-story.",
            "Why did the germ cross the microscope? To get to the other slide.",
            "My girlfriend told me I was average. She is so mean!",
            "What did the guy say when his wife threw sodium and chloride at him? That's a(s)-salt!",
        ],
    },
    5: {
        "name": "Miscellaneous Jokes",
        "jokes": [
            "What do you call a pig that does karate? A pork chop.",
            "Where does Batman go to the bathroom? The batroom.",
            "What did the left eye say to the right eye? Between you and me, something smells.",
            "Why didn't the melons get married? Because they cantaloupe.",
            "What do you call a fake noodle? An impasta.",
            "How did the pig get to the hogspital? In a hambulance.",
            "I'm so good at sleeping I can do it with my eyes closed!",
            "Why does Humpty Dumpty love autumn? Because he had a great fall.",
            "Why did the cow jump over the moon? The farmer had cold hands.",
            "How do celebrities stay cool? They have many fans.",
            "What do you call a pudgy psychic? A four-chin teller.",
            "How much money does a pirate pay for corn? A buccaneer.",
            "Where do young trees go to learn? Elementree school.",
            "Why do bees have sticky hair? Because they use a honeycomb.",
            "How did the student feel when he learned about electricity? Totally shocked.",
            "Why was six afraid of seven? Because 7-8-9.",
            "I tried to catch fog yesterday. Mist.",
            "Two peanuts were walking down the street. One was a-salted.",
            "What did the buffalo say when his kid went to college? Bison.",
            "What did the mayonnaise say when the refrigerator door was opened? Close the door, I'm dressing.",
        ],
    },
    6: {
        "name": "General Jokes",
        "jokes": [
            "Did you hear about the circus fire? It was in tents!",
            "How do you catch a squirrel? Climb a tree and act like a nut!",
            "Did you hear about the guy who invented Lifesavers? They say he made a mint!",
            "I told my wife she should embrace her mistakes. She gave me a hug.",
            "Why don't eggs tell jokes? They might crack up!",
            "What did the big flower say to the little flower? 'Hi, bud!'",
            "I went to buy some camouflage pants, but I couldn't find any.",
            "What did the grape say when it got stepped on? Nothing, it just let out a little wine.",
            "What do you call a snowman with a six-pack? An abdominal snowman!",
            "Why don't skeletons fight each other? They don't have the guts!",
            "Did you hear about the restaurant on the moon? Great food, no atmosphere!",
            "Why did the math book look sad? Because it had too many problems!",
            "What did one hat say to the other hat? You stay here, I'll go on ahead!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "Why was the broom late? It swept in!",
            "How do you make Holy water? You boil the hell out of it!",
            "What do you call cheese that isn't yours? Nacho cheese.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "What do you get when you cross a snowman and a vampire? Frostbite.",
        ],
    },
    7: {
        "name": "Dark Jokes",
        "jokes": [
            "Why did the zombies get divorced? Their marriage was dead.",
            "What do you call headphones that walk out on their children? Deadbeats.",
            "I can’t believe I got fired from the calendar factory. All I did was take a day off.",
            "When I was a kid, I was afraid of the dark. Now that I’m grown up, the electricity bill made me afraid of the light.",
            "Welcome to Plastic Surgery Anonymous. Nice to meet so many new faces.",
            "My wife is mad that I ruined our anniversary. I’m not sure how; I didn’t even know it was today.",
            "I tried to warn my son about playing Russian roulette. It went in one ear and out the other.",
            "I took my family skydiving. I should have given them parachutes.",
            "Did you hear about the guy who lost his left side? He’s all right now!",
            "Why do vampires seem unwell? They’re always coffin.",
            "The only concept that flat-earthers fear is sphere itself.",
            "Why did the skeleton go to prom? Because he had nobody to go with.",
            "I bought my blind friend a cheese grater for his birthday. He later told me it was the most violent book he’d ever read.",
            "My girlfriend dumped me, so I stole her wheelchair. Guess who came crawling back?",
            "I asked my wife to clean the oven. I probably should have turned it off first.",
            "When my uncle Frank passed away, he requested his ashes buried in his favorite beer. His wish was to be Frank in Stein.",
            "Don’t challenge Death to a pillow fight unless you’re ready for the reaper cushions.",
            "I thought opening a door for a lady was good manners, but she just screamed and flew out of the plane.",
            "I can’t believe I got fired from the calendar factory. All I did was take a day off.",
            "I once had a job smashing cans.",
        ],
    },
}


def get_topic_choice() -> int:
    """
    Prompts the user to select a topic number and validates the input.
    Returns the valid topic number. Exits the program if 0 is entered.
    """
    while True:
        try:
            choice = int(input("Enter the topic number (0 to exit): "))
            if choice == 0:
                print("Exiting Jokes program. Goodbye!")
                exit()
            if choice in joke_categories:
                return choice
            else:
                print(
                    f"Invalid topic number. Please enter a number between 1 and {len(joke_categories)}."
                )
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_random_joke_from_topic(topic_num: int) -> str:
    """
    Retrieves a random joke from the specified topic number.
    Args:
        topic_num (int): The 1-based index of the joke topic.
    Returns:
        str: A random joke from the selected topic.
    Raises:
        KeyError: If topic_num is not found in joke_categories, though get_topic_choice should prevent this.
    """
    selected_category = joke_categories[topic_num]
    return random.choice(selected_category["jokes"])


if __name__ == "__main__":
    print("Welcome to Jokes!")

    # Display available topics dynamically from the dictionary
    for num, category_info in joke_categories.items():
        print(f"{num}. {category_info['name']}")

    # Get user choice and validate
    chosen_topic_num = get_topic_choice()

    # Get the joke
    selected_joke = get_random_joke_from_topic(chosen_topic_num)

    # Print the joke
    print(
        f"\nHere's a joke from the topic '{joke_categories[chosen_topic_num]['name']}':"
    )
    print(selected_joke)
