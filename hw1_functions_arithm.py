

def add(a = None, b = None):
    while True:
        try:
            a = float(input("Input first number (integer or decimal): "))
            b = float(input("Input second number (integer or decimal): "))
            if a != int(a):
                result = a + b
                print(result)
                break
            else:
                result = int(a) + int(b)
                print(result)
                break
        except:
            print("Oops! Try Again!")

add()