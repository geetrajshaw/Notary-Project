# Utility function for printing the transactions list
def addSpaces(input, total_length):
    input = str(input)
    while (total_length - len(input)) > 0:
        input = input + " "
    return input

# This function prints all the verified transactions in the blockchain


def viewTransactions(blockchain):

    if len(blockchain.chain) == 0:
        print("\nNo completed transactions to display!!!")
        return

    print("Transaction ID      Seller      Buyer        LegalDoc_ID     Amount(INR)     Timestamp")
    print("-------------------------------------------------------------------------------------")
    transaction_quote = "{}      {}      {}      {}     {}      {}"

    for block in blockchain.chain:
        for transaction in block['transactions_list']:
            print(transaction_quote.format(
                addSpaces(transaction[0], len("Transaction ID")),
                addSpaces(transaction[2], len("Seller")),
                addSpaces(transaction[3], len("Buyer")),
                addSpaces(transaction[4], len("LegalDoc_ID")),
                addSpaces(transaction[1], len("Amount(INR)")),
                transaction[5]
            ))
