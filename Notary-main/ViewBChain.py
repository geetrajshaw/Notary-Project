import json

# This function takes the index of the block as an input and prints the corresponding block


def viewBlock(blockchain):
    if len(blockchain.chain) == 0:
        print("\nNo blocks available in blockchain")
        return

    while True:
        while True:
            try:
                index = int(input("\n>>> Enter the index of the block: "))
                break
            except ValueError:
                print("\nBlock Index should be a number. Please try again.")
                continue

        if index > len(blockchain.chain):
            print("\nNo block matches the index")
            y_or_no = input("\n>>> Repeat query>[y/n]")
            if y_or_no == 'y':
                continue
        break

    for block in blockchain.chain:
        if block["index"] == index:
            block = dict((k, block[k]) for k in ['index', 'previous_hash',
                                                 'merkle_root', 'validator', 'hash'])
            print(json.dumps(block, indent=4))
            return

    print("\nNo block found that matches the index.")
    return

# This function prints the entre blockchain


def viewBlockchain(blockchain):
    if len(blockchain.chain) == 0:
        print("\nNo blocks added yet.")
        return

    # print(json.dumps(blockchain.chain, indent=4))
    for i in blockchain.chain:
        i = dict((k, i[k]) for k in ['index', 'previous_hash',
                 'merkle_root', 'validator', 'hash'])
        print(json.dumps(i, indent=4))
        # print("---------------------------------------------------------------------------------------------------------------------")
