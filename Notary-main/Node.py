class Nodes:
    def __init__(self, name, amount):
        self.name = name
        self.amount = float(amount)
        self.reward = 0


list_node = []


def addNode():
    print("Enter the number of Users")
    num = int(input())
    for i in range(num):
        name = input("Enter the name of the User: ")
        amount = input("Enter the amount of the User: ")
        list_node.append(Nodes(name, amount))


def viewNode():
    print("Name\t\tamount\t\treward")
    for i in list_node:
        print(i.name, "\t\t", i.amount, "\t\t", i.reward)
