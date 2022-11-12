#s - array letters
#Checking letter in "s" array, if true result +=1
def counter(message):
    s = ['A', 'E', 'O', 'I', 'U', 'a', 'e', 'o', 'i', 'u']
    result = 0
    for letter in message:
        if letter in s:
            result += 1
            continue
    print(f"Result is {result}")
   
 #Input message   
if __name__ == "__main__":
    message = input("Enter message \n")
    print(" ")
    counter(message)