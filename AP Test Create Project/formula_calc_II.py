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
    The results are ''' + str(result) +'''
    ''')
    history.append("Cubic Formula: " + str(result))

def view_history(num):
    if num == "ALL":
        for item in range(len(history)):
            print('''
                ''' + str(history[item - 1]))
    elif num > len(history):
        print('''
        There aren't that many entries in the session history.
        ''')
    elif len(history) == 0:
        print('''  
        There is no History to view.
        ''')
    else:
        for item in range(num):
            if item == num:
                break
            else:
                print('''
                '''+str(history[item - 1]))
        print(" ")

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

def sphere_surface_area(r):
    result = 4*math.pi*(r**2)
    print('''
    The result is ''' + str(result) +'''
    ''')
    history.append("Sphere Surface Area: " + str(result))

def quadratic_formula():
    a = float(input("Please enter the value for A: "))
    b = float(input("Please enter the value for B: "))
    c = float(input("Please enter the value for C: "))
    if (b**2)-(4*a*c) < 0:
        print('''
        This has no zeros.
        ''')
    else:
        result = -b + math.sqrt((b**2)-(4*a*c)) / (2*a)
        result_2 = -b - math.sqrt((b**2)-(4*a*c)) / (2*a)
        print('''
        The results are ''' + str(result) +''' and ''' + str(result_2)+'''
        ''')
        history.append("Quadratic Formula: " + str(result) + ", " + str(result_2))

def quartic_formula():
    a = float(input("Please enter the value for A: "))
    b = float(input("Please enter the value for B: "))
    c = float(input("Please enter the value for C: "))
    d = float(input("Please enter the value for D: "))
    the_big_one = (2*(b**3)) - (9*a*b*c) + (27*(c**2)) + (27*(a**2)*d) - (72*b*d) + math.sqrt(-4*( ( (b**2) - (3*a*c) + (12*d) )**3) + ( ( (2*(b**3)) - (9*a*b*c) + (27*(c**2)) + (27*(a**2)*d) - (72*b*d)))**2)**(1/3)
    if (-4*(((b**2)-(3*a*c)+(12*d))**3)+(((2*(b**3))-(9*a*b*c)+(27*(c**2))+(27*(a**2)*d)-(72*b*d)))**2) < 0 or ( ( ((-a**2)/2) - ((2*b)/3) + ( ( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d)) ) / 3 * (the_big_one) ) + (the_big_one / (32**(1/3)) )) - (1/2) * ( ((-a**2)/2) - ((4*b)/3) + (( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d))) / 3 * the_big_one ) - (the_big_one/(32**(1/3))) - ((-a**3)) + (4*a*b) - (8*c) / 4)) < 0 or (((-a**2)/2) - ((2*b)/3) + ( ( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d)) ) / 3 * (the_big_one) ) + (the_big_one / (32**(1/3)) )) < 0:
        print('''
        This has no zeros.
        ''')
    else:
        result1 = ((-a/4) - 0.5 * math.sqrt( ( ((-a**2)/2) - ((2*b)/3) + ( ( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d)) ) / 3 * (the_big_one) ) + (the_big_one / (32**(1/3)) )) - (1/2) * math.sqrt(( ((-a**2)/2) - ((4*b)/3) + (( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d))) / 3 * the_big_one ) - (the_big_one/(32**(1/3))) - ((-a**3)) + (4*a*b) - (8*c)) / (4 * math.sqrt(( ((-a**2)/2) - ((2*b)/3) + ( ( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d)) ) / 3 * (the_big_one) ) + (the_big_one / (32**(1/3)) )))))))
        result2 = ((-a/4) - 0.5 * math.sqrt( ( ((-a**2)/2) - ((2*b)/3) + ( ( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d)) ) / 3 * (the_big_one) ) + (the_big_one / (32**(1/3)) )) + (1/2) * math.sqrt(( ((-a**2)/2) - ((4*b)/3) + (( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d))) / 3 * the_big_one ) - (the_big_one/(32**(1/3))) - ((-a**3)) + (4*a*b) - (8*c)) / (4 * math.sqrt(( ((-a**2)/2) - ((2*b)/3) + ( ( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d)) ) / 3 * (the_big_one) ) + (the_big_one / (32**(1/3)) )))))))
        result3 =((-a/4) - 0.5 * math.sqrt( ( ((-a**2)/2) - ((2*b)/3) + ( ( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d)) ) / 3 * (the_big_one) ) + (the_big_one / (32**(1/3)) )) - (1/2) * math.sqrt(( ((-a**2)/2) - ((4*b)/3) + (( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d))) / 3 * the_big_one ) - (the_big_one/(32**(1/3))) + ((-a**3)) + (4*a*b) - (8*c)) / (4 * math.sqrt(( ((-a**2)/2) - ((2*b)/3) + ( ( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d)) ) / 3 * (the_big_one) ) + (the_big_one / (32**(1/3)) )))))))
        result4 = ((-a/4) - 0.5 * math.sqrt( ( ((-a**2)/2) - ((2*b)/3) + ( ( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d)) ) / 3 * (the_big_one) ) + (the_big_one / (32**(1/3)) )) + (1/2) * math.sqrt(( ((-a**2)/2) - ((4*b)/3) + (( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d))) / 3 * the_big_one ) - (the_big_one/(32**(1/3))) + ((-a**3)) + (4*a*b) - (8*c)) / (4 * math.sqrt(( ((-a**2)/2) - ((2*b)/3) + ( ( (2**(1/3)) * ((b*2) - (3*a*c) + (12*d)) ) / 3 * (the_big_one) ) + (the_big_one / (32**(1/3)) )))))))
        print('''
        The results are ''' + str(result1) + ',' + str(result2) + ',' +str(result3) + ', and ' + str(result4) + '''
        ''')
        history.append("Quartic Formula: " + str(result1) + ',' + str(result2) + ',' +str(result3) + ', and ' + str(result4))

def pythagorean_theorem():
    a = float(input("Please enter the value for A: "))
    b = float(input("Please enter the value for B: "))
    result = math.sqrt((a**2)+(b**2))
    print('''
    The result is ''' + str(result), "or the square root of " + str((result**2)) + '''
    ''')
    history.append("Pythagorean Theorem: " + str(result) +"/The square root of " + str(result**2))

print("Welcome to the Improved Formula Calculator!")
run = True
while run == True:
    choice = input('''What would you like to do?

    1. Quartic Formula
    2. Cubic Formula
    3. Quadratic Formula
    4. Heron's Formula
    5. Surface Area of a Sphere
    6. Pythagorean Theorem
    7. View History
    8. End Program

    ''')
    if choice in ["1","2","3","4","5","6","7","8"]:
        choice == int(choice)
    if choice == 1:
        quartic_formula()
    elif choice == 2:
        cubic_formula()
    elif choice == 3:
        quadratic_formula()
    elif choice == 4:
        herons_formula()
    elif choice == 5:
        sphere_surface_area(float(input("Please enter the radius of the sphere: ")))
    elif choice == 6:
        pythagorean_theorem()
    elif choice == 7:
        entries = input("How many entries back back would you like to go? Enter ALL to view the entire History for this session: ")
        numbers_through_100 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"]
        if entries in numbers_through_100:
            view_history(int(entries))
        elif entries == "ALL":
            view_history(entries)
        else:
            print('''  
                    Please try again with a valid input. Only numbers 1-100 are accepted.
                    ''')
    elif choice == 8:
        run = False
    else:
        print('''
        That is not a valid selection, please try again.
        ''')
