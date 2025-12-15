#Elvis Nguyen
def test_passwd(password:str):
    upperCaseCounter = 0
    digitCounter = 0

    for char in range(len(password)):
        tempStr = password[char]

        if tempStr.isdigit():
            digitCounter += 1

        if tempStr.isupper():
            upperCaseCounter += 1

    if ((upperCaseCounter >= 2) and (digitCounter >= 2)):
        return True
    else:
        return False
    
def main():
    passwd = input("Enter your password here: ")
    result = test_passwd(passwd)

    print(result)
    
if __name__ == "__main__":
    main()