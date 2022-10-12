"""
Lookup hex values for dictionary of colours.
"""
COLOUR_TO_HEX = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                 "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                 "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                 "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                 "aquamarine4": "#458b74", "azure1": "#f0ffff"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    if colour_name not in COLOUR_TO_HEX:
        print("Invalid colour name")
    else:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    colour_name = input("Enter a colour name: ")
