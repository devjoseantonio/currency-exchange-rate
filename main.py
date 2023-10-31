import requests
import json

option = 0
headers = {"accept": "application/json"}

##print(response.text)
print("This program converts one currency to another.")
print("Select an option:\n"
      "1. EUR to USD\n"
      "2. EUR to COP\n"
      "3. USD to EUR\n"
      "4. USD to COP\n"
      "5. COP to USD\n"
      "6. COP to EUR\n")
while option != '':
    error = False
    option = input("Insert a number or press enter to exit: ")
    if option != '':
        try:
            option = int(option)
            match option:
                case 1:
                    currencyFrom = "EUR"
                    currencyTo = "USD"
                case 2:
                    currencyFrom = "EUR"
                    currencyTo = "COP"
                case 3:
                    currencyFrom = "USD"
                    currencyTo = "EUR"
                case 4:
                    currencyFrom = "USD"
                    currencyTo = "COP"
                case 5:
                    currencyFrom = "COP"
                    currencyTo = "USD"
                case 6:
                    currencyFrom = "COP"
                    currencyTo = "EUR"
                case _:
                    print("Error: the number {} is not a valid option\n".format(option))
                    error = True
            if not error:
                amount = float(input("Insert the amount to convert: "))
                if amount <= 0:
                    print("Error: The amount must be greather than 0")
                else:
                    url = "https://api.fastforex.io/convert?" \
                    "from=" + currencyFrom + "&to=" + currencyTo + "&amount={}" \
                    "&api_key=".format(amount)
                    response = requests.get(url, headers=headers)
                    json_response = json.loads(response.text)
                    
        except:
            print("Error: The software only accepts numbers\n")
            