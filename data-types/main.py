
# --- Integer

print("Data Types Examples")

integerA = 5
integerB = 6

print("integer: " + str(integerA) + " + " + str(integerB) + " = " + str(integerA + integerB) )

# --- Float

floatA = 5.1
floatB = 6.2

print("float: " + str(floatA) + " + " + str(floatB) + " = " + str(floatA + floatB) )

# --- String

firstName = "Vasia"
lastName = "Pupkin"

print("Hello " + firstName + " " + lastName)

carList = [ "Mercedes", "BMW", "Zhiguli" ]

print("Cars " + str(carList) )

print("Cars 2: " + str(carList[1]) )

# --- Dictionaries

languageDict = { 
    "Hello" : "Привет", 
    "Bye": "Пока" 
}

print("language translates " + str(languageDict) )

print(str("Hello") + " translate " + str(languageDict["Hello"]) )

# --- Tuples

cityTup = ( "Moscow", "Tel-Aviv" )

print("cities " + str(cityTup) )

print("Travel from " + str(cityTup[1]) + " to " + str(cityTup[0]) )

# --- Set

bagSet = { "Pen", "Book", "Papers" }

print("bag " + str(bagSet) )

for thing in bagSet:
    print("Bag include " + str(thing) )

bagSet.add("Glasses")

print("bag " + str(bagSet) )

# --- Boolean

lightStatus = False

print("Light " + str(lightStatus) )

print("Light is " + str(lightStatus) )

lightStatus = True

print("Light is " + str(lightStatus) )
