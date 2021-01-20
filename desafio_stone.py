
def shopping_list():
    #INSERT THE PRODUCT'S LIST BELOW, RESPECTING THE FORMAT [[item, quantity, value], ..., [item, quantity, value]]
    itens = []
    #INSERT THE E-MAIL'S LIST BELOW, RESPECTING THE FORMAT ['a@gmail.com', 'b@hotmail.com',...]
    emails = []

    return itens, emails


def calculate(itens, emails):

    #In case the product's or e-mail's list are empty
    if itens == [] or emails == []:
        return -1

    total = 0
    result_list = {}
    
    #Calculation of the shopping list global value
    for x in range(len(itens)):
        value = itens[x][1] * itens[x][2]
        total += value

    #Calculation of the value each person (e-mail) should pay      
    each_value = total // len(emails) #value for each person (e-mail)
    remain = total % len(emails) #remain value if the division is not exact

    #Dict construction {email : each payable value}
    for y in range(len(emails)-1):
        result_list[emails[y]] = each_value #Each person pays the correspondent value

    result_list[emails[len(emails)-1]] = each_value + remain #The last person pays the correspondent value + remain value

    return result_list


def main():
   
    itens, emails = shopping_list()
    result = calculate(itens, emails)

    if result == -1:
        print('Lista de compras vazia ou lista de e-mails vazia.')

    else:
         print(result)

main()


