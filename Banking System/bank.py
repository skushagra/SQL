import sqlite3
import sys
import random
# Creating SQLite Connection
conn = sqlite3.connect("card.s3db")
cur = conn.cursor()
# function to check validity
def check_card(newcn):
    tfcs = ""
    tfs = 0
    temp_cn = newcn[:-1]
    chsm = newcn[15]
    for i in range(len(temp_cn)):
        if i % 2 == 0:
            fchar = int(temp_cn[i]) * 2
            if fchar > 9:
                fchar -= 9
            tfcs += str(fchar)
        else:
             tfcs += temp_cn[i]
    for i in range(len(tfcs)):
        tfs += int(tfcs[i])
    fcs2 = tfs % 10
    if fcs2 == 0:
        cs = str(0)
    else:
        cs = str(10 - fcs2)
    if cs == chsm:
        return "Valid"
    else:
        return "Not Valid"



# Create card function
def create_account():
    iin = "400000"
    fcs = ""
    fs = 0
    cs = ""
    ain = int(random.randint(111111111,999999999))
    cn = iin + str(ain)
    for i in range(len(cn)):
        if i % 2 == 0:
            fchar = int(cn[i]) * 2
            if fchar > 9:
                fchar -= 9
            fcs += str(fchar)
        else:
             fcs += cn[i]
    for i in range(len(fcs)):
        fs += int(fcs[i])
    fcs2 = fs % 10
    if fcs2 == 0:
        cs = str(0)
    else:
        cs = str(10 - fcs2)
    iin = "400000"
    ncn = iin + str(ain) + cs
    temp_pin = int(random.randint(1111,9999))
    npin = str(temp_pin)
    print("Your card has beed created")
    lst = list()
    lst.extend([int(ncn), int(npin)])# Serial number | number | pin | balance
    cur.execute("INSERT INTO card (number, pin, balance) VALUES (?, ?,0)", lst)
    conn.commit()
    print("Your card number:")
    print(ncn)
    print("Your card PIN:")
    print(npin)
    print()
    front_end()
# Log in function
def log_in():

    print("Enter card number:")
    inp_cn = input()
    print("Enter your PIN:")
    inp_pin = input()
    cur.execute("Select * from card")
    all_info = cur.fetchall()
    for i in all_info:
        lst_or_cn = list()
        lst_or_cn.extend([int(inp_cn), int(inp_pin)])
        cur.execute("SELECT EXISTS(SELECT * from card where number = ? and pin = ?)",lst_or_cn)
        result1 = cur.fetchone()
        if result1[0] == 0:
            print("Wrong card number or PIN!")
            print()
            front_end()
        if int(i[1]) == int(inp_cn):
            if int(i[2]) == int(inp_pin):
                print()
                lst_for_cn = list()
                lst_for_cn.append(inp_cn)
                lst_for_pin = list()
                lst_for_pin.append(inp_pin)
                print("You have successfully logged in!")
                print()
                while True:
                    print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
                    ch = input()
                    if ch == "1":
                        cur.execute("SELECT balance from card where number = ? ",lst_for_cn)
                        bal_info = cur.fetchall()
                        for i in bal_info:
                            print()
                            print("Balance :",i[0])
                            print()
                            break
                    if ch == "2":
                        print()
                        print("Enter income:")
                        add_inc = int(input())
                        cur.execute("SELECT balance from card where number = ? ",lst_for_cn)
                        inc_info = cur.fetchall()
                        for i in inc_info:
                            cur_inc = i[0]
                            break
                        new_inc = int(cur_inc) + add_inc
                        lst_for_inc_and_num =  list()
                        lst_for_ninc = list()
                        lst_for_inc_and_num.extend([new_inc, inp_cn])
                        cur.execute("update card set balance = ? where number = ?",lst_for_inc_and_num)
                        conn.commit()
                        print("Income was added!")
                        print()
                    if ch == "3":
                        total_cards = 0
                        print()
                        print("Transfer")
                        print("Enter card number:")
                        inp_cn2 = input()
                        validiy = check_card(inp_cn2)

                        if validiy == "Not Valid":
                            print("Probably you made mistake in the card number. Please try again!")
                            print()
                        elif validiy == "Valid":
                            cur.execute("SELECT count(number) from card")
                            no = cur.fetchall()
                            for i in no:
                                total_cards = i[0]
                                break
                            cur.execute("SELECT number from card")
                            all_cards = cur.fetchall()
                            tc  = 0
                            for i in all_cards:
                                lst_for_cn2 = list()
                                lst_for_cn2.append(inp_cn2)
                                pon = cur.execute("SELECT EXISTS(SELECT * from card where number = ?)",lst_for_cn2)
                                pon = cur.fetchone()
                                # print(pon)
                                if pon[0] == 0 :
                                    print("Such a card does not exist.")
                                    print()
                                    break
                                # print(type(total_cards))
                                # print(all_cards[total_cards-1])
                                if tc <= total_cards:
                                    #print(i[0])
                                    if i[0] == inp_cn2:
                                        if inp_cn == inp_cn2:
                                            print("You can't transfer money to the same account!")
                                            print()
                                        else:
                                            print("Enter how much money do you want to transfer:")
                                            transfer_amt = input()
                                            temp_lst1 = list()
                                            temp_lst1.append(int(inp_cn))
                                            cur.execute("SELECT balance from card where number = ?",temp_lst1)
                                            ini_bal = cur.fetchall()
                                            usr_balance = 0
                                            for i in ini_bal:
                                                usr_balance = i[0]
                                            if int(transfer_amt) > int(usr_balance):
                                                print("Not enough money!")
                                                print()
                                            else:
                                                usr_balance = usr_balance - int(transfer_amt)
                                                lst = list()
                                                lst.extend([int(usr_balance), int(inp_cn)])
                                                cur.execute("UPDATE card set balance = ? where number = ?",lst)
                                                temp_lst2 = list()
                                                temp_lst2.append(int(inp_cn2))
                                                cur.execute("select balance from card where number = ?",temp_lst2)
                                                suser_bal = cur.fetchall()
                                                bal = 0
                                                for i in suser_bal:
                                                    bal = i[0]
                                                bal += int(transfer_amt)
                                                lst1 = list()
                                                lst1.extend([int(bal), int(inp_cn2)])
                                                cur.execute("UPDATE card set balance = ? where number = ?", lst1)
                                                conn.commit()
                                                print("Success!")
                                                print()
                                    tc += 1
                                elif tc > int(total_cards):
                                    print("Such a card does not exist")
                                    break
                    if ch == "4":
                        print()
                        temp_lst10 = list()
                        temp_lst10.append(int(inp_cn))
                        cur.execute("DELETE from card where number = ?",temp_lst10)
                        cur.fetchall()
                        conn.commit()
                        print("Your account has been closed!")
                        print()
                    if ch == "5":
                        print()
                        front_end()
                    if ch == "0":
                      print()
                      print("Bye!")
                      sys.exit()




# Front End function
def front_end():
    while True:
        print("1. Create Account\n2. Log into account\n0. Exit")
        choice = input()
        if choice == "1":
            print()
            create_account()
        elif choice == "2":
            print()
            result = log_in()
            if result == "0":
                return
        elif choice == "0":
            print()
            print("Bye!")
            sys.exit()
front_end()
conn.commit()
conn.close()
# 4000005203832473
# 1668

# 4000008898549394
# 7116