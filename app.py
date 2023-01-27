import application

print("Welcome!\n\nBASKETBALL TEAM STATS TOOL\n")
print("\n----MENU----\n\n")

print(
"""
Here are your choices:
    A) Display Team Stats
    B) Quit
"""
)
answer = input("Enter an option: ")

if answer.lower() == "a":
    print(
        """
        A) Panthers
        B) Bandits
        C) Warriors  
        """
    )
    answer2 = input("Enter an option: ")
    if answer2.lower() == "a":
         print(application.show_stats(application.teams_list, 0))
    elif answer2.lower() == "b":
        print(application.show_stats(application.teams_list, 0))
    elif answer2.lower() == "c":
        print(application.show_stats(application.teams_list, 0))
    else:
        print("Not a valid choice")
