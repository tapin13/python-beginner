# define simple function
def echoHello():
    print("Hello from function")

print("Hello from main")

echoHello()

echoHello()

# define function with argument
def multArgumentByTwo(x):
    return x * 2

print("Result work of function multArgumentByTwo(3): " + str(multArgumentByTwo(3)))

print("Result work of function multArgumentByTwo(51): " + str(multArgumentByTwo(51)))

# multArgumentByTwo() - TypeError: multArgumentByTwo() missing 1 required positional argument: 'x'

# define function with two arguments
def sum(x, y):
    return x + y

print("Result work of function sum(3, 5): " + str(sum(3, 5)))

print("Result work of function sum(-2, 69): " + str(sum(-2, 69)))

# define function with argument and without return
def echoArgument(x):
    print("function argument value: " + str(x))

echoArgument(32)
echoArgument(126)
echoArgument("any string value")

print("Enmpty return function: " + str(echoArgument(21)))

# define function that only return value
def getTemperature():
    return 36.6

print("Human normal temperature is " + str(getTemperature()))

name_1 = "Tom"
weight_1 = 50
height_1 = 1.65

name_2 = "Garry"
weight_2 = 150
height_2 = 1.55

name_3 = "Viki"
weight_3 = 90
height_3 = 1.70

def bmi(name, weight, height):
    print("bmi get data - name: " + name + ", weight: " + str(weight) + ", height: " + str(height))

    bmi = weight / ( height ** 2 )

    return bmi

print("Name: " + name_1 + " - bmi: " + str(bmi(name_1, weight_1, height_1)))
print("Name: " + name_2 + " - bmi: " + str(bmi(name_2, weight_2, height_2)))
print("Name: " + name_3 + " - bmi: " + str(bmi(name_3, weight_3, height_3)))

def bmiToVerbal(name, bmi):
    if(bmi < 25):
        print("Name: " + name + " weight ok")
    else:
        print("Name: " + name + " weight bad")

bmiToVerbal(name_1, bmi(name_1, weight_1, height_1))
bmiToVerbal(name_2, bmi(name_2, weight_2, height_2))
bmiToVerbal(name_3, bmi(name_3, weight_3, height_3))

def convertMilesToKilometers(miles):
    return miles * 1.6

def squareArea(side_1, side_2):
    return side_1 * side_2

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

print("convertMilesToKilometers(50): " + str(convertMilesToKilometers(50)))
print("squareArea(2, 3): " + str(squareArea(2, 3)))
print("isEven(5): " + str(isEven(5)))
print("isEven(80): " + str(isEven(80)))

