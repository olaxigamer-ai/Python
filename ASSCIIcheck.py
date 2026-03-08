a=str(input("Enter your charachter."))
print("the ASII value is", ord(a))
print("The type of charachter entered is", type(a))

def is_uppercase_char(ch):
    return ch.isupper()
if is_uppercase_char(a):
        print(f"'{a}' is uppercase.")
else:
        print(f"'{a}' is not uppercase.")