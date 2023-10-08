import BlockChain
import AddTransactions
import ViewProperty
import ViewMultipleTransaction
import ViewTimestamp
import ViewBChain
import ViewUnverified
import Node
# Initiating the blockchain
blockchain = BlockChain.Blockchain()

print("<------------------------SESSION START------------------------->")

leftover_trns = []
# To hold any unverified transactions after an iteration

# Iterations start...
# In each iteration the user can perform only one query
while True:
    print("\n_________________________________________")
    print("_________________________________________")
    print("\n[1] - Add Users")
    print("[2] - View Users")
    print("[3] - Add Transactions")
    print("[4] - View completed Transactions")
    print("[5] - View Transactions for a particular Legal Document")
    print("[6] - View a block")
    print("[7] - View the Blockchain")
    print("[8] - View Timestamp of a transaction")
    print("[9] - View unverified transactions")
    print("[10] - Forge the Block")
    print("\n[e] - Exit")
    choice = input("\n>>> Choose a query to execute: ")

    if choice == "1":
        Node.addNode()
    elif choice == "2":
        Node.viewNode()
    elif choice == "3":
        unverified_trns = AddTransactions.inputTransactions(
            blockchain, leftover_trns)

    elif choice == "4":
        ViewMultipleTransaction.viewTransactions(blockchain)

    elif choice == "5":
        ViewProperty.viewTransaction(blockchain)

    elif choice == "6":
        ViewBChain.viewBlock(blockchain)

    elif choice == "7":
        ViewBChain.viewBlockchain(blockchain)

    elif choice == "8":
        ViewTimestamp.viewTimestamp(blockchain)

    elif choice == "9":
        ViewUnverified.viewUnverifiedTransactions(leftover_trns)
    elif choice == "10":
        leftover_trns = AddTransactions.addTransactions(
            unverified_trns, blockchain)
        print("Forged the block successfully!")

    elif choice == "e":
        if blockchain.chain_valid(blockchain.chain) == False:

            exit()

        print("\nThank you.\n")
        break

    else:
        print('\nPlease choose from the queries given!!!')

print("<-------------------------SESSION END-------------------------->")
