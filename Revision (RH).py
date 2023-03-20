import random

subjectchoice = input("Which subject would you like to revise? (Maths, science, english, history, french and computer science) ").capitalize()

if subjectchoice == "Maths":
    topic = input("Which topic would  you like to revise? You can choose from Shapes, Loci, Problem Solving, Fractions and Co-Ordinates.").capitalize()
    if topic == "Shapes"
        a = random.randint(1,100)
        b = random.randint(1,100)
        c = random.randint(1,100)
        d = int(a) + int(b)
        answer = int(d) / int(2) * int(c)
        a = str(a)
        b = str(b)
        c = str(c)
        answer = float(answer)
        giveanswer = float(input("The trapezium has parallel sides of "+a+"cm and "+b+"cm with a height of "+c+"cm. What is the area of the trapezium? "))
        giveanswer = str(giveanswer)
        print("Your answer was "+giveanswer".")
        if giveanswer == answer + "cm":
            print("1")
        else:
            print("2")
#elif subjectchoice == "Science":
#    print("1")
#elif subjectchoice == "History":
#    print("2")
#elif subjectchoice == "French":
#    print("3")
#elif subjectchoice == "Computer Science":
#    print("4")
