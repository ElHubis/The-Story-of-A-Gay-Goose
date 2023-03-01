
name = input ("Please Choose A Name ")
if name == (""):
    name = ("Bob")
name_confirmation = ["Yes","No", "yes", "no"] 
print("Doth thy wish to henceforth be known by thy name", name, "?")
userInput = ""
while userInput not in name_confirmation:
    print("Yes/No")
    userInput = input()
    if userInput not in name_confirmation:
        print("We Literally Gave You Two Options, And You Still Failed")
        continue

