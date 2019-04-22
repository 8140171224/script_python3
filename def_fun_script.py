# This ine is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2 : {arg2}")

# Ok, that *args is achully pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no argument
def print_none():
    print("I got nothing'.")

print_two("aakash", "padhiyar")
print_two_again("dhaval", "padhiyar")
print_one("first!")
print_none()
