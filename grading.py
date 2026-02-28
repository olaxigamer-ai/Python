print("enter marks obtained in 5 subjects out of 100")
maths=float(input("math"))
science=float(input("science"))
english=float(input("english"))
spanish=float(input("spanish"))
german=float(input("german"))
total=maths+science+english+spanish+german
percent=(total/500)*100
if percent>=91 and percent<=100:
    print("your grade is A1")
elif percent>=81 and percent<=91:
    print("your grade is A2")
elif percent>=71 and percent<=81:
    print("your grade is B1")
elif percent>=61 and percent<=71:
    print("your grade is B2")
elif percent>=51 and percent<=61:
    print("your grade is C1")
elif percent>=41 and percent<=51:
    print("your grade is C2")
elif percent>=31 and percent<=41:
    print("your grade is D1")
elif percent>=21 and percent<=31:
    print("your grade is D2")
elif percent>=11 and percent<=21:
    print("your grade is E1")
elif percent>=0 and percent<=11:
    print("your grade is E2")
else:
    print("invalid input!")