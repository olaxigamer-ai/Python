class employ:

    def __init__(self):
        print("Employee created.")

    def __del__(self):
        print("Destructor called.")

def create_obj():
    print("Making object...")
    obj=employ()

print("Calling create object function...")
obj=create_obj()
print("Program End.")