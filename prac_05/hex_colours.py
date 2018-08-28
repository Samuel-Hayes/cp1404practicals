COLOURS = {"AliceBlue": "#f0f8ff", "black": "#000000", "blue1": "#0000ff", "red1": "#ff0000", "RoyalBlue": "#4169e1",
           "SaddleBrown": "#8b4513", "tan": "#d2b48c", "tomato1": "#ff6347", "violet": "#ee82ee", "wheat": "#f5deb3"}

colour = input("Enter colour name: ")
while colour != "":
    if colour in COLOURS:
        print(colour, "is", COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ")
