# a program that asks users for inputs. Uses the inputs to update a pre-written story.

text = "I am a programmer. I have been programming for 5 years. I am a student at the department of Systems \
    Engineering, University of Lagos."

profession = input("What do you do? ")
verb = input("Type in any verb")
years = input("Type in a number")
course = input("What is your course of study? ")

print(f"I am a {profession}. I have been {verb} for {years} years. I am a student at the department of {course} University of Lagos.")