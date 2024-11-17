# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:39:14 2020

@author:Adithya,lakshetha
"""

#ENTER YOUR MYSQL PASSWORD IN LINE 12 PASSWD FIELD 
import mysql.connector as ch
import random
import sys
conn=ch.connect(host="localhost",user="root",passwd="")
cur=conn.cursor()
cur.execute("Create database IF NOT EXISTS HELLOBUS;")
conn.commit()
cur.execute("use HELLOBUS;")
conn.commit()
cur.execute("create table if not exists bus_ticket_available (Departure varchar(30),Destination varchar(30),BusNo varchar(30),Time varchar(30),AvailableTickets numeric);")
conn.commit()
cur.execute("create table if not exists bus_detail (UserName varchar(30),Name varchar(30),Age varchar(30),Gender varchar(30),Contact varchar(30),Departure varchar(30),Destination varchar(30),BusNo varchar(30),DateOfBus varchar(20), TimeOfBus varchar(30),BusCost varchar(30),NoOfTickets varchar(30));")
conn.commit()
cur.execute("delete from bus_ticket_available;")
cur.execute("insert into bus_ticket_available values('{}','{}','{}','{}',{});".format("Chennai","Kanyakumari","1254","6:00 AM",25))
conn.commit()
cur.execute("insert into bus_ticket_available values('{}','{}','{}','{}',{});".format("Trichy","Nagarcoil","6790","10:00 AM",25))
conn.commit()
cur.execute("insert into bus_ticket_available values('{}','{}','{}','{}',{});".format("Coimbatore","Tanjore","1977","1:00 PM",25))
conn.commit()            
cur.execute("insert into bus_ticket_available values('{}','{}','{}','{}',{});".format("Salem","Pondicherry","1809","4:00 PM",25))
conn.commit()
cur.execute("insert into bus_ticket_available values('{}','{}','{}','{}',{});".format("Madurai","Tuticorin","2384","12:00 PM",25))
conn.commit()
     
def busmenu():
    while True:
        print("*"*30)
        print("TNEXPRESS--BUS TICKET BOOKING")
        print("*"*30)
        print("1.BUS DETAIL")
        print("2.E-BOOKING OF TICKET")
        print("3.CANCELLATION OF TICKET")
        print("4.VIEW HISTORY")
        print("5.LOG OUT")
        n=int(input("Enter your choice:"))
        if(n==1):
            bus_detail()
        elif(n==2):
            e_booking()
        elif(n==3):
            cancellation()
        elif(n==4):
            view_history()
        elif(n==5):
            print("********LOG OUT??********")
            a=input("Are you sure you want to log out?(y/n):")
            if a=="y" or a=="Y":
                sys.exit()
            else:
                busmenu()
        else:
            print("WRONG CHOICE!!")

def bus_detail():
    print("*"*30)
    print("STARTING POINT-DESTINATION")
    print("*"*30)
    print("Chennai-Kanyakumari")
    print("Trichy-Nagarcoil")
    print("Coimbatore-Tanjore")
    print("Salem-Pondicherry")
    print("Madurai-Tuticorin")
    a=str(input("Enter your starting point:"))
    if a[1] in "Hh":
        print("Your Destination : KANYAKUMARI")
        print("Bus Number : 1254")
        print("Bus Time from starting point : 06:00 AM")
        b=input("If your Destination is KANYAKUMARI press y, else press n:")
        while True:
            if b in "yY":
                break
            elif b in "nN":
                print("---------THERE IS NO SERVICE TO OTHER CITY---------")
                break
    elif a[0] in "Tt":
        print("Your Destination : NAGARCOIL")
        print("Bus Number : 6790")
        print("Bus Time from starting point : 10:00 AM")
        b=input("If your Destination is NAGARCOIL press y, else press n:")
        while True:
            if b in "yY":
                break
            elif b in "nN":
                print("---------THERE IS NO SERVICE TO OTHER CITY---------")
                break 
    elif a[1] in "Oo":
        print("Your Destination : TANJORE")
        print("Bus Number : 1977")
        print("Bus Time from Departure : 01:00 PM")
        b=input("If your Destination is TANJORE press y, else press n:")
        while True:
            if b in "yY":
                break
            elif b in "nN":
                print("---------THERE IS NO SERVICE TO OTHER CITY---------")
                break 
    elif a[0] in "Ss":
        print("Your Destination : PONDICHERRY") 
        print("Bus Number : 1809")
        print("Bus Time from Departure : 04:00 PM")
        b=input("If your Destination is PONDICHERRY press y, else press n:")
        while True:
            if b in "yY":
                break
            elif b in "nN":
                print("---------THERE IS NO SERVICE TO OTHER CITY---------")
                break 
    elif a[0] in "mM":
        print("Your Destination : TUTICORIN")
        print("Bus Number : 2384")
        print("Bus Time from Departure : 12:00 PM")
        b=input("If your Destination is TUTICORIN press y, else press n:")
        while True:
            if b in "yY":
                break
            elif b in "nN":
                print("---------THERE IS NO SERVICE TO OTHER CITY---------")
                break 
    busmenu()
    
def e_booking():
    print("*"*50)
    print("ENTER YOUR INFORMATION AS FOLLOWS:")
    print("*"*50)
    h=str(input("Enter your userID:"))
    a=str(input("Enter passenger's name:"))
    R=str(input("Enter passenger's age:"))
    c=str(input("Enter passenger's gender M/F/O:"))
    t=str(input("Enter passenger's contact:"))
    F=input("Enter passenger's address:")
    r=str(input("Date on which you want to travel(year-month-date):"))
    print("*"*30)
    print("STARTING POINT-DESTINATION")
    print("*"*30)
    print("Chennai-Kanyakumari")
    print("Trichy-Nagarcoil")
    print("Coimbatore-Tanjore")
    print("Salem-Pondicherry")
    print("Madurai-Tuticorin")
    o=str(input("Enter your starting point:"))
    if o[1] in "Hh":
        print("Your Destination : KANYAKUMARI") 
        print("Bus Number : 1254")
        print("Bus Time from Departure : 06:00 AM")
        b=input("If your Destination is KANYAKUMARI press y:")
        while True:
            if b in "yY":
                k=input("Enter your Destination:")
                nt=int(input("Enter no of ticket(s):"))
                n=input("Enter your Bus Number:")
                E1="\"_h%\""
                A=25
                A-=nt
                print("Total number of ticket(s) left is",A)
                cur.execute("update bus_ticket_available set AvailableTickets=AvailableTickets-{} where Departure like '{}'".format(nt,E1))
                conn.commit()
                if n=="1254":
                    print("Amount is",nt*1100,"rupees")
                else:
                    print("WRONG BUS NUMBER--TRY AGAIN FROM FIRST!!!")
                    break
                z=input("Enter your Amount:")
                e=str(input("Enter time from starting point of your bus:"))
                x=input("Enter your credit card or debit card number:")
                m=str(input("Would you like to confirm your seat(y/n):"))
                if m=="y" or m=="Y":
                    T=random.randint(1,10)
                    print("Your Seat Number(s):")
                    for i in range(0,nt):
                        print("B0",T+i,end="\t")
                    print("YOUR TICKET(S) IS CONFIRMED AND AMOUNT IS DEBITED FROM YOUR ACCOUNT!!!!")
                    break
                elif m=="n" or m=="N":
                    print("YOUR TICKET(S) IS NOT RESERVED AND AMOUNT IS NOT DEBITED FROM YOUR ACCOUNT!!!!")
                    break
                else:
                    print("WRONG OPTION!!!")
                    break
    elif o[0] in "Tt":
        print("Your Destination : NAGARCOIL")
        print("Bus Number : 6790")
        print("Bus Time from starting point : 10:00 AM")
        b=input("If your Destination is NAGARCOIL press y:")
        while True:
            if b in "yY":
                k=input("Enter your Destination:")
                nt=int(input("Enter no of ticket(s):"))
                n=input("Enter your Bus Number:")
                E2="\"_r%\""
                A=25
                A-=nt
                print("Total number of ticket(s) left is",A)
                cur.execute("update bus_ticket_available set AvailableTickets=AvailableTickets-{} where Departure like {}".format(nt,E2))
                conn.commit()
                if n=="6790":
                    print("Amount is",nt*750,"rupees")
                else:
                    print("WRONG BUS NUMBER--TRY AGAIN FROM FIRST!!!")
                    break
                z=input("Enter your Amount:")
                e=str(input("Enter time from starting point of your bus:"))
                x=input("Enter your credit card or debit card number:")
                m=str(input("Would you like to confirm your seat(y/n):"))
                if m=="y" or m=="Y":
                    T=random.randint(1,10)
                    print("Your Seat Number(s):")
                    for i in range(0,nt):
                        print("B0",T+i,end="\t")
                    print("YOUR TICKET(S) IS CONFIRMED AND AMOUNT IS DEBITED FROM YOUR ACCOUNT!!!!")
                    break
                elif m=="n" or m=="N":
                    print("YOUR TICKET(S) IS NOT RESERVED AND AMOUNT IS NOT DEBITED FROM YOUR ACCOUNT!!!!")
                    break
                else:
                    print("WRONG OPTION!!!")
                    break
    elif o[1] in "Oo":
        print("Your Destination : TANJORE")
        print("Bus Number : 1977") 
        print("Bus Time from starting point : 01:00 PM")
        b=input("If your Destination is TANJORE press y:")
        while True:
            if b in "yY":
                k=input("Enter your Destination:")
                nt=int(input("Enter no of ticket(s):"))
                n=input("Enter your Bus Number:")
                E3="\"_o%\""
                A=25
                A-=nt
                print("Total number of ticket(s) left is",A)
                cur.execute("update bus_ticket_available set AvailableTickets=AvailableTickets-{} where Departure like {}".format(nt,E3))
                conn.commit()
                if n=="1977":
                    print("Amount is",nt*1200,"rupees")
                else:
                    print("WRONG BUS NUMBER--TRY AGAIN FROM FIRST!!!")
                    break
                z=input("Enter your Amount:")
                e=str(input("Enter time from starting point of your bus:"))
                x=input("Enter your credit card or debit card number:")
                m=str(input("Would you like to confirm your seat(y/n):"))
                if m=="y" or m=="Y":
                    T=random.randint(1,10)
                    print("Your Seat Number(s):")
                    for i in range(0,nt):
                        print("B0",T+i,end="\t")
                    print("YOUR TICKET(S) IS CONFIRMED AND AMOUNT IS DEBITED FROM YOUR ACCOUNT!!!!")
                    break
                elif m=="n" or m=="N":
                    print("YOUR TICKET(S) IS NOT RESERVED AND AMOUNT IS NOT DEBITED FROM YOUR ACCOUNT!!!!")
                    break
                else:
                    print("WRONG OPTION!!!")
                    break
    elif o[0] in "Ss":
        print("Your Destination : PONDICHERRY")
        print("Bus Number : 1809")
        print("Bus Time from starting point : 04:00 PM")
        b=input("If your Destination is PONDICHERRY press y:")
        while True:
            if b in "yY":
                k=input("Enter your Destination:")
                nt=int(input("Enter no of ticket(s):"))
                n=input("Enter your Bus Number:")
                E4="\"__l%\""
                A=25
                A-=nt
                print("Total number of ticket(s) left is",A)
                cur.execute("update bus_ticket_available set AvailableTickets=AvailableTickets-{} where Departure like {}".format(nt,E4))
                conn.commit()
                if n=="1809":
                    print("Amount is",nt*890,"rupees")
                else:
                    print("WRONG BUS NUMBER--TRY AGAIN FROM FIRST!!!")
                    break
                z=input("Enter your Amount:")
                e=str(input("Enter time from starting of your bus:"))
                x=input("Enter your credit card or debit card number:")
                m=str(input("Would you like to confirm your seat(y/n):"))
                if m=="y" or m=="Y":
                    T=random.randint(1,10)
                    print("Your Seat Number(s):")
                    for i in range(0,nt):
                        print("B0",T+i,end="\t")
                    print("YOUR TICKET(S) IS CONFIRMED AND AMOUNT IS DEBITED FROM YOUR ACCOUNT!!!!")
                    break
                elif m=="n" or m=="N":
                    print("YOUR TICKET(S) IS NOT RESERVED AND AMOUNT IS NOT DEBITED FROM YOUR ACCOUNT!!!!")
                    break
                else:
                    print("WRONG OPTION!!!")
                    break
    elif o[0] in "mM":
        print("Your Destination : TUTICORIN")
        print("Bus Number : 2384")
        print("Bus Time from starting point : 12:00 PM")
        b=input("If your Destination is TUTICORIN press y:")
        while True:
            if b in "yY":
                k=input("Enter your Destination:")
                nt=int(input("Enter no of ticket(s):"))
                n=input("Enter your Bus Number:")
                E5="\"__d%\""
                A=25
                A-=nt
                print("Total number of ticket(s) left is",A)
                cur.execute("update bus_ticket_available set AvailableTickets=AvailableTickets-{} where Departure like {}".format(nt,E5))
                conn.commit()
                if n=="2384":
                    print("Amount is",nt*650,"rupees")
                else:
                    print("WRONG BUS NUMBER--TRY AGAIN FROM FIRST!!!")
                    break
                z=input("Enter your Amount:")
                e=str(input("Enter time from starting point of your bus:"))
                x=input("Enter your credit card or debit card number:")
                m=str(input("Would you like to confirm your seat(y/n):"))
                if m=="y" or m=="Y":
                    T=random.randint(1,10)
                    print("Your Seat Number(s):")
                    for i in range(0,nt):
                        print("B0",T+i,end="\t")
                    print("YOUR TICKET(S) IS CONFIRMED AND AMOUNT IS DEBITED FROM YOUR ACCOUNT!!!!")
                    break
                elif m=="n" or m=="N":
                    print("YOUR TICKET(S) IS NOT RESERVED AND AMOUNT IS NOT DEBITED FROM YOUR ACCOUNT!!!!")
                    break
        else:
            print("WRONG OPTION!!!")
    q="Insert into bus_detail values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(h,a,R,c,t,o,k,n,r,e,z,nt)
    cur.execute(q)
    conn.commit()
    busmenu()
    
def cancellation():
    a=input("Enter your Name: ")
    b=input("Enter your Bus number:")
    cur.execute("select NoOfTickets from bus_detail where Name='{}' and BusNo='{}';".format(a,b))
    f=cur.fetchone()
    if f is None:
        print("The Name and Bus number DOES NOT match!!")
    else:
        print("The no of booked tickets is: ",int(f[0]))
        c=int(input("Enter the number of Ticket(s) to be CANCELLED: "))
        if c<=int(f[0]):
            cur.execute("select departure from bus_detail where Name='{}' and BusNo='{}'".format(a,b))
            d=cur.fetchone()
            s=d[0]
            if s[1] in "hH":
                E1="\"_h%\""
                cur.execute("update bus_ticket_available set AvailableTickets=AvailableTickets+{} where Departure like {}".format(c,E1))    
                print("Your Ticket(s) has been CANCELLED!!")
                cur.execute("select AvailableTickets from  bus_ticket_available where Departure like {}".format(E1))  
                av=cur.fetchone()
                cur.execute("update bus_detail set NoOfTickets=NoOfTickets-{} where Name= '{}' and BusNo='{}'".format(c,a,b))
                print("Available ticket(s) of your Route is: ",int(av[0]))
                cur.execute("select NoOfTickets from  bus_detail where Name= '{}'".format(a))
                avv=cur.fetchone()
                print("Present count of your BOOKED TICKET(S): ",int(avv[0]))
            elif s[1] in "rR":
                E2="\"_r%\""
                cur.execute("update bus_ticket_available set AvailableTickets=AvailableTickets+{} where Departure like {}".format(c,E2))    
                print("Your Ticket(s) has been CANCELLED!!")
                cur.execute("select AvailableTickets from  bus_ticket_available where Departure like {}".format(E2))  
                av=cur.fetchone()
                cur.execute("update bus_detail set NoOfTickets=NoOfTickets-{} where Name= '{}' and BusNo='{}'".format(c,a,b))
                print("Available ticket(s) of your Route is: ",int(av[0]))
                cur.execute("select NoOfTickets from  bus_detail where Name= '{}'".format(a))
                avv=cur.fetchone()
                print("Present count of your BOOKED TICKET(S): ",int(avv[0]))
            elif s[1] in "oO":
                E3="\"_o%\""
                cur.execute("update bus_ticket_available set AvailableTickets=AvailableTickets+{} where Departure like {}".format(c,E3))    
                print("Your Ticket(s) has been CANCELLED!!")
                cur.execute("select AvailableTickets from  bus_ticket_available where Departure like {}".format(E3))  
                av=cur.fetchone()
                cur.execute("update bus_detail set NoOfTickets=NoOfTickets-{} where Name= '{}' and BusNo='{}'".format(c,a,b))
                print("Available ticket(s) of your Route is: ",int(av[0]))
                cur.execute("select NoOfTickets from  bus_detail where Name= '{}'".format(a))
                avv=cur.fetchone()
                print("Present count of your BOOKED TICKET(S):",int(avv[0]))
            elif s[2] in "lL":
                E4="\"__l%\""
                cur.execute("update bus_ticket_available set AvailableTickets=AvailableTickets+{} where Departure like {}".format(c,E4))    
                print("Your Ticket(s) has been CANCELLED!!")
                cur.execute("select AvailableTickets from  bus_ticket_available where Departure like {}".format(E4))  
                av=cur.fetchone()
                cur.execute("update bus_detail set NoOfTickets=NoOfTickets-{} where Name= '{}' and BusNo='{}'".format(c,a,b))
                print("Available ticket(s) of your Route is:",int(av[0]))
                cur.execute("select NoOfTickets from  bus_detail where Name= '{}'".format(a))
                avv=cur.fetchone()
                print("Present count of your BOOKED TICKET(S):",int(avv[0]))
            elif s[2] in "dD":
                E5="\"__d%\""
                cur.execute("update bus_ticket_available set AvailableTickets=AvailableTickets+{} where Departure like {}".format(c,E5))    
                print("Your Ticket(s) has been CANCELLED!!")
                cur.execute("select AvailableTickets from  bus_ticket_available where Departure like {}".format(E5))  
                av=cur.fetchone()
                cur.execute("update bus_detail set NoOfTickets=NoOfTickets-{} where Name= '{}' and BusNo='{}'".format(c,a,b))
                print("Available ticket(s) of your Route is: ",int(av[0]))
                cur.execute("select NoOfTickets from  bus_detail where Name= '{}'".format(a))
                avv=cur.fetchone()
                print("Present count of your BOOKED TICKET(S):",int(avv[0]))
        else:
            print("EXCEEDED LIMIT!!!")  
        conn.commit()
    busmenu()

def view_history():
    a=input("Enter your UserID:")
    cur.execute("select * from bus_detail where UserName='{}'".format(a))
    B=cur.fetchall()
    print(B)
    conn.commit()
    busmenu() 

g="y"
while True:
    print("*"*40)
    print("WELCOME TO TNEXPRESS BUS TICKET BOOKING")           
    print("*"*40)
    x=input("Are you an old user?(y/n):")
    
    if x=='y' or x=='Y':
        print("**********USER LOG-IN**********")
        a=str(input("Enter your UserID:"))      
        c=input("Did you enter your userid ?(y/n):")
        if c=="y" or c=="Y":
            busmenu()
        else:
           print("You will have to try again!!")
           break
    elif x=="n" or x=="N":
        w=str(input("Enter your name:"))
        print("Your UserID is--->",w)
        Up=input("Did you get your UserID ?(y/n):")  
        if Up=="y" or Up=="Y":
            busmenu()
        else:
            print("Sorry you will have to try again from first!!")
            break
    else:
        print("Sorry you will have to try again from first!!")
        break
    print("===================================================================")