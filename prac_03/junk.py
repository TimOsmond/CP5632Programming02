# """
# Read CSV
# """
# with open("guitars.txt") as in_file:
#     for line in in_file:
#         #print(line)
#         parts = line.split(",")
#         name = parts[0]
#         date = int(parts[1])
#         price = float(parts[2])
#         #print(parts)
#         print(f"{name} was made in {date} and costs ${price:,.2f}")
# in_file.close()

# filename = input("Filename: ")
# with open(filename) as in_file:
#     for line in in_file:
#         if line[0] == "#":
#         # or if line.startswith("#"):
#             print(line.strip())

# s = "\tPython, Monty   \n"
# print(s[1], ".", sep="")
# print(s.strip(), ".", sep="")
# s.replace(" ", "*")
# print(s.lstrip(), ".", sep="")
# print(s.strip().split(","))

# name = input("Name: ")
# with open("name.txt", "w") as out_file:
#     print(name, file=out_file)

names_string = ["a", "b", "c"]
for string in names_string:
    with open(string + ".txt", "w") as out_file:
        print(string, file=out_file)

