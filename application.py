import constants

def clean_data(players):
    cleaned = players
    for player in cleaned:
        num_height = player['height'].split(" ") 
        player['height'] =  int(num_height[0])
        player['experience'] =  player['experience'].upper == "YES"
    return cleaned

player_list = clean_data(constants.PLAYERS)

max_members = len(constants.PLAYERS) / len(constants.TEAMS)
teams = constants.TEAMS


def balance_teams(teams):
    team_stats = []
    team_roster = {'Team' : '', 'Players': "", "Total Players": 0}
    for team in teams:
        for player in player_list:
            if team_roster['Total Players'] < max_members:
                team_roster['Team'] = team + " Stats"
                if team not in player:
                    player[team] = team
                    team_roster['Players'] += player['name'] + ", " 
                    team_roster['Total Players'] += 1
            else:
                team_stats.append(team_roster)
                team_roster =  {'Team' : '', 'Players': "", "Total Players": 0}
                

    return team_stats     

teams_list = balance_teams(teams)
    
def show_stats(teamlist, i):
    team_stat = teams_list[i]
    return(
        f"""
        Team: {team_stat['Team']}
        ---------------------------
        Total Players: {team_stat['Total Players']}
        ---------------------------
        Players on Team:
            {team_stat['Players']}

        """
    )
team1 = show_stats(teams_list, 0)
team2 = show_stats(teams_list, 2)
team3 = show_stats(teams_list, -1)



print("Welcome!\n\nBASKETBALL TEAM STATS TOOL\n")
print("\n----MENU----\n\n")
while True:
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
            print(team1)
            input("Press enter to continue...")
        elif answer2.lower() == "b":
            print(team2)
            input("Press enter to continue...")
        elif answer2.lower() == "c":
            print(team3)
            input("Press enter to continue...")
        else:
            print("Not a valid choice")
    elif answer.lower() == "b":
        print("Thanks for using my app")
        break
