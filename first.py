from unidecode import unidecode
import matplotlib.pyplot as plt
import numpy as np
books={}
class book:

    def __init__(self,name ,p1,p2,star):
        self.name=name
        self.p1=int(p1)
        self.p2=int(p2)
        self.star=star
        self.pricemaxx=0
        self.priceminn=0
        self.pricemin=0
        self.sood=0
    def pricerange(self):
        if ( self.p1==0 or self.p2 ==0):
            self.pricemin=max(self.p1,self.p2)
        else:
            self.pricemin=min(self.p1,self.p2)
        self.priceminn=((self.pricemin*7)/10)+2000+4000
        self.priceminn=((self.priceminn)/10)*11
        self.pricemaxx=self.pricemin
        self.sood=(self.pricemaxx-self.priceminn)/2
    def competitivity(self):
        if( self.priceminn < self.pricemaxx ):
            return "is competitive"
        else:
            return "is not competitive"


def plott(i):
    x = np.array(["Zabanmehr","Hadafnovin","nimA.reverse()","profit"])
    y = np.array([int(books[i].p1),int(books[i].p2),int((books[i].priceminn+books[i].pricemaxx)/2),books[i].sood])
    plt.bar(x, y, width = 0.1)
    plt.title(books[i].name)
    plt.ylabel("price")
    plt.show()

def numberout(line):

    new_str=""
    for i in range(len(line)):
        if(line[i].isdigit()==True):
            new_str=new_str+line[i]
    if (len(new_str)==0):
        number=0
    else:
        number=int(new_str)
    return number

def convert(text):
    return unidecode(text)

with open("names.txt", "r", encoding="utf-8") as file:
    content = file.read()
    converted_content = convert(content)
    with open("converted.txt", "w", encoding="utf-8") as new_file:
        new_file.write(converted_content)

def check():
    file1=open('converted.txt','r')
    file2=open('data.txt','w')
    for i in range(20):
        name=file1.readline().replace('Title: ','')
        name=name.strip()
        price1=numberout(file1.readline())
        price2=numberout(file1.readline())
        star=file1.readline()
        books.update({name : book(name,price1,price2,star)})
        if(price1==0 and price2==0):
            file2.write(f"title: {books[name].name}\n")
            file2.write(f"Zabanmehr : price not found\n")
            file2.write(f"Hadafnovin : price not found\n")
            file2.write(f"price range : not found\n")
            file2.write(f"nimA.reverse : 100000\n")
            file2.write(f"{star}\n")
            books[name].priceminn=100000
            books[name].pricemaxx=100000
            books[name].sood=20000

        else:
            books[name].pricerange()
            file2.write(f"title: {books[name].name}\n")
            file2.write(f"Zabanmehr : {books[name].p1}\n")
            file2.write(f"Hadafnovin : {books[name].p2}\n")
            file2.write(f"price range : {books[name].priceminn} - {books[name].pricemaxx}\n")
            file2.write(f"nimA.reverse : {(books[name].priceminn+books[name].pricemaxx)/2}\n")
            file2.write(f"{star}\n")
        file1.readline()
    
check()
