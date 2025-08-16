from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.scrapethissite.com/pages/forms/")
contents = response.text

soup = BeautifulSoup(contents,"html.parser")

title = soup.find(name="h1")
if title.small:
   title.small.decompose()
table = soup.find_all(name="tr",class_="team")
title = title.getText().replace("\n","")
print(title)
YEAR = 1990
team_names = []
team_wins = []
team_losses = []
text_file = open(f"Hockey_Teams_Data_{YEAR}.txt","w")
text_file.write(f"{title}")
text_file.write("\n")
text_file.write("\n")
max_wins = 0
max_losses = 100

for teams in table:
    if int(teams.find(class_="year").getText().replace("\n","").replace(" ","")) == YEAR:
        name= teams.find(class_="name").getText().replace("\n","").replace("  ","")
        team_names.append(name)
        wins = int(teams.find(class_="wins").getText().replace("\n","").replace(" ",""))
        team_wins.append(wins)
        losses = int(teams.find(class_="losses").getText().replace("\n","").replace(" ",""))
        team_losses.append(losses)
        text_file.write(f"{name} had {wins} wins and {losses} losses.")
        text_file.write("\n")
        if wins > max_wins:
            max_wins = wins
        if losses < max_losses:
            max_losses = losses

print(team_names)
print(team_wins)
print(team_losses)
max_winner = team_names[(team_wins.index(max_wins))]
max_loser = team_names[(team_losses.index(max_losses))]
print(max_loser+"   "+max_winner)

text_file.write("\n")
text_file.write("\n")
text_file.write(f"In this year {max_winner} has won the most number of games with a total of {max_wins} wins and \n"
                f"{max_loser} suffered the most losses in the year with {max_losses} matches lost.")
