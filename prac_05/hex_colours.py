"""
Lookup hex values for dictionary of colours.
"""
COLOUR_TO_HEX = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                 "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                 "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                 "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                 "aquamarine4": "#458b74", "azure1": "#f0ffff"}

lowercase_colours_to_hex = {key.lower(): value for key, value in COLOUR_TO_HEX.items()}
colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    if colour_name not in lowercase_colours_to_hex:
        print("Colour not found")
    else:
        print(f"{colour_name} is {lowercase_colours_to_hex[colour_name]}")
    colour_name = input("Enter a colour name: ").lower()
