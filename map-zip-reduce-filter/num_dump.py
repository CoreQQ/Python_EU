from functools import reduce

#Convert string array to int array
def convert(file):
    num = list(map(lambda x: int(x), file))
    return num

#Return list with all paired nums
def get_paired(num):
    return list(filter(lambda a: a % 2 == 0, num))


#Create array, append sum digit all nums 
def get_sum(temp):
    s = []
    for i in range(0, len(temp), 1):
        x = [int(j) for j in str(temp[i])] #num to array
        s.append(reduce(lambda a, b: a+b, x)) # sum all digit
    return s


#


#Return list with square all array element
def get_square(lod):
	return list(map(lambda x: x**2, lod))

#Main function, call all function and print steps or result
def main():
    with open("numbers.txt", "r") as f: #Read line array
        file = list(f) # Create Array
    
    num = convert(file) # Convert str to int

    temp = get_paired(num) #First step
    print(f"Step 1: {temp}")

    lod = get_sum(temp) # Second step
    print(f"Step 2: {lod}")

    lod = get_square(lod) #Third step
    print(f"Step 3: {lod}")

    end = list(zip(temp, lod)) # Last step, Create zip First step and Third step
    print(f"Result: {end}")



#Start program
if __name__ == "__main__":
    main()



