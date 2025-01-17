import math

history = []

def cube_root(num):
    return num ** (1/3)

def cubic_formula():
    a = float(input("Please enter the value for A: "))
    b = float(input("Please enter the value for B: "))
    c = float(input("Please enter the value for C: "))
    d = float(input("Please enter the value for D: "))
    frac_1 = ((-b**3)/(27*a**3))
    frac_2 = ((b*c)/(6*a**2))
    frac_3 = (d/(2*a))
    frac_4 = (c/(3*a))
    frac_5 = ((b**2)/(9*a**2))
    frac_6 = (b/(3*a))
    result = cube_root((frac_1+frac_2-frac_3) + math.sqrt((frac_1+frac_2-frac_3)**2) + ((frac_4-frac_5)**3) + (frac_1+frac_2-frac_3) + math.sqrt((frac_1+frac_2-frac_3)**2) + ((frac_4-frac_5)**3) - frac_6)
    print('''
    The result for x is ''' + str(result) +'''
    ''')
    history.append("Cubic Formula: " + str(result))

def view_history():
    print('''
    '''+str(history)+'''
    ''')

def herons_formula():
    a = float(input("Please enter the value for A: "))
    b = float(input("Please enter the value for B: "))
    c = float(input("Please enter the value for C: "))
    s = (a+b+c)/2
    result = (s*(s-a)*(s-b)*(s-c)) ** (1/2)
    print('''
    The result is ''' + str(result) +'''
    ''')
    history.append("Heron's Formula: " + str(result))

def sphere_surface_area():
    r = float(input("Please enter the radius of the sphere: "))
    result = 4*math.pi*(r**2)
    print('''
    The result is ''' + str(result) +'''
    ''')
    history.append("Sphere Surface Area: " + str(result))

def quadratic_formula():
    a = float(input("Please enter the value for A: "))
    b = float(input("Please enter the value for B: "))
    c = float(input("Please enter the value for C: "))
    result = -b + math.sqrt((b**2)-(4*a*c)) / (2*a)
    result_2 = -b - math.sqrt((b**2)-(4*a*c)) / (2*a)
    print('''
    The result is ''' + str(result) +''' and ''' + str(result_2)+'''
    ''')
    history.append("Quadratic Formula: " + str(result) + ", " + str(result_2))

print("Welcome to the Second Formula Calculator!")
while True:
    choice = int(input('''What would you like to do?

    1. Cubic Formula
    2. Quadratic Formula
    3. Heron's Formula
    4. Surface Area of a Sphere
    5. View History

    '''))
    if choice == 1:
        cubic_formula()
    if choice == 2:
        quadratic_formula()
    if choice == 3:
        herons_formula()
    if choice == 4:
        sphere_surface_area()
    if choice == 5:
        view_history()
