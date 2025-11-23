print("Welcome to the Game!\nHere there will be 6 Topics and you will have to choose a Topic and Answer the Questions \nTotally 15 Questions will be asked.")


def choice_selection(choice):
    if choice == 1:
        print("You have chosen Sports")
        quiz_section(Sports_questions)
    elif choice == 2:
        print("You have chosen Tech")
        quiz_section(Tech_questions)
    elif choice == 3:
        print("You have chosen Food")
        quiz_section(Food_questions)
    elif choice == 4:
        print("You have chosen History")
        quiz_section(History_questions)
    elif choice == 5:
        print("You have chosen Space")
        quiz_section(Space_questions)
    elif choice == 6:
        print("You have chosen Math")
        quiz_section(Math_questions)
    elif choice == 0:
        print("Thank you for playing!")
        exit()
    else:
        print("Invalid Choice")


#Sport_questions

Sports_questions = [
    {
        "question": "In which sport would you perform a slam dunk?",
        "options": ["A) Basketball", "B) Soccer", "C) Tennis", "D) Baseball"],
        "answer": "A"
    },
    {
        "question": "How many players are on a soccer team on the field at the start of a match?",
        "options": ["A) 9", "B) 10", "C) 11", "D) 12"],
        "answer": "C"
    },
    {
        "question": "In which sport is the term 'love' used?",
        "options": ["A) Tennis", "B) Badminton", "C) Squash", "D) Table Tennis"],
        "answer": "A"
    },
    {
        "question": "What is the term for a score of three strikes in a row in bowling?",
        "options": ["A) A birdie", "B) A hat-trick", "C) A trifecta", "D) A turkey"],
        "answer": "D"
    },
    {
        "question": "In which country were the first modern Olympic Games held?",
        "options": ["A) Italy", "B) France", "C) Greece", "D) USA"],
        "answer": "C"
    },
    {
        "question": "What is the name of the trophy awarded to the winner of the Stanley Cup?",
        "options": ["A) The Lord Stanley Prize", "B) The Ice Crown", "C) The Hockey Grail", "D) The Stanley Cup is the name of the trophy itself"],
        "answer": "D"
    },
    {
        "question": "Which two teams share the record for the most NBA championship titles?",
        "options": ["A) Boston Celtics and the LA Lakers", "B) Chicago Bulls and Golden State Warriors", "C) New York Knicks and Philadelphia 76ers", "D) Miami Heat and San Antonio Spurs"],
        "answer": "A"
    },
    {
        "question": "What is the diameter of a basketball hoop in inches?",
        "options": ["A) 22", "B) 20", "C) 18", "D) 24"],
        "answer": "C"
    },
    {
        "question": "What sport is called the “sport of kings”?",
        "options": ["A) Horse Racing", "B) Fencing", "C) Polo", "D) Chess"],
        "answer": "C"
    },
    {
        "question": " Which country has played in every soccer World Cup?",
        "options": ["A) Brazil", "B) Germany", "C) Italy", "D) Argentina"],
        "answer": "A"
    },
]

    
#Tech_questions
Tech_questions = [
    {
        "question": "What does HTTP stand for?",
        "options": ["A) HyperText Transfer Protocol", "B) HighText Transfer Protocol", "C) HyperText Transmission Protocol", "D) HighText Transmission Protocol"],
        "answer": "A"
    },
    {
        "question": "What does 'Wi-Fi' stand for?",
        "options": ["A) Wireless Fidelity", "B) Wide Frequency", "C) Wireless Firewall", "D) It does not stand for anything"],
        "answer": "D"
    },
    {
        "question": "What is the main function of the ALU (Arithmetic Logic Unit)?",
        "options": ["A) Store data", "B) Perform calculations", "C) Manage memory", "D) Control input/output"],
        "answer": "B"
    },
    {
        "question": "Which programming language is known as the backbone of web development?",
        "options": ["A) Python", "B) Java", "C) JavaScript", "D) C++"],
        "answer": "C"
    },
    {
        "question": "What does CSS stand for?",
        "options": ["A) Creative Style Sheets", "B) Colorful Style Sheets", "C) Computer Style Sheets", "D) Cascading Style Sheets"],
        "answer": "D"
    },
    {
        "question": "What does 'URL' stand for?",
        "options": ["A) Uniform Resource Locator", "B) Universal Resource Locator", "C) Uniform Resource Link", "D) Universal Resource Link"],
        "answer": "A"
    },
    {
        "question": "In what year was the first email sent?",
        "options": ["A) 1965", "B) 1971", "C) 1980", "D) 1990"],
        "answer": "B"
    },
    {
        "question": "What social media platform is known for its 280-character limit?",
        "options": ["A) X (formerly Twitter)", "B) Facebook", "C) Instagram", "D) LinkedIn"],
        "answer": "A"
    },
    {
        "question": "What was the original name of the programming language Java?",
        "options": ["A) Orange", "B) Pine", "C) Maple", "D) Oak"],
        "answer": "D"
    },
    {
        "question": " What is the name of the first widely used web browser?",
        "options": ["A) Internet Explorer", "B) Opera", "C) Netscape Navigator", "D) Mosaic"],
        "answer": "D"
    }
]


#Food_questions
Food_questions = [
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["A) Tomato", "B) Avocado", "C) Onion", "D) Lime"],
        "answer": "B"
    },
    {
        "question": "From which country does pizza originate?",
        "options": ["A) USA", "B) Greece", "C) Italy", "D) France"],
        "answer": "C"
    },
    {
        "question": "What is the primary ingredient in the Japanese dish, sushi?",
        "options": ["A) Raw fish", "B) Seaweed", "C) Vinegared rice", "D) Soy sauce"],
        "answer": "C"
    },
    {
        "question": "What is the most consumed manufactured drink in the world?",
        "options": ["A) Coffee", "B) Coca-Cola", "C) Tea", "D) Orange Juice"],
        "answer": "C"
    },
    {
        "question": "What is the most expensive spice in the world by weight?",
        "options": ["A) Vanilla", "B) Saffron", "C) Cardamom", "D) Cloves"],
        "answer": "B"
    },
    {
        "question": "From which country do French fries originate?",
        "options": ["A) France", "B) USA", "C) Belgium", "D) Germany"],
        "answer": "C"
    },
    {
        "question": "What is the main ingredient in hummus?",
        "options": ["A) Lentils", "B) Chickpeas", "C) Black Beans", "D) Tahini"],
        "answer": "B"
    },
    {
        "question": "Which country is the largest producer of coffee in the world?",
        "options": ["A) Colombia", "B) Vietnam", "C) Brazil", "D) Ethiopia"],
        "answer": "C"
    },
    {
        "question": "What type of pasta is shaped like a bowtie?",
        "options": ["A) Penne", "B) Fusilli", "C) Farfalle", "D) Rigatoni"],
        "answer": "C"
    },
    {
        "question": "What is the only food that does not spoil?",
        "options": ["A) Salt", "B) Honey", "C) Dried rice", "D) Sugar"],
        "answer": "B"
    },
    {
        "question": "Which nut is used to make marzipan?",
        "options": ["A) Walnut", "B) Pistachio", "C) Almond", "D) Hazelnut"],
        "answer": "C"
    },
    {
        "question": "What is the most popular fruit in the world?",
        "options": ["A) Banana", "B) Apple", "C) Mango", "D) Tomato"],
        "answer": "D"
    },
    {
        "question": "What is the name of the fungus used to make bread rise?",
        "options": ["A) Mold", "B) Yeast", "C) Mushroom", "D) Penicillin"],
        "answer": "B"
    },
    {
        "question": "What is the main flavor of the liqueur Cointreau?",
        "options": ["A) Lemon", "B) Orange", "C) Cherry", "D) Anise"],
        "answer": "B"
    },
    {
        "question": "From which plant is tequila made?",
        "options": ["A) Cactus", "B) Agave", "C) Sugarcane", "D) Yucca"],
        "answer": "B"
    }
]


# History Quiz Questions
History_questions = [
    {
        "question": "Who was the first Prime Minister of India?",
        "options": ["A) Mahatma Gandhi", "B) Sardar Vallabhbhai Patel", "C) Jawaharlal Nehru", "D) Indira Gandhi"],
        "answer": "C"
    },
    {
        "question": "In which year did India gain independence from British rule?",
        "options": ["A) 1950", "B) 1947", "C) 1945", "D) 1942"],
        "answer": "B"
    },
    {
        "question": "The ancient city of Rome was built on how many hills?",
        "options": ["A) Five", "B) Seven", "C) Nine", "D) Three"],
        "answer": "B"
    },
    {
        "question": "Who was the first emperor of Rome?",
        "options": ["A) Julius Caesar", "B) Augustus", "C) Nero", "D) Constantine"],
        "answer": "B"
    },
    {
        "question": "In what year did World War I begin?",
        "options": ["A) 1912", "B) 1914", "C) 1916", "D) 1918"],
        "answer": "B"
    },
    {
        "question": "What was the name of the ship that brought the Pilgrims to America in 1620?",
        "options": ["A) The Santa Maria", "B) The Titanic", "C) The Mayflower", "D) The Discovery"],
        "answer": "C"
    },
    {
        "question": "Who invented the printing press?",
        "options": ["A) Leonardo da Vinci", "B) Johannes Gutenberg", "C) Isaac Newton", "D) Galileo Galilei"],
        "answer": "B"
    },
    {
        "question": "Who was the last queen of France?",
        "options": ["A) Queen Elizabeth I", "B) Catherine the Great", "C) Marie Antoinette", "D) Queen Victoria"],
        "answer": "C"
    },
    {
        "question": "The ancient pyramids are located in which country?",
        "options": ["A) Greece", "B) Mexico", "C) Egypt", "D) Sudan"],
        "answer": "C"
    },
    {
        "question": "What was the Renaissance?",
        "options": ["A) A war in the Middle Ages", "B) A period of \"rebirth\" in arts and science", "C) An ancient Roman festival", "D) A style of architecture"],
        "answer": "B"
    },
    {
        "question": "Who was the first woman to fly solo across the Atlantic Ocean?",
        "options": ["A) Amelia Earhart", "B) Bessie Coleman", "C) Harriet Quimby", "D) Sally Ride"],
        "answer": "A"
    },
    {
        "question": "In which country did the Industrial Revolution begin?",
        "options": ["A) France", "B) Germany", "C) Great Britain", "D) United States"],
        "answer": "C"
    },
    {
        "question": "Who wrote the \"I Have a Dream\" speech?",
        "options": ["A) Malcolm X", "B) Martin Luther King Jr.", "C) Nelson Mandela", "D) Abraham Lincoln"],
        "answer": "B"
    },
    {
        "question": "What empire was ruled by Genghis Khan?",
        "options": ["A) The Ottoman Empire", "B) The Roman Empire", "C) The Mongol Empire", "D) The Persian Empire"],
        "answer": "C"
    },
    {
        "question": "What is the oldest university in the world?",
        "options": ["A) University of Oxford", "B) University of Bologna", "C) University of al-Qarawiyyin", "D) Harvard University"],
        "answer": "C"
    }
]


# Space Quiz Questions
Space_questions = [
    {
        "question": "What is the name of the galaxy our solar system is in?",
        "options": ["A) Andromeda", "B) The Milky Way", "C) Triangulum", "D) Whirlpool"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the \"Red Planet\"?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "Who was the first human to walk on the moon?",
        "options": ["A) Yuri Gagarin", "B) Buzz Aldrin", "C) Neil Armstrong", "D) Michael Collins"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Saturn", "C) Jupiter", "D) Neptune"],
        "answer": "C"
    },
    {
        "question": "What is the name of the force that holds us to the Earth?",
        "options": ["A) Magnetism", "B) Gravity", "C) Friction", "D) Centripetal Force"],
        "answer": "B"
    },
    {
        "question": "How many planets are in our solar system?",
        "options": ["A) Seven", "B) Eight", "C) Nine", "D) Ten"],
        "answer": "B"
    },
    {
        "question": "What is the closest star to Earth?",
        "options": ["A) Proxima Centauri", "B) Alpha Centauri A", "C) The Sun", "D) Sirius"],
        "answer": "C"
    },
    {
        "question": "What is a \"light-year\"?",
        "options": ["A) The time it takes light to travel around the Earth", "B) The distance light travels in one year", "C) A unit of time equal to 365 days", "D) The speed of light"],
        "answer": "B"
    },
    {
        "question": "What is the name of the first artificial satellite sent into space?",
        "options": ["A) Explorer 1", "B) Sputnik 1", "C) Vanguard 1", "D) Hubble"],
        "answer": "B"
    },
    {
        "question": "Which planet is famous for its rings?",
        "options": ["A) Jupiter", "B) Uranus", "C) Saturn", "D) Neptune"],
        "answer": "C"
    },
    {
        "question": "What is the name of the American space agency?",
        "options": ["A) ESA", "B) Roscosmos", "C) NASA", "D) ISRO"],
        "answer": "C"
    },
    {
        "question": "How long does it take for the Earth to orbit the Sun?",
        "options": ["A) 365.25 days", "B) 365 days", "C) 366 days", "D) 356 days"],
        "answer": "A"
    },
    {
        "question": "What is the name of the largest volcano in our solar system, located on Mars?",
        "options": ["A) Mauna Kea", "B) Mount Everest", "C) Olympus Mons", "D) Arsia Mons"],
        "answer": "C"
    },
    {
        "question": "What is the name of the second-largest planet in our solar system?",
        "options": ["A) Jupiter", "B) Saturn", "C) Uranus", "D) Neptune"],
        "answer": "B"
    },
    {
        "question": "Who was the first person to travel into space?",
        "options": ["A) Neil Armstrong", "B) Yuri Gagarin", "C) Alan Shepard", "D) John Glenn"],
        "answer": "B"
    }
]


# Math Quiz Questions
Math_questions = [
    {
        "question": "What is the value of Pi to two decimal places?",
        "options": ["A) 3.12", "B) 3.14", "C) 3.16", "D) 3.18"],
        "answer": "B"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A) Five", "B) Six", "C) Seven", "D) Eight"],
        "answer": "B"
    },
    {
        "question": "What is the sum of the interior angles of a triangle?",
        "options": ["A) 90 degrees", "B) 180 degrees", "C) 270 degrees", "D) 360 degrees"],
        "answer": "B"
    },
    {
        "question": "What is 5 to the power of 3?",
        "options": ["A) 15", "B) 25", "C) 125", "D) 53"],
        "answer": "C"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    },
    {
        "question": "In a right-angled triangle, what is the name for the longest side?",
        "options": ["A) Adjacent", "B) Opposite", "C) Hypotenuse", "D) Vertex"],
        "answer": "C"
    },
    {
        "question": "What do you call a polygon with 8 sides?",
        "options": ["A) A hexagon", "B) A decagon", "C) An octagon", "D) A nonagon"],
        "answer": "C"
    },
    {
        "question": "What is the next number in the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...?",
        "options": ["A) 11", "B) 12", "C) 13", "D) 14"],
        "answer": "C"
    },
    {
        "question": "What does the Roman numeral \"C\" represent?",
        "options": ["A) 50", "B) 100", "C) 500", "D) 1000"],
        "answer": "B"
    },
    {
        "question": "What is the square root of 144?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 14"],
        "answer": "C"
    },
    {
        "question": "What is 9 multiplied by 7?",
        "options": ["A) 56", "B) 63", "C) 72", "D) 81"],
        "answer": "B"
    },
    {
        "question": "How many seconds are in one hour?",
        "options": ["A) 60", "B) 1200", "C) 3600", "D) 6000"],
        "answer": "C"
    },
    {
        "question": "An angle greater than 90 degrees but less than 180 degrees is called what?",
        "options": ["A) An acute angle", "B) An obtuse angle", "C) A right angle", "D) A reflex angle"],
        "answer": "B"
    },
    {
        "question": "What is the perimeter of a circle called?",
        "options": ["A) Diameter", "B) Radius", "C) Circumference", "D) Arc"],
        "answer": "C"
    },
    {
        "question": "What number is represented by a \"Googol\"?",
        "options": ["A) 1 followed by 10 zeros", "B) 1 followed by 100 zeros", "C) 1 followed by 1,000 zeros", "D) 1 followed by 1,000,000 zeros"],
        "answer": "B"
    }
]


# Main Logic
def quiz_section(given_topic):
    for i in range(len(given_topic)):
        if i == len(given_topic):
            print(f"Your Final score is: {score}/{i+1}\n")
        print(f"Q{i+1}. {given_topic[i]['question']}")
        for option in given_topic[i]['options']:
            print(option)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        if user_answer == given_topic[i]['answer']:
            print("Correct!\n")
            global score
            score += 1
            print(f"Your current score is: {score}/{i+1}\n")
        elif user_answer not in ["A", "B", "C", "D"]:
            print("Invalid option. Please choose A, B, C, or D.")
        else:
            print(f"Wrong! The correct answer is {given_topic[i]['answer']}")
            print(f"Your current score is: {score}/{i+1}\n")


if __name__ == "__main__":
    score = 0
    choice = int(input("Choose a Topic from the following:\n1.Sports\n2.Tech\n3.Food\n4.History\n5.Space\n6.Math\nIf you want to exit the quiz, enter 0\nENTER YOUR CHOICE IN NUMBER:"))
    choice_selection(choice)
    exit()