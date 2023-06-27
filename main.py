import json
from prettytable import PrettyTable
import os,sys
my_table = PrettyTable()
def CLR():
    os.system('cls' if os.name=='nt' else 'clear')
class Library:
    def __init__(self):
        try:
            f = open("data.txt","r")
            data = f.read()
            self.database = json.loads(data)
            print(self.database)
        except:
            print("File not found")
    def writeFile(self):
        f = open("data.txt","w")
        f.write(json.dumps(self.database))
    def showList(self):
        CLR()
        try:
            my_table.clear_rows()
            my_table.field_names = ["Book name","Available items","Price(1Qty)"]
            for i in self.database:
                my_table.add_row([i.title(),self.database[i][0],self.database[i][1]])
            print(my_table)
        except:
            print("Some error occured at prettytables")
    def addItem(self):
        CLR()
        try:
            qname = input("Enter the item name : ").lower()
            if qname in self.database:
                inp = input("Enter the quantity : ")
                self.database[qname][0] += inp
            else:
                inp = int(input("Enter the quantity : "))
                self.database[qname] = [inp]
                inp = int(input("Enter price of the book : "))
                self.database[qname].append(inp)
            self.writeFile()
        except:
            CLR()
            print("Enter valid input")
            self.addItem()
    def delItem(self):
        CLR()
        query = input("Enter the item name : ").lower()
        if query in self.database:
            op = input(f"Sure to delete {self.database[query][0]} items of {query}?").lower()
            if op[0] == "y":
                del self.database[query]
            else:
                pass
            self.writeFile()
        else:
            print("Item not found!")
    def buyBook(self):
        CLR()
        query = input("Enter the item name : ").lower()
        if query in self.database:
            op = int(input(f"Enter number of items you want to buy(Available : {self.database[query][0]}) : "))
            if op <= self.database[query][0]:
                ch = input(f"Do you want to buy {query.title()} for {op*self.database[query][1]}/- ?").lower()
                if ch[0] == 'y':
                    CLR()
                    print("item brought")
                    if op == self.database[query][0]:
                        del self.database[query]
                    else:
                        self.database[query][0] = self.database[query][0]-op
                    self.writeFile()
                else:
                    pass
            else:
                CLR()
                print(f"{query} has only {self.database[query][0]} available itemms")
        else:
            CLR()
            print(f"{query} Item not found!")
def main():
    lib = Library()
    while True:
        inp = input("1)Show Books\n2)Add Book\n3)Delete Book\n4)Purchase book\n5)Exit : ")
        if inp=='1':
            lib.showList()
        elif inp=='2':
            lib.addItem()
        elif inp=='3':
            lib.delItem()
        elif inp=='4':
            lib.buyBook()
        else:
            sys.exit()
main()