import math

history = []



def cubic_formula():
    a = int(input("Please enter the value for A: "))
    b = int(input("Please enter the value for B: "))
    c = int(input("Please enter the value for C: "))
    d = int(input("Please enter the value for D: "))
    frac_1 = ((-b**3)/(27*a**3))
    frac_2 = ((b*c)/(6*a**2))
    frac_3 = (d/(2*a))
    frac_4 = (c/(3*a))
    frac_5 = ((b**2)/(9*a**2))
    frac_6 = (b/(3*a))
    result = cube_root((frac_1+frac_2-frac_3) + math.sqrt((frac_1+frac_2-frac_3)**2) + ((frac_4-frac_5)**3) + (frac_1+frac_2-frac_3) + math.sqrt((frac_1+frac_2-frac_3)**2) + ((frac_4-frac_5)**3) - frac_6)
    print('''
    The result is ''' + str(result) +'''
    ''')
    history.append("Cubic Formula: " + str(result))

def view_history():
    print('''
    '''+str(history)+'''
    ''')

def cube_root(num):
    return num ** (1/3)

print("Welcome to the Cubic Formula Calculator!")
while True:
    choice = int(input('''What would you like to do?

    1. Cubic Formula
    2. View History

    '''))
    if choice == 1:
        cubic_formula()
    if choice == 2:
        view_history()