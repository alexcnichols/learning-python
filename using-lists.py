spacelist = ["rocket", "planet", "asteroid", "alien"]
for x in range(0,2):
    print(spacelist[0])
    for item in spacelist:
        print(item)
    #spacelist[0] = "planet zarg"
    del spacelist[0]
    spacelist.append("moon")
print()
spacelist2 = ["space station", "star", "black hole"]
spacelistTogether = spacelist + spacelist2
for item in spacelistTogether:
    print(item)