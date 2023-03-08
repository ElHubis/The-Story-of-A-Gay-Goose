def intro():
    wake_up_options = ["1", "2", "3"]
    print("What Do You Wake Up To:")
    userInput = ""
    while userInput not in wake_up_options:
        print("1.Ash And Dust \n2.Nothing \n3.Boyfriend")
        userInput = input()
        if userInput == "1":
            print("\n \n \n")       
            wasteland()
        elif userInput == "2":
            print("\n \n \n")  
            void()
        elif userInput == "3":
            print("\n \n \n")
            breakfast()  
        else:
            print("Please Choose One Of The Numbers")

def wasteland():
    wasteland_options = ["1", "2", "3"]
    print("You Wake Up On The Ground, Surrounded By Radioactive Wastelands.")
    print("Next To You Is A Banana(Lots Of Calories).")
    print("Standing In Front Of You Is A Man, Asking You To Join Ceasar.")
    print("What Do You Do?")
    userInput = ""
    while userInput not in wasteland_options:
        print("1.Refuse To Join Ceasar. \n2.Eat The Banana. \n3.Go Back To Sleep")
        userInput = input()
        if userInput == "1":
            print("When you refuse to join, the man picks you up by the neck and drags you with him. He brings you to a cross and get crusified")
            print("You Die")
            print("\n \n \n")       
            wasteland()
        elif userInput == "2":
            print("\n \n \n")  
            void()
        elif userInput == "3":
            print("\n \n \n")
            breakfast()  
        else:
            print("Please Choose One Of The Numbers")
def void():
    wake_up_options = ["1", "2", "3"]

def breakfast():
    wake_up_options = ["1", "2", "3"]

name = input ("Please Choose A Name ")
if name == (""):
    name = ("Bob")
name_confirmation = ["Yes","No", "yes", "no"] 
print("Doth thy wish to henceforth be known by the name", name, "?")
userInput = ""
while userInput not in name_confirmation:
    print("Yes/No")
    userInput = input()
    if userInput == "Yes" or userInput == "yes":
        print("Game Start \n \n \n \n")       
        intro()
    elif userInput == "No" or userInput =="no":
        print("Well i guess you don't wanna play. Game Over")
    else:
        print("We Literally Gave You Two Options, And You Still Failed")
