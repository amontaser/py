blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def addvalue(transaction_amount, last_transaction=[1.0]):
    if last_transaction == None:
        last_transaction = [1.0]
    blockchain.append([last_transaction, transaction_amount])


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


def get_transaction_value():
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('your choice :')
    return user_input


def print_blockchain_elements():
    for index, block in enumerate(blockchain):
        print(index, '.Outputting Block >>>', block)


while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: mainpulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        amount = get_transaction_value()
        addvalue(amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [1.1]
    elif user_choice == 'q':
        break
    else:
        print('input was invalid, please choose another option')
    if not verify_chain():
        print('invalid blockchain!')
        print_blockchain_elements()
        break

print('OK, Goodbye (♥_♥)')