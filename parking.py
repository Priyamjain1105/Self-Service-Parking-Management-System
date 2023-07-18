#parking bill of DRDO DEPARTMENT
#entry,exit,bill[sno,name,phonum,date,entrytime , exittime,]
#main
import time
import pickle
import csv
import datetime
import os




#functions

#TO GET PRESENT DATE
def date():
    cd = datetime.date.today()
    d = str(cd)
    return d


#TO GET PRESENT TIME    
def ptime():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

#THE FIRST MENU SCREEN    
def main():
    print("PRESS 1 FOR ENTRY ONLY")
    print("PRESS 2 FOR EXIT ONLY")
    print("PRESS 3 FOR MANAGING")
    print("PRESS 4 FOR QUIT")
    
    ch = int(input("ENTER YOUR CHOOISE"))
    print("\n\n\n\n\n")
    if ch == 1:
        while True:
            print("________________________________")
            entry()
            print("\n"*3+"________________________________"+"\n"*4)
    elif ch == 2:
        while True:
            
            exitn()
            print("\n"*3+"________________________________"+"\n"*4)
    elif ch ==3:
        while True:
            
            manager()
            deco()
    else:
        print("THANKYOU")
        
            
        
#HEADING FOR ALL THREE FILES
def write_heading():
    
    global fb,fw,fc

    #opening files
    f = open(fb,"ab")
    f2 = open(fw,"a")
    f3 = open(fc,"a")

    #entries
    sno = "sno"
    name = "Name"
    phonenum = "Phoneno"
    date = "Date"
    entry = "Entry Time"
    exitt = "Exit Time"

    #record
    rec = [sno,name,phonenum,date,entry,exitt]

    #updating
    pickle.dump(rec,f)
    f2.write("BILLS")
    b = csv.writer(f3)
    b.writerow(rec)

    #closing files
    f.close()
    f2.close()
    f3.close()
    
    

#ONLY ENTRY SCREEN    
def entry():
    global fb
    print("ENTRY")
    f = open(fb,"ab")
    
    sno1 = sno()
    name = input("ENTER YOUR NAME:")
    
    while True:
          c = 0
          pno = input("ENTER YOUR PHONE NUM:")
          if pno.isdigit():
              if len(pno)== 10:
                  print("PHONE NUM VERIFIED")
                  c = 1
          if c == 1:
              break
          else:
              print("CANT VERIFY ,PLEASE REENTER YOUR PHONE NUM\n")  
              
    d1 = date()
    t1 = ptime()
    rec = [sno1,name,pno,d1,t1]
    print(rec)
    pickle.dump(rec,f)
    f.close()
    print("\n\n")
    print("YOUR SNO IS "+str(sno1
                             ))
    time.sleep(3)
    print("ENTRY PERMITTED")
    time.sleep(5)
    
   
    
    
    
#ONLY EXIT SCEEN    
def exitn():
    global fbe,fc,fw
    print("EXIT")
    
    while True:
        sno = int(input("ENTER YOUR SNO"))
        c = checks(sno)
        if c == False:
           print("CANNOT VERIFY THE SNO,PLEASE TRY AGAIN")
        else:
           print("SNO VERIFIED")
           break
           
    

    rec = c
    t = ptime()
    
    rec.append(t)

    
    
    f = open(fbe,"ab")
    f2 = open(fc,"a")
    b = csv.writer(f2)
    b.writerow(rec)
    pickle.dump(rec,f)
    f.close()
    f2.flush()
    f2.close()
    
    time.sleep(3)
    name = rec[1].capitalize()
    

    bill = "\nDRDO OFFICE PARKING\n\nSno:"+str(rec[0])+"\n\n"+"Name:"+str(name)+"\n"+"Phone No:"+"Verified"+"\n"+"Date:"+rec[3]+"\n"+"Entry:"+rec[4]+"\n"+"Exit:"+rec[5]+"\nTHANK YOU"
    print(bill)
    f3 = open(fw,"w")
    f3.write(bill)
    print("\n\nPLEASE TAKE YOUR BILL")
    f3.close()
    time.sleep(3)
    print("EXIT PERMITTED THANKYOU")
    time.sleep(5)
    print("\n"*10)
    
    
    
    
    
#decoration
def deco():
    print("___________________________________________\n\n\n______________________________________")
    

    
    
#MANAGING SCREEN
def manager():
    print("managing")
    print("PRESS 1 TO SEE ALL PREVIOUS PARKINGS(ENTRY+EXIT)")
    print("PRESS 2 FOR WRITE")
    print("PRESS 3 FOR UPDATE")
    print("PRESS 4 FOR DELETE")
    print("PRESS 5 TO SEE ALL PRESENT ENTRIES")
    print("PRESS 6 TO BACKUP THE DATA")
    print("PRESS 7 TO REMOVE EMPTY LIST FROM ENTRY")
    print("PRESS 11 FOR ENTRY SCREEN")
    print("PRESS 12 FOR EXIT SCREEN")
    print("PRESS 20 TO RETURN TO MAIN MENU")
    ch  = int(input("ENTER YOUR CHOOISE"))
    
    if  ch == 1:
        read()
    elif ch == 2:
        write()
    elif ch == 3:
        update()

    elif ch == 4:
        delete()
    elif ch == 5:
        readp()
    elif ch == 6:
        backup()
    elif ch == 7:
         delete_empty_list()
    elif ch == 11:
        entry()
    elif ch == 12:
        exitn()
    else:
        main()
        
     
        
#SNO GENERATOR
def sno():
    f = open(fb,"rb")
    sno = 0
    try:
        while True:
            rec = pickle.load(f)
            sno = rec[0] 

    except EOFError:
        f.close()
        sno = sno+1
        return sno
    

#TO MAKE SURE SNO IS ONLY USED ONCE TO EXIT/complex because deleting can cause lost of whole data    
def checks(s):
    f = open(fb,"rb")
    try:
        while True:
          rec = pickle.load(f)
          sno = rec[0]
          if s == sno:
             f.close()
             fg = 0
             f1 = open(fbe,"rb")
    
             try:
               while True:
                    rec1 = pickle.load(f1)
                    sno = rec1[0]
                    if s == sno:
                       return False
             except EOFError:
                  f.close()
                  return rec
                 
                
    except EOFError:
           return False

#TO READ ALL THE RECORDS(ENTRY+EXIT)        
def read():
    global fc
    f = open(fc,'r')
    b = csv.reader(f,delimiter = ',')
    for i in b:
        if i == []:
            continue
        else:
            print(i)
            
    print("All Records Printed")
    f.close

#TO WRITE A RECORD MANUALLY
def write():
    
    print("ADD ENTRY MANUALLY")
    name = input("Enter Name:")
    pno  = int(input("Enter PhoneNO:"))
    da = date()
    ti = ptime()
    sno1 = sno()
    global fb
    f = open(fb,'ab')
    
    rec = [sno1,name,pno,da,ti]
    pickle.dump(rec,f                )
    f.flush()
    f.close()
    print("RECORD IS ADDED")
    print("ALLOTED SNO IS:",sno1)


#IF DATA IS LOST,WE CAN USE SAVED DATA AS BACKUP    
def backup():
    global fbe, fb
    f = open(fbe,"rb")
    f2 = open(fb,"ab")
    try:
        while True:
          rec = pickle.load(f)
          pickle.dump(rec,f2)
          
                
    except EOFError:
           print("RECORDS BACKED UP")
    f.close()
    f2.close()
    
#TO DELETE ANY RECORD/ONLY POSSIBLE BEFORE EXIT    
def delete(sno = 0):
    global fb,ft
    if sno == 0:
       sno = int(input("Enter the sno of the record you want to delete:"))
    f = open(fb,"rb")
    f2 = open(ft,"ab")
    try:
        while True:
            rec = pickle.load(f)
            if rec[0] == sno:
                continue
            else:
                pickle.dump(rec,f2)
    except EOFError:
       print("RECORD DELETED,NOW THE PERSON MAY NOT BE ABLE TO EXIT THE PARKING")
       f.close()
       f2.close()
       os.remove(fb)
       os.rename(ft,fb)


def delete_empty_list():
    global fb,ft
   
    f = open(fb,"rb")
    f2 = open(ft,"ab")
    try:
        while True:
            rec = pickle.load(f)
            if rec == []:
                continue
            else:
                pickle.dump(rec,f2)
    except EOFError:
       print("RECORD DELETED,NOW THE PERSON MAY NOT BE ABLE TO EXIT THE PARKING")
       f.close()
       f2.close()
       os.remove(fb)
       os.rename(ft,fb)

       

#TO UPDATE ANY RECORD/ONLY POSSIBLE BEFOR EXIT
def update():
    global fb,ft
    print("RECORDS CAN ONLY BE UPDATED UNTIL CAR IS PARKED NOT AFTER THE EXIT")
    sno = int(input("Enter the sno you want to update"))
    f = open(fb,"rb")
    f2 = open(ft,"ab")
    try:
        while True:
            rec = pickle.load(f)
            if rec[0] == sno:
                print(rec)
                print("PRESS 1: FOR NAME")
                print("PRESS 2: FOR Pno")
                ch = int(input("ENTER YOUR CHOOISE"))
                if ch == 1:
                    name = input("ENTER NEW NAME")
                    rec[1] = name
                elif ch == 2:
                     pno = int(input("Enter Phoneno"))
                     rec[2] = pno
                pickle.dump(rec,f2)
            else:
                pickle.dump(rec,f2)
    except EOFError:
       print("RECORD UPDATED")
       f.close()
       f2.close()
       os.remove(fb)
       os.rename(ft,fb)

#TO READ THE RECORDS AFTER ENTRY
def readp():
    
    global fb
    f = open(fb,"rb")
    try:
        while True:
            
            rec = pickle.load(f)
            print(rec)
    except EOFError:
        print("ALL RECORDS PRINTED")
        f.close()
        

#variables
fw = "e:\\desktop\\parking\\bill.txt" #To print recipt
fb = "e:\\desktop\\parking\\parking.dat"#only entry records
fbe = "e:\\desktop\\parking\\exiting.dat"#after exit full record
fc = "e:\\desktop\\parking\\sheet.csv"#recods saves in excel after exit
ft = "e:\\desktop\\parking\\temp.dat"#for updating or deleting the records

main()
