# PYTHON LEARNING HUB
# An Interactive Python Tutorial Program

colors = ["RED", "BLUE", "GREEN", "PURPLE", "YELLOW"]
selected_color = random.choice(colors)

print("=" * 45)
print("WELCOME TO PYTHON LEARNING HUB".center(45))
print("=" * 45)
print("Welcome color:", selected_color)

name = input("\nEnter your name, future coder: ")
print("\nHello,", name + "!")
print("Let's learn Python together.")

chapters = {
    "1": {
        "title": "Introduction to Programming and Problem Solving",
        "lessons": [
            "Programming is the process of creating instructions for a computer.",
            "Problem solving means finding a solution to a given problem.",
            "An algorithm is a step-by-step procedure for solving a problem.",
            "Pseudocode is a simple way of writing program instructions.",
            "A flowchart is a diagram that shows the steps of a process.",
            "Program logic is the sequence of instructions used to solve a problem.",
            "The problem-solving process includes understanding, planning, designing, coding, testing, and improving the solution."
        ],
        "questions": [
            {
                "question": "What is an algorithm?",
                "choices": [
                    "A. A step-by-step procedure",
                    "B. A computer screen",
                    "C. A programming language"
                ],
                "answer": "A"
            },
            {
                "question": "When was Python programming created?",
                "choices": [
                    "A. 1999",
                    "B. 1991",
                    "C. 1995"
                ],
                "answer": "B"
            },
            {
                "question": "Who created Python programming?",
                "choices": [
                    "A. Jose Rizal",
                    "B. Sir Jomar Sangil",
                    "C. Guido van Rossum"
                ],
                "answer": "C"
            }
        ]
    },

    "2": {
        "title": "Python Basic Syntax",
        "lessons": [
            "Python is a high-level programming language.",
            "Syntax refers to the rules for writing Python code.",
            "Python uses indentation to organize code blocks.",
            "The print() function displays information on the screen."
        ],
        "questions": [
            {
                "question": "Which function displays output in Python?",
                "choices": [
                    "A. input()",
                    "B. print()",
                    "C. random()"
                ],
                "answer": "B"
            },
            {
                "question": "What is Python?",
                "choices": [
                    "A. A programming language",
                    "B. A computer device",
                    "C. An operating system"
                ],
                "answer": "A"
            },
            {
                "question": "What is used to organize code blocks in Python?",
                "choices": [
                    "A. Symbols",
                    "B. Numbers",
                    "C. Indentation"
                ],
                "answer": "C"
            }
        ]
    },

    "3": {
        "title": "Arithmetic Operators and Expressions",
        "lessons": [
            "Arithmetic operators are used to perform mathematical operations.",
            "Addition (+) adds numbers.",
            "Subtraction (-) subtracts numbers.",
            "Multiplication (*) multiplies numbers.",
            "Division (/) divides numbers.",
            "Modulus (%) returns the remainder.",
            "Exponentiation (**) raises a number to a power."
        ],
        "questions": [
            {
                "question": "What is the result of 5 + 3 * 2?",
                "choices": [
                    "A. 16",
                    "B. 11",
                    "C. 13"
                ],
                "answer": "B"
            },
            {
                "question": "Which operator is used for multiplication?",
                "choices": [
                    "A. *",
                    "B. +",
                    "C. /"
                ],
                "answer": "A"
            },
            {
                "question": "Which operator gives the remainder?",
                "choices": [
                    "A. **",
                    "B. /",
                    "C. %"
                ],
                "answer": "C"
            }
        ]
    },

    "4": {
        "title": "Variables, Constants, and Data Types",
        "lessons": [
            "A variable stores a value in a program.",
            "A constant is a value intended not to change.",
            "Common Python data types include:",
            "int - whole numbers",
            "float - decimal numbers",
            "str - text or characters",
            "bool - True or False values."
        ],
        "questions": [
            {
                "question": "Which data type is used for text?",
                "choices": [
                    "A. int",
                    "B. float",
                    "C. str"
                ],
                "answer": "C"
            },
            {
                "question": "Which data type is used for whole numbers?",
                "choices": [
                    "A. int",
                    "B. str",
                    "C. bool"
                ],
                "answer": "A"
            },
            {
                "question": "Which data type stores True or False?",
                "choices": [
                    "A. float",
                    "B. bool",
                    "C. str"
                ],
                "answer": "B"
            }
        ]
    },

    "5": {
        "title": "Basic Input and Output",
        "lessons": [
            "Input means receiving information from the user.",
            "The input() function gets information from the user.",
            "Output means displaying information.",
            "The print() function displays output.",
            "Example: name = input('Enter your name: ')",
            "Example: print('Hello', name)"
        ],
        "questions": [
            {
                "question": "Which function receives information from the user?",
                "choices": [
                    "A. print()",
                    "B. input()",
                    "C. type()"
                ],
                "answer": "B"
            },
            {
                "question": "Which function displays output?",
                "choices": [
                    "A. print()",
                    "B. input()",
                    "C. int()"
                ],
                "answer": "A"
            },
            {
                "question": "What does input() do?",
                "choices": [
                    "A. Deletes information",
                    "B. Closes the program",
                    "C. Gets information from the user"
                ],
                "answer": "C"
            }
        ]
    },

    "6": {
        "title": "Conditional Statements and Logical Operators",
        "lessons": [
            "A condition is an expression that evaluates to True or False.",
            "An if statement executes code when a condition is True.",
            "An if-else statement provides two possible paths.",
            "An if-elif-else statement checks multiple conditions.",
            "Logical operators combine or change conditions.",
            "and - True when both conditions are True.",
            "or - True when at least one condition is True.",
            "not - reverses a Boolean result."
        ],
        "questions": [
            {
                "question": "Which logical operator is True when both conditions are True?",
                "choices": [
                    "A. or",
                    "B. not",
                    "C. and"
                ],
                "answer": "C"
            },
            {
                "question": "Which statement is used to check a condition?",
                "choices": [
                    "A. if",
                    "B. print",
                    "C. input"
                ],
                "answer": "A"
            },
            {
                "question": "What does the else statement do?",
                "choices": [
                    "A. Repeats the program",
                    "B. Executes when the if condition is False",
                    "C. Gets user input"
                ],
                "answer": "B"
            }
        ]
    },

    "7": {
        "title": "Introduction to Iteration and Loops",
        "lessons": [
            "Iteration means repeating a set of instructions.",
            "A loop repeats code while a condition or sequence allows it.",
            "A for loop is commonly used to repeat instructions for each item in a sequence.",
            "A while loop repeats instructions while its condition is True.",
            "Loops help reduce repeated code."
        ],
        "questions": [
            {
                "question": "Which loop repeats while a condition is True?",
                "choices": [
                    "A. while loop",
                    "B. print loop",
                    "C. input loop"
                ],
                "answer": "A"
            },
            {
                "question": "Which loop is commonly used to go through a sequence?",
                "choices": [
                    "A. if loop",
                    "B. for loop",
                    "C. else loop"
                ],
                "answer": "B"
            },
            {
                "question": "What is iteration?",
                "choices": [
                    "A. Ending a program",
                    "B. Displaying text",
                    "C. Repeating instructions"
                ],
                "answer": "C"
            }
        ]
    }
}


def show_chapter(number):
    chapter = chapters[number]

    print("\n" + "=" * 45)
    print(chapter["title"].upper())
    print("=" * 45)

    for lesson in chapter["lessons"]:
        print("\n- " + lesson)

    print("\nExample:")

    if number == "1":
        print("1. Start")
        print("2. Input two numbers")
        print("3. Add the numbers")
        print("4. Display the result")
        print("5. End")

    elif number == "2":
        print('print("Hello, World!")')

    elif number == "3":
        print("a = 5")
        print("b = 3")
        print("print(a + b)")

    elif number == "4":
        print('name = "Alex"')
        print("age = 18")
        print("print(name, age)")

    elif number == "5":
        print('name = input("Enter your name: ")')
        print('print("Hello", name)')

    elif number == "6":
        print("age = 18")
        print("if age >= 18:")
        print('    print("Adult")')
        print("else:")
        print('    print("Minor")')

    elif number == "7":
        print("for i in range(1, 4):")
        print("    print(i)")

    answer = input("\nDo you want to take the chapter quiz? (yes/no): ")

    if answer.lower() == "yes":
        take_quiz(number)


def take_quiz(number):
    chapter = chapters[number]
    score = 0

    print("\n--- CHAPTER QUIZ ---")

    for question_number, item in enumerate(chapter["questions"], start=1):
        print("\nQuestion", question_number)
        print(item["question"])

        for choice in item["choices"]:
            print(choice)

        user_answer = input("Your answer (A/B/C): ").upper().strip()

        if user_answer == item["answer"]:
            print("Correct! Great job!")
            score += 1
        else:
            print("Incorrect.")
            print("Correct answer:", item["answer"])

    print("\nYour final score:", score, "out of 3")

    if score == 3:
        print("Excellent! Perfect score!")
    elif score >= 2:
        print("Good job! Keep practicing!")
    else:
        print("Keep studying. You can do better!")


def main_menu():
    while True:
        print("\n" + "=" * 45)
        print("PYTHON LEARNING HUB - MAIN MENU")
        print("=" * 45)

        for number in chapters:
            print(number + ". " + chapters[number]["title"])

        print("0. Exit")

        choice = input("\nChoose a chapter (0-7): ").strip()

        if choice == "0":
            print("\nThank you for using Python Learning Hub!")
            print("Keep practicing, future coder,", name + "!")
            break

        elif choice in chapters:
            show_chapter(choice)

        else:
            print("Invalid choice. Please select from 0 to 7.")


main_menu()


