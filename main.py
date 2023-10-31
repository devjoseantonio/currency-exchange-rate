import requests
import json
import env

currenys = ["EUR", "USD", "COP"]
option1 = 0
option2 = 0
headers = {"accept": "application/json"}

def printOptions ():
    i = 0
    for x in currenys:
        print(str(i) + ". " + x)
        i += 1


while option1 != '':
    error = False
    print("\nThis program converts one currency to another.")
    print("Select an option to convert from.")
    printOptions()
    option1 = input("Insert a number or press enter to exit: ")
    if option1 != '':
        
        try:
            option1 = int(option1)
            if 0 <= option1 <= 2:
                print("Select an option to convert to.")
                printOptions()
                option2 = input("Insert a number or press enter to return: ")
                option2 = int(option2)
                if 0 <= option2 <= 2:
                    print("Select an amount to convert.")
                    amount = float(input("Insert the amount to convert: "))
                    if amount <= 0:
                        print("Error: The amount must be greather than 0")
                    else:
                        url = ("https://api.fastforex.io/convert?" \
                            "from=" + currenys[option1] + "&to=" + currenys[option2] + "&amount={}" \
                                "&api_key=" + env.API_KEY).format(amount)
                    response = requests.get(url, headers=headers)
                    json_response = json.loads(response.text)
                    response = json_response.get("result")
                    
                    print(str(amount) + " " + currenys[option1] + " in " + currenys[option2] + " are " + str(response.get(currenys[option2])))
                else:
                    error = True
            else:
                error = True
            if error:
                print("Error: The number must be in between of 0 and 2")
        except:
            print("Error: The software only accepts numbers\n")