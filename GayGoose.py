import time

def start():
    name = input ("Please Choose A Name ")
    if name == ("") or name != ("Bob"):
        name = ("Bob")
    name_confirmation = ["Yes","No", "yes", "no"] 
    print("Doth Thy Wish To Henceforth Be Known By The Name", name, "?")
    userInput = ""
    while userInput not in name_confirmation:
        print("Yes/No")
        userInput = input()
        if userInput == "Yes" or userInput == "yes":
            print("Game Start \n \n \n \n")       
            intro()
        elif userInput == "No" or userInput =="no":
            print("Yes You Do")
            print("Game Start \n \n \n \n")  
            intro()
        else:
            print("We Literally Gave You Two Options, And You Still Failed")

def intro():
    wake_up_options = ["1", "2", "3"]
    print("What Do You Wake Up To:")
    time.sleep(2)
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
    time.sleep(2)
    print("Next To You Is A Banana(Lots Of Calories).")
    time.sleep(2)
    print("Standing In Front Of You Is A Man, Asking You To Join Ceasar.")
    time.sleep(2)
    print("What Do You Do?")
    time.sleep(2)
    userInput = ""
    while userInput not in wasteland_options:
        print("1.Refuse To Join Ceasar. \n2.Eat The Banana. \n3.Go Back To Sleep")
        userInput = input()
        if userInput == "1":
            print("When You Refuse To Join, The Man Picks You Up By The Neck And Drags You With Him. He Brings You To A Cross And Get Crusified")
            time.sleep(3)
            print("You Die")
            time.sleep(2) 
            print("\n \n \n")
            wasteland()
        elif userInput == "2":
            print("You Decide To Ignore The Man And Instead Eat The Banana")
            time.sleep(2)
            print("The Banana Contained A ¡LOT! Of Calories Due To Its Unexpected Trace Amounts (Massive) Of Uranium")
            time.sleep(2)
            print("Due To A Gram Of Uranium Containing 20 000 000 000 Calories, You Die")
            time.sleep(2)
            print("You're Dead")
            time.sleep(2)
            print("\n \n \n")  
            wasteland()
        elif userInput == "3":
            print("You Decide That You Are Not Dealing With This Shit And Go Back To Sleep")
            time.sleep(2)
            print("\n \n \n")
            breakfast()  
        else:
            print("Please Choose One Of The Numbers")
def void():
    void_options = ["1", "2", "3"]
    print("You Open Your Eyes And You're Unsure If You've Even Opened Them")
    time.sleep(2)
    print("You Look Around And See Nothing But Darkness, Though There Might Not Even Be Darkness")
    time.sleep(2)
    print("Then, Booming And Loud, Filling The Infinite Plane You Find Yourself In, You Hear The Voice Of Jod")
    time.sleep(2)
    print("'Young One' The Voice Says. 'I sense Greatness Within You' It Continues")
    time.sleep(2)
    print("'I Offer You The Position Of Jod, Will You Take My Place As Ruler Of The Universe'")
    time.sleep(2)
    userInput = ""
    while userInput not in void_options:
        print("1.Become Jod. \n2.Travel Until You Find Something. \n3.Join With The Void")
        userInput = input()
        if userInput == "1":
            print("'Then Child, I Will Grant The Powers Of Jod'")
            time.sleep(2)
            print("You Feel Unlimited Power Flow Through Your Veins")
            time.sleep(2)
            print("You Proceed To Create The World Acording To Your Most Perfect Image")
            time.sleep(2)
            print("With Geese At The Top Of Food Chain, Geese Proceed To Take Over The World")
            time.sleep(2)
            print("You Have Created The Greatest Reality For Geese-Kind, You Win")
            time.sleep(2)
            print("\n \n \n") 
            intro()
        elif userInput == "2":
            print("You Travel Without Finding Something And Eventually Starve To Death")
            time.sleep(2)
            print("\n \n \n")  
            void()
        elif userInput == "3":
            print("The Voice Of Jod Somehow Begins To Fade Into The Distance Until It Dissapears Completely")
            time.sleep(2)
            print("Though You Can't See It, You Feel The Darkness Creeping Ever Closer")
            time.sleep(2)
            print("When The Darkness Reaches You It Enters You And Becomes You")
            time.sleep(2)
            print("You Are The Void And The Void Is You")
            time.sleep(2)
            print("You See Everything And Know Everything")
            time.sleep(2)
            print("You Are Everything, Everwhere, All At Once")
            time.sleep(2)
            print("Despite This, There Is Still One Question You Can Not Answer")
            time.sleep(2)
            print("'Why Is The Goose Gay?'")
            time.sleep(2)
            print("Why Don't You Take A Gander")
            time.sleep(2)
            print("\n \n \n")
            goose_gay()  
        else:
            print("Please Choose One Of The Numbers")

def goose_gay():
    question_options = ["1", "2", "3"]
    userInput = ""
    while userInput not in question_options:
        print("1.He Loves Alejandro. \n2.He Likes Thick Necks \n3.He Enjoys Beautiful Feathers.")
        userInput= input()
        if userInput == "1":
            print("That Is Not Your Boyfriends Name. Who Is Alejandro?")
            time.sleep(2)
            print("You Cheating Bastard")
            time.sleep(2)
            print("\n \n \n")
            breakfast()
        elif userInput == "2":
            print("Respectable Answer")
            time.sleep(2)
            print("\n \n \n")
            breakfast_2()
        elif userInput == "3":
            print("That's What You Liked About Your Ex")
            time.sleep(2)
            print("Your Boyfriend Is Not Your Ex")
            time.sleep(2)
            print("What The Fuck Dude")
            time.sleep(2)
            print("\n \n \n")
            breakfast()
        else:
            print("Please Choose One Of The Numbers")
            
def breakfast():
    breakfast_options = ["1", "2", "3"]
    print("You Open Your Eyes And See A Breakfast Tray In Front Of You")
    time.sleep(2)
    print("On The Tray There Are Some Perfectly Cooked Eggs, A Plate Of Pancakes And A Bowl Of Fruit")
    time.sleep(2)
    print("Your Beautiful Boyfriend Has Made You Breakfast In Bed")
    time.sleep(2)
    print("The Handsom Man Himself Is Sitting Next To You In Bed, Looking Into Your Eyes With Burning, But Controlled, Passion")
    time.sleep(2)
    print("What Do You Do")
    time.sleep(2)
    userInput = ""
    while userInput not in breakfast_options:
        print("1.Eat Some Eggs. \n2.Eat A Pancake \n3.Feed Eachother Fruit")
        userInput = input()
        if userInput == "1":
            print("You Eat The Eggs And Realise You've Become A Cannibal")
            time.sleep(2)
            print("Fuck")
            time.sleep(1)
            print("\n \n \n")       
            breakfast()
        elif userInput == "2":
            print("You Eat A Pancake While Looking At Your Boyfriend")
            time.sleep(2)
            print("The Pancakes Are Perfect")
            time.sleep(2)
            print("Life Is Good")
            time.sleep(2)
            print ("Congratulations, You Enjoyed A Nice Breakfast With Your Boyfriend")
            time.sleep(2)
            print("Now Do It Again")
            time.sleep(2)
            print("\n \n \n")  
            start()
        elif userInput == "3":
            print("You Feed Eachother The Fruit And It's A Magical Moment")
            time.sleep(2)
            print("You Decide To Go On A Vacation")
            time.sleep(2)
            print("Congratulations, You Spent A Fantastic Week With Your Boyfriend In Paris, Eating Lots Of Well-Done Steak As Well As Blowing Up The Eifel Tower")
            time.sleep(4)
            print("Now Do It Again")
            time.sleep(2)
            print("\n \n \n")
            start()  
        else:
            print("Please Choose One Of The Numbers")    

def breakfast_2():
    breakfast_2_options = ["1", "2", "3", "4"]
    print("You Open Your Eyes And See A Breakfast Tray In Front Of You")
    time.sleep(2)
    print("On The Tray There Are Some Perfectly Cooked Eggs, A Plate Of Pancakes And A Bowl Of Fruit")
    time.sleep(2)
    print("Your Beautiful Boyfriend Has Made You Breakfast In Bed")
    time.sleep(2)
    print("The Handsom Man Himself Is Sitting Next To You In Bed, Looking Into Your Eyes With Burning, But Controlled, Passion")
    time.sleep(2)
    print("What Do You Do")
    time.sleep(2)
    userInput = ""
    while userInput not in breakfast_2_options:
        print("1.Eat Some Eggs. \n2.Eat A Pancake \n3.Feed Eachother Fruit \n4.Take Your Boyfriend On A Date")
        userInput = input()
        if userInput == "1":
            print("You Eat The Eggs And Realise You've Become A Cannibal")
            time.sleep(2)
            print("Fuck")
            time.sleep(1)
            print("\n \n \n")       
            breakfast()
        elif userInput == "2":
            print("You Eat A Pancake While Looking At Your Boyfriend")
            time.sleep(2)
            print("The Pancakes Are Perfect")
            time.sleep(2)
            print("Life Is Good")
            time.sleep(2)
            print ("Congratulations, You Enjoyed A Nice Breakfast With Your Boyfriend")
            time.sleep(2)
            print("Now Do It Again")
            time.sleep(2)
            print("\n \n \n")  
            start()
        elif userInput == "3":
            print("You Feed Eachother The Fruit And It's A Magical Moment")
            time.sleep(2)
            print("You Decide To Go On A Vacation")
            time.sleep(2)
            print("Congratulations, You Spent A Fantastic Week With Your Boyfriend In Paris, Eating Lots Of Well-Done Steak As Well As Blowing Up The Eifel Tower")
            time.sleep(2)
            print("Now Do It Again")
            time.sleep(2)
            print("\n \n \n")
            start()  
        elif userInput == "4":
            print("You're Grateful For The Wonderful Breakfast, Handmade From Scratch By Your Beautiful Boyfriend")
            time.sleep(2)
            print("You Decide To Ask Him On A Date. Your Treat")  
            time.sleep(2)
            print("In The Evening You Have A Wonderful Date, And At The End Of The Night Your Boyfriend Propeses")
            time.sleep(2)
            print("You Say Yes And You Have The Wedding And Life Of Your Dreams")
            time.sleep(2)
            print("Congratulations, Your Boyfriend Is Now Your Husband")
            time.sleep(2)
            print("Now Do It Again")
            time.sleep(2) 
            print("\n \n \n")
            start()  
        else:
            print("Please Choose One Of The Numbers")

start()