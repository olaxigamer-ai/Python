def tip(bill_amount,tip_perc):
    total=bill_amount+((tip_perc/100)*bill_amount)
    total=round(total,2)
    print("total amount to pay is", total)
tip(500,5)