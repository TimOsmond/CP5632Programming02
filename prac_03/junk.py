"""
Read CSV
"""
with open("guitars.txt") as in_file:
    for line in in_file:
        #print(line)
        parts = line.split(",")
        name = parts[0]
        date = int(parts[1])
        price = float(parts[2])
        #print(parts)
        print(f"{name} was made in {date} and costs ${price:,.2f}")
in_file.close()
