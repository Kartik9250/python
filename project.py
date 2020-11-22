"""
mysql code:-

create database stocks;
use stocks;
create table stock(sid int(2), name varchar(10), price int(3));
insert into stock values(1, "patanjali", "50rs"),(2, "arora", "32rs"),(3, "dabar", "58rs"),(4, "parle", "76rs"),(5, "oscorp", "43rs");
create table account(sid int(2), date datetime(), quantity int(3);
"""

import mysql.connector as sql
from tabulate import tabulate
from datetime import date

mycon = sql.connect(host = "localhost", user = "kartik", password = "9250", database = "stocks")
cur = mycon.cursor()

cur.execute("select * from stock")
data = cur.fetchall()

def menu1():
    print("\t \t ******** Welcome to stock management software 2020 ********")
    print()
    print("1. View Stocks")
    print("2. Buy Stocks")
    print("3. Sell Stocks")
    print("4. Exit")
    print()

    var1 = int(input('Enter your choice: '))

    if var1 == 1:
        menu2()
    elif var1 == 2:
        menu3("bought")
    elif var1 == 3:
        menu3("sold")
    elif var1 == 4:
        exit()
    else:
        print('Kindly select a valid option from the above')
        if var1 == 1:
            menu1()
        else:
            exit()


    print("------------------------------------------------------------------")
    print()


def menu2():
    print(tabulate(data, headers=['stock_id', 'Name', 'Price'],tablefmt='psql'))

    var1 = int(input('Press [1] to go back and [2] to exit: '))

    if var1 == 1:
        menu1()
    else:
        exit()

    print("------------------------------------------------------------------")
    print()

def menu3(a):
    back = a
    dt = date.today()
    date1 = dt.strftime('%Y/%m/%d')
    
    if a == "bought":
        var1 = int(input('Enter sid to buy stock: '))
        var2 = int(input('How many would you like to buy: ')) 

        cur.execute("select * from stock where sid like "+str(var1))
        d = cur.fetchall()

    elif a == "sold":
        var1 = int(input('Enter sid to sell stock: '))
        var2 = int(input('How many would you like to sell: '))

        cur.execute("select * from account where sid like "+str(var1))
        d = cur.fetchall()

    print()

    if len(d) == 0:
        input("Sid doesnt match with our records, try again by pressing any key: ")
        print("------------------------------------------------------------------")
        print()
        menu3(back)

    else:
        val = (var1, date1, var2, a)
        sql = "insert into account values(%s,%s,%s,%s)" 
        cur.execute(sql,val)
        mycon.commit()

    var1 = int(input('Press [1] to go back and [2] to exit: '))

    if var1 == 1:
        menu1()
    else:
        exit()

    print("------------------------------------------------------------------")
    print()


menu1()
