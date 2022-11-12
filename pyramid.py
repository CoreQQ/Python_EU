

#Search first element
# For i in range x*2 (5*2 =10) result = first elemtnt + i
# Create output add "{element} + "
#In last elemtnt remove 2 last symblos
def pyra(x):
    algorithm = 1
    for i in range(x):
        algorithm += i*2
    result = 0
    output = ""
    print("  ")
    for i in range(0, x*2, 2):
        output += (f"{algorithm + i} + ")
        result += algorithm + i
    
    output = output[:-2]
    print(f"{output}\n Result: {result}")



#input x
x = int(input("Enter x \n"))
pyra(x)