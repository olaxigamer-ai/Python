#bp is buying price
bp=float(input("please enter your buying price"))
#sp is selling price
sp=float(input("please enter your selling price"))
if(sp>bp):
    profit=sp-bp
    print("Profit=",profit)
else:
    loss=bp-sp
    print("Loss=",loss)