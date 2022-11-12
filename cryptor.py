
#Crypting message, return result
#seter - array letters
#Checking letter in seter array, if true append result letter index + 13
#If letter upper, set lower, check, append upper

def cryptor(message):
    seter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result = ""
    for letter in message:
        if letter in seter:
            result += seter[(seter.index((letter.upper())) +13) %26]
            continue
        elif letter.upper() in seter:
            result += seter[(seter.index((letter.upper())) +13) %26].lower()
            continue
        result += letter
    return result

#Start program. Get text. Print result
if __name__ == "__main__":
    message = input("Enter text: ")
    print(cryptor(message))