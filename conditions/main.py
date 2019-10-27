a = 1
b = 2

if a < b :
    print("a less then b")
    print("b more then a")

print("done with if condition 1")

# -----------------------------

c = 4
d = 4

if c < d :
    print("c less then d")
else :
    print("c more then d or c equale to d")

print("done with if condition 2")

# -----------------------------

e = 5
f = 4

if e < f :
    print("e less then f")
elif e == f :
    print("e equale to f")
else :
    print("e more then f")

print("done with if condition 3")

# -----------------------------

j = 19
h = 2
if j < h :
    print("j less then h")
else :
    if j == h :
        print("j equale h")
    else :
        print("j more then h")


print("done with if condition 4")

# -----------------------------

name = "Mark"
height = 1.9
weight = 72

bmi = weight / ( height ** 2 )

print("Name " + name + " have BMI: " + str(bmi) )

if bmi < 25 :
    print(name + " not fat")
else :
    print(name + " is overweight")

print("done with if condition 5")

# -----------------------------

name = "Maria"
height = 1.9
weight = 120

bmi = weight / ( height ** 2 )

print("Name " + name + " have BMI: " + str(bmi) )

if bmi < 25 :
    print(name + " not fat")
else :
    print(name + " is overweight")

print("done with if condition 6")
