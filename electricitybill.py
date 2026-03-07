print("Electricity bill calculator. 1. if unit<50, cost=2.60, tax=25 2. 50<unit>100 cost=3.5 and tax=35 3. if 100<unit>200 cost=5.26 and tax=45, 4. if unit>200 cost=8.45 and tax=75")
unit=int(input("Please enter number of units you consumed."))
if unit<50:
    amount=unit*2.60
    tax=25
elif unit<=100:
    amount=130+((unit-50)*3.25)
    tax=35
elif unit<=200:
    amount=130+162.5+((unit-100)*5.26)
    tax=45
else:
    amount=130+162.50+526+((unit-200)*8.25)
    tax=75
total=amount+tax
print("\n electricity bill is =",total)
