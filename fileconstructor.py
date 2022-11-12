#Write text to file in append mode
def write(name):
    file = open(name,"a", encoding='utf-8') 
    text = input("Enter text: ")
    file.write(f" {text}")
    
#Read text from file    
def read():
    return file.read()


#Truncate file to 0 bytes in write mode
def truncate(name):
    file = open(name,"w", encoding='utf-8')
    file.truncate()


#Create file name. Append .txt, open file. Choise cycle
def main():
    name = input("Enter file name: ")
    name += ".txt"

    file = open(name,"w", encoding='utf-8')

    while True:
        file = open(name, encoding='utf-8')
        
        choise = int(input("""Choise:
    1 - Write
    2 - Read
    3 - Clear all
    """))
        
        if choise == 1:
            write(name)
        elif choise == 2:
            print(read())
        elif choise == 3:
            truncate(name)
            
        else:
            print("You make mistake. Try again")


if __name__ == "__main__":
    main()