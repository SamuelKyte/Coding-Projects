hero = "Super Man"
print(hero[0].upper() + '^' + hero[1].upper() + '^' + hero[2].upper() + '^' + hero[3].upper() + '^' +hero[4].upper() + '^' + hero[6].upper() + '^' + hero[7].upper() + '^' + hero[8].upper())
print("")
#got curious and wanted to seperate each letter so I found some extra information on: https://www.geeksforgeeks.org/iterate-over-characters-of-a-string-in-python/
for i, v in enumerate(hero.upper()):
  print(v)
  
  print(" ")
print(hero[0:5].upper() + hero[6:9].upper())
print(hero.upper()[0:10])
print(hero.upper()[::-1])