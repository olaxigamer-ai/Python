temp=input("What temperature is it today?")
print("what is the weather like today? 1 is yes and 0 is no")
sun=input("Sunny?:")
rain=input("Rain?")
windy=input("windy?")

if temp>20 and sun==1:
    print("Wear loose clothes")
elif temp>20 and rain==1:
    print("wear loose clothes and a jacket")
elif temp<20 and rain==1:
    print("wear thick clothes and a jacket")
elif windy==1:
    print("wear a jacket.")
else:
    print("wear thick clothes")