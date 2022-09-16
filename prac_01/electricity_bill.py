"""
CP1404/CP5632 - Practical 1
Programs to estimate an electricity bill over a period of days.
"""

# print("Electricity bill estimator 1.0")
# price = float(input("Price per kWh in cents: "))
# usage = float(input("Daily use in kWh: "))
# days = int(input("Number of days in the billing period: "))
# bill = (price * usage * days)/100
# print(f"Estimated bill: ${bill:.2f}")

TARIFF_11 = 0.244618  # price in $
TARIFF_31 = 0.136928  # price in $

print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
while tariff not in (11, 31):
    print("Invalid tariff!")
    tariff = int(input("Which tariff? 11 or 31: "))
if tariff == 11:
    PRICE = TARIFF_11
else:
    PRICE = TARIFF_31
usage = float(input("Daily use in kWh: "))
days = int(input("Number of days in the billing period: "))
bill = (PRICE * usage * days)
print(f"Estimated bill: ${bill:.2f}")
