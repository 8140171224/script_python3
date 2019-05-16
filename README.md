# script_python3
basic_to_high

# copy_past_twofiles.py 	

    from sys import argv
    from os.path import exists


    script, from_file, to_file = argv

    print(f"Copying from {from_file} to {to_file}")

    # we could to these two on one line, how?
    in_file = open(from_file)
    in_data = in_file.read()

    print(f"The input file is {len(in_data)} bytes long")

    print(f"Does the output file exist? {exists(to_file)}")
    print("Read, hit RETURN  to continue, CTRL+C  to abort")
    input()

    out_file = open(to_file, 'w')
    out_file.write(in_data)

    print("Alright, all done.")

    out_file.close()
    in_file.close()
    
    
#	def_fun_script.py 	

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
    
    
 # file_text_edit_script.py 	

    from sys import argv

    script, input_file = argv

    def print_all(f):
        print(f.read())

    def rewind(f):
        f.seek(0)

    def print_a_line(line_count, f):
        print(line_count, f.readline())

    current_file = open(input_file)

    print("First let's print the wiole file:\n")

    print_all(current_file)

    print("Now let's rewind, kind of line a tape.")

    rewind(current_file)

    print("Let's print three lines:")

    current_line = 1
    print_a_line(current_line, current_file)

    current_line = current_line + 1
    print_a_line(current_line, current_file)

    current_line = current_line + 1
    print_a_line(current_line, current_file)
    
    
#	fun_var_script.py

    def cheese_and_crackers(cheese_count, boxes_of_crackers):
        print(f"You have {cheese_count} cheeses!")
        print(f"You have {boxes_of_crackers} boxes of creackers")
        print("Men that's enough for a party!")
        print("Get a blacket.\n")


    print("we can just give the function numbers directly:")
    cheese_and_crackers(20, 30)


    print("OR, we can use variable for our script:")
    amount_of_chesse = 10
    amount_of_crackers = 50


    cheese_and_crackers(amount_of_chesse, amount_of_crackers)

    print("we can even do math inside too:")
    cheese_and_crackers(10 + 20, 5 + 6)

    print("And we can combine the two, variables and math:")
    cheese_and_crackers(amount_of_chesse + 100, amount_of_crackers + 1000)
    
#	get_input_script.py

    from sys import argv

    script, user_name = argv 
    prompt = '>'
    print(f"Hi {user_name} T'm the {script} script.")
    print("I'd like to ask you a few questions.")

    print(f"Do you like me {user_name}") 
    likes = input(prompt)

    print(f"Where do you live {user_name}?")
    lives = input(prompt)

    print("What kind of computer do you have?")
    computer = input(prompt)

    print(f'''
    Alright so you said {likes} about me like me.
    You live in {lives}. Not sure where that is.
    And you  have a {computer}. Nice.
    ''')
# open&read_file_script.py

    from sys import argv

    script, filename = argv

    txt = open(filename) 

    print(f"Here's your file name {filename}:\n\n\n\n\n\n\n")
    print(txt.read())

    print("Type the filename again:\n\n\n")
    file_again = input('> ')

    txt_again = open(file_again)

    print(txt_again.read())
    
#	sum_puzzle_script.py


    def add (a, b):
        print(f"ADDING {a} + {b}")
        return a + b

    def subtract(a, b):
        print(f"SUBTRACTING {a} - {b}")
        return a - b

    def multiply(a, b):
        print(f"MULTIPLYING {a} * {b}")
        return a * b

    def divide(a, b):
        print(f"DIVIDING {a} / {b}")
        return a / b

    print("Let's do some math with just functions!")

    age = add(30, 5)
    height = subtract(78, 4)
    weight = multiply(90, 2)
    iq = divide(100, 2)

    print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

    # A puzzle for the extra credit, type it in anyway.
    print("here is a puzzle.")

    what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

    print("That becomes: ", what, "Can you do it by hand?")
    
    
#	write_in_file_script.p

    from sys import argv 
    script, filename = argv

    print(f"We're going to erase {filename}.")
    print("If you don't want that, hit CTRL+C (>C)")
    print("If you do want that,hit RETURN.")

    input('?')

    print("Opening the file... ")
    target = open(filename, 'w')

    print("Truncating the file. Goodbey!")
    target.truncate()

    print("Now I', going to ask you for three lines.")

    line1 = input("line 1: ")
    line2 = input("line 2: ")
    line3 = input("line 3: ")

    print("I'm going to write there to the file.")

    target.write(line1)
    target.write('\n')
    target.write(line2)
    target.write('\n')
    target.write(line3)

    print("And finally , we close it.")
    target.close()
