# List
# You have a list of superheroes representing the Justice League.
justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
print(justice_league)

# 1. Calculate the number of members in the Justice League
print(f"Number of members in the Justice League is {len(justice_league)}")

# 2. Batman recruited Batgirl and Nightwing as new members.
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

# 3. Wonder Woman is now the leader of the Justice League.
# Move her to the beginning of the list.
wonder_woman_index = justice_league.index("Wonder Woman")
wonder_woman = justice_league.pop(wonder_woman_index)
leader = justice_league.insert(0,wonder_woman)
print(justice_league)

# 4. Aquaman and Flash are having conflicts, and you need to separate them.
# Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.
green_lantern_index = justice_league.index('Green Lantern')
green_lantern = justice_league.pop(green_lantern_index)
justice_league.insert(justice_league.index('Aquaman'),green_lantern)
print(justice_league)

# 5. The Justice League faced a crisis, and Superman decided to assemble a new team.
# Replace the existing list with the following new members:
# "Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow".
justice_league = ["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]
print(justice_league)

# 6. Sort the Justice League alphabetically. The hero at the 0th
# index will become the new leader.
justice_league.sort()
print(justice_league)