from functools import reduce

#Convert string to int 
def converter(file):
    num = []
    for i in range(0, len(file), 1):
        array = int(file[i]) #Convert str to int
        num.append(array)
    return num

#Return list with all paired nums
def step1(num):
    return list(filter(lambda a: a % 2 == 0, num))

#Create array, append sum digit all nums 
def step2(result):
    back = []
    for i in range(0, len(result), 1):
        nums = [int(j) for j in str(result[i])]
        back.append(reduce(lambda a, b: a+b, nums))
    return back

#return square list
def step3(result):
    	return list(map(lambda x: x**2, result))


def ziper(s, result):
    print(list(zip(s, result)))

#Main commander. 
def main():
    with open("numbers.txt", "r") as temp:
        file = list(temp)
    num = converter(file)
    result = step1(num)
    s = result
    result = step2(result)
    result = step3(result)
    
    ziper(s, result)



if __name__ == "__main__":
    main()