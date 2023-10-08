import datetime
import Node

# This function takes input(unverified transactions) from the user


def inputTransactions(blockchain, leftover_trns):

    input_transactions = leftover_trns

    while True:
        print("\nInput Transaction details")

        while True:
            trn_id = input("\n>>> Transaction id : ")

            exists = False
            for block in blockchain.chain:  # Check if the transaction id already exists in the blockchain
                for transaction in block["transactions_list"]:
                    if trn_id == transaction[0]:
                        exists = True
                        break
                if exists:
                    break
            for transaction in input_transactions:
                if exists:
                    break
                else:
                    if trn_id == transaction[0]:
                        exists = True
                        break
            if exists:
                print("\nTransaction already exists! Please Try again.")
                continue
            break

        amount = -1
        while True:
            try:
                amount = float(input("\n>>> Amount         : "))
                break
            except ValueError:
                print("\nInvalid amount!! Please try again")

        amount_enough = True
        Buyer = input("\n>>> Buyer          : ")
        buyer_exists = False
        for i in Node.list_node:
            if Buyer == i.name:
                if (i.amount-amount < 0):
                    print("Buyer does not have enough amount")
                    amount_enough = False
                    buyer_exists = True
                    break
                i.amount = i.amount - amount
                amount_enough = True
                buyer_exists = True
                break
        if amount_enough == False:
            continue
        if buyer_exists == False:
            print("Buyer does not exist")
            continue

        Seller = input("\n>>> Seller         : ")
        seller_exists = False
        for i in Node.list_node:
            if Seller == i.name:
                i.amount = i.amount + amount
                seller_exists = True
                break
        if seller_exists == False:
            print("Seller does not exist")
            continue
        if (Seller == Buyer):
            print("Seller and Buyer cannot be same")
            continue
        # print("\nInput Property id")
        property_id = input("\n>>> Legal Document id    : ")

        input_transactions.append((
            trn_id,
            amount,
            Seller,
            Buyer,
            property_id,
            str(datetime.datetime.now().strftime("%Y-%m-%d AT %H:%M %p"))
        ))

        y_or_n = input("\nD O N E!\n>>> Add more?[y/n]")

        if y_or_n == 'n':
            return input_transactions


# This function verifies the transactions and adds them to the block(3 transactions per block)
def addTransactions(input_transactions, blockchain):

    #count = len(input_transactions)
    verified_trn_list = tuple(input_transactions)
    input_transactions = []

    blockchain.mine_block(verified_trn_list)

    if (not blockchain.chain_valid(blockchain.chain)):
        print("Blockchain is not valid")

    return input_transactions
