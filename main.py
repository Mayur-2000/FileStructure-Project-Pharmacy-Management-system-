import os
from fpdf import FPDF

print("=" * 148)
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tMEDICURE PHARMACY")
print("=" * 148)


def login():
    print("\t\t\t\t\tLOGIN to Continue...")
    print("_" * 100)
    ch = int(input("Press 1 to login as Admin or Press 0 to login as Salesman: "))
    if ch == 1:
        while True:
            print("LOGIN as Admin:")
            username = "Admin"
            password = "Admin123"
            uname = input("Enter your Username: ")
            pword = input("Enter your password: ")
            if (uname == username) and (pword == password):
                print("LOGIN SUCCESSFULL")
                break
            else:
                print("LOGIN UNSUCCESSFULL")
                print("INVALID CREDENTIALS.... Please try again....")
                continue
        print("\n")
        menu()

    if ch == 0:
        while True:
            print("LOGIN as Salesman:")
            uname = input("Enter your Username: ")
            pword = input("Enter your password: ")
            file1 = open("Salesman Details.txt", "r")
            flag = 0
            index = 0
            for line in file1:
                index += 1
                if uname in line:
                    flag = 1
                    break
            if flag == 0:
                print("You are not a registered salesman with us")
            else:
                with open("Salesman Details.txt") as f:
                    lines = f.readlines()
                    str1 = lines[index - 1]
                    lst1 = str1.split(" ")
                    if ((uname == lst1[3]) and (pword == lst1[4])):
                        print("LOGIN SUCCESSFULL")
                        menu1()
                        break
                    else:
                        print("LOGIN UNSUCCESSFULL")
                        print("INVALID CREDENTIALS.... Please try again....")
                        continue
        file1.close()
        j = 1
        bill_medicine(j)
        bill_medicine1(j)


def menu():
    print("=" * 70)
    print("Menu Bar...")
    print("=" * 70)
    print("Select an Action to Continue:")
    print("1. Add medicine details")
    print("2. Delete medicine details")
    print("3. Modify Medicine details")
    print("4. Search Medicine details")
    print("5. Search by Index Medicine details")
    print("6. View Medicines")
    print("7. Make a Bill")
    print("8. Print a Bill in pdf")
    print("9. Register salesman")
    print("10. Remove salesman")
    print("11. Log out as Salesman")
    print("12. Log out as Admin")
    print("")
    num = int(input("Enter your choice: "))
    print("")
    if (num == 1):
        add_medicine()
        return
    if (num == 2):
        delete_medicine()
        return
    if (num == 3):
        update_medicine()
        return
    if (num == 4):
        search_medicine()
        return
    if (num == 5):
        search_by_index_medicine()
        return
    if (num == 6):
        view_all_medicine()
        return
    if (num == 7):
        j = 1
        bill_medicine(j)
        return
    if (num == 8):
        printfile()
        return
    if (num == 9):
        reg_salesman()
        return
    if (num == 10):
        delete_salesman()
        return
    if (num == 11):
        log_out()
        return
    if (num == 12):
        log_out()
        return

def menu1():
    print("=" * 70)
    print("Menu Bar...")
    print("=" * 70)
    print("Select an Action to Continue:")
    print("13. Search Medicine details")
    print("14. Search by Index Medicine details")
    print("15. View Medicines")
    print("16. Make a Bill")
    print("17. Print a Bill in pdf")
    print("11. Log out as Salesman")
    print("")
    num = int(input("Enter your choice: "))
    print("")

    if (num == 13):
        search_medicine1()
        return
    if (num == 14):
        search_by_index_medicine1()
        return
    if (num == 15):
        view_all_medicine1()
        return
    if (num == 16):
        j = 1
        bill_medicine1(j)
        return
    if (num == 17):
        printfile1()
        return
    if (num == 11):
        log_out()
        return


def add_medicine():
    print("=" * 70)
    print("Add new Medicine")
    print("=" * 70)
    print("Enter new Medicine details")
    print("")
    while True:
        name = input("Enter name: ")
        company = input("Enter manufacturer company: ")
        price = input("Enter price of 1 unit: ")
        quantity = str(float(input("Enter no of units: ")))
        mfgdate = input("Enter manufacture date {dd/mm/yyyy}: ")
        expdate = input("Enter expiry date {dd/mm/yyyy}: ")
        print("")
        add_medicine = open("Medicine Details.txt", "a")
        record = name + " " + company + " " + price + " " + quantity + " " + mfgdate + " " + expdate
        add_medicine.write(record)
        add_medicine.write("\n")
        add_medicine.close()
        test = int(input("Press 1 to continue add medicines or Press 0 to exit: "))
        if test == 1:
            print("")
            continue
        else:
            break
    menu()


def delete_medicine():
    file1 = open("Medicine Details.txt", "r")
    tempfile = open("Del Med Det.txt", "w")
    delmed = input("Enter medicine name to delete: ")
    s = ' '
    while s:
        s = file1.readline()
        L = s.split(" ")
        if len(s) > 0:
            if L[0] != delmed:
                tempfile.write(s)
    tempfile.close()
    file1.close()
    os.remove("Medicine Details.txt")
    os.rename("Del Med Det.txt", "Medicine Details.txt")
    test = int(input("Press 1 to continue delete medicine or Press 0 to exit: "))
    if test == 1:
        delete_medicine()
    else:
        menu()


def update_medicine():
    string1 = input("Enter medicine to update:")
    file1 = open("Medicine Details.txt", "r")
    flag = 0
    index = 0
    for line in file1:
        index += 1
        if string1 in line:
            lt = line.split(" ")
            if string1 == lt[0]:
                flag = 1
                break
    if flag == 0:
        print('Medicine', string1, 'Not Found')
    else:
        print('Medicine', string1, 'Found In Line', index)
        with open("Medicine Details.txt") as f:
            lines = f.readlines()
            str1 = lines[index - 1]
            lines.remove(str1)
            lst1 = str1.split(" ")
            print("Select Action to Modify the Medicine Details: ")
            print("1. Modify Price per Unit")
            print("2. Modify Quantity")
            print("3. Modify Manufacture Date")
            print("4. Modify Expiry Date")
            ch1 = int(input("Enter your choice: "))
            if ch1 == 1:
                pr = input("Enter the new price: ")
                lst1[2] = pr
            if ch1 == 2:
                qt = input("Enter the new quantity: ")
                lst1[3] = qt
            if ch1 == 3:
                mfg = input("Enter the new manufacture date: ")
                lst1[4] = mfg
            if ch1 == 4:
                exp = input("Enter the new expiry date: ")
                lst1[5] = exp
            strg = " ".join(lst1)
            lines.append(strg)
            udate_medicine = open("Medicine Details.txt", "w")
            udate_medicine.truncate(0)
            for item in lines:
                udate_medicine.write(item)
            udate_medicine.close()
    file1.close()
    test = int(input("Press 1 to continue search medicine or Press 0 to exit: "))
    if test == 1:
        update_medicine()
    else:
        menu()


def search_medicine():
    string1 = input("Enter medicine to search:")
    file1 = open("Medicine Details.txt", "r")
    flag = 0
    index = 0
    for line in file1:
        index += 1
        if string1 in line:
            flag = 1
            break
    if flag == 0:
        print('Medicine', string1, 'Not Found')
    else:
        print('Medicine', string1, 'Found In Line', index)
        with open("Medicine Details.txt") as f:
            lines = f.readlines()
            str1 = lines[index - 1]
            lst1 = str1.split(" ")
            print("Medicine Name: " + lst1[0] + " | Manufacturer: " + lst1[1] + " | Price per Unit: " + lst1[
                2] + " | Quantity left(in units): " + lst1[3] + " | Manufacture Date: " + lst1[4] + " | Expiry Date:" +
                  lst1[5])
    file1.close()
    test = int(input("Press 1 to continue search medicine or Press 0 to exit: "))
    if test == 1:
        search_medicine()
    else:
        menu()

#function for salesman
def search_medicine1():
    string1 = input("Enter medicine to search:")
    file1 = open("Medicine Details.txt", "r")
    flag = 0
    index = 0
    for line in file1:
        index += 1
        if string1 in line:
            flag = 1
            break
    if flag == 0:
        print('Medicine', string1, 'Not Found')
    else:
        print('Medicine', string1, 'Found In Line', index)
        with open("Medicine Details.txt") as f:
            lines = f.readlines()
            str1 = lines[index - 1]
            lst1 = str1.split(" ")
            print("Medicine Name: " + lst1[0] + " | Manufacturer: " + lst1[1] + " | Price per Unit: " + lst1[
                2] + " | Quantity left(in units): " + lst1[3] + " | Manufacture Date: " + lst1[4] + " | Expiry Date:" +
                  lst1[5])
    file1.close()
    test = int(input("Press 1 to continue search medicine or Press 0 to exit: "))
    if test == 1:
        search_medicine1()
    else:
        menu1()


def search_by_index_medicine():
    try:
        key = int(input("Enter the record number to retrieve: "))  # 1-n
        if key <= 0:
            print("Record not Found")
        else:
            with open("Medicine Details.txt") as f:
                lines = f.readlines()
                keyRecord = lines[key - 1]
                lst = keyRecord.split(" ")
                print("Medicine Name: " + lst[0] + " | Manufacturer: " + lst[1] + " | Price per Unit: " + lst[
                    2] + " | Quantity left(in units): " + lst[3] + " | Manufacture Date: " + lst[4] + " | Expiry Date:" +
                      lst[5])
            f.close()
    except:
        print("Record not found ")
    finally:
        test = int(input("Press 1 to continue search medicine by index or Press 0 to exit: "))
        if test == 1:
            search_by_index_medicine()
        else:
            menu()


#function for salesman
def search_by_index_medicine1():
    try:
        key = int(input("Enter the record number to retrieve: "))  # 1-n
        if key <= 0:
            print("Record not Found")
        else:
            with open("Medicine Details.txt") as f:
                lines = f.readlines()
                keyRecord = lines[key - 1]
                lst = keyRecord.split(" ")
                print("Medicine Name: " + lst[0] + " | Manufacturer: " + lst[1] + " | Price per Unit: " + lst[
                    2] + " | Quantity left(in units): " + lst[3] + " | Manufacture Date: " + lst[4] + " | Expiry Date:" +
                      lst[5])
            f.close()
    except:
        print("Record not found ")
    finally:
        test = int(input("Press 1 to continue search medicine by index or Press 0 to exit: "))
        if test == 1:
            search_by_index_medicine1()
        else:
            menu1()



def view_all_medicine():
    with open("Medicine Details.txt") as f:
        lines = f.readlines()
        for line in lines:
            lst1 = line.split(" ")
            print("Medicine Name: " + lst1[0] + " | Manufacturer: " + lst1[1] + " | Price per Unit: " + lst1[
                2] + " | Quantity left(in units): " + lst1[3] + " | Manufacture Date: " + lst1[4] + " | Expiry Date:" +
                  lst1[5])
    f.close()
    menu()

#function for salesman
def view_all_medicine1():
     with open("Medicine Details.txt") as f:
         lines = f.readlines()
         for line in lines:
             lst1 = line.split(" ")
             print("Medicine Name: " + lst1[0] + " | Manufacturer: " + lst1[1] + " | Price per Unit: " + lst1[
                 2] + " | Quantity left(in units): " + lst1[3] + " | Manufacture Date: " + lst1[4] + " | Expiry Date:" +
                   lst1[5])
     f.close()
     menu1()


def bill_medicine(j):
    while True:
        print("=" * 70)
        print("Welcome to BILLING section...")
        print("=" * 70)
        c_name = input("Enter the customer name: ")
        c_billdate = input("Enter today's date {dd/mm/yyyy}: ")
        i = 1
        item_list = {}
        var = int(input("Enter the number of items: "))
        for i in range(var):
            item_name = input("Enter " + str(i + 1) + " Medicine: ")
            if item_name == "-":
                break
            file1 = open("Medicine Details.txt", "r")
            flag = 0
            index = 0
            for line in file1:
                index += 1
                if item_name in line:
                    flag = 1
                    break
            if flag == 0:
                print('Medicine', item_name, 'Not Found')
                continue
            item_qnty = int(input("Enter the number of units required: "))
            file1 = open("Medicine Details.txt", "r")
            flag1 = 0
            index1 = 0
            for line1 in file1:
                index1 += 1
                if item_name in line1:
                    flag1 = 1
                    break
            if flag1 == 1:
                with open("Medicine Details.txt") as f:
                    lines = f.readlines()
                    str1 = lines[index1 - 1]
                    lines.remove(str1)
                    lst1 = str1.split(" ")
                left = (float(lst1[3]) - float(item_qnty))
                lst1[3] = str(left)
                strg = " ".join(lst1)
                lines.append(strg)
                udate_medicine = open("Medicine Details.txt", "w")
                udate_medicine.truncate(0)
                for item in lines:
                    udate_medicine.write(item)
                udate_medicine.close()
            item_list[item_name] = item_qnty

        print("Total items: " + str(len(item_list)))
        dict_bill = {}
        for item, value in item_list.items():
            file1 = open("Medicine Details.txt", "r")
            flag = 0
            index = 0
            for line in file1:
                index += 1
                if item in line:
                    flag = 1
                    break
            if flag == 0:
                print('Medicine not found', item, 'Not Found')
            else:
                with open("Medicine Details.txt") as f:
                    lines = f.readlines()
                    str1 = lines[index - 1]
                    lst1 = str1.split(" ")
                n = float(lst1[2]) * float(value)
                dict_bill[item] = n
        total = 0
        for item, value in dict_bill.items():
            print(item + ("==" * 30) + str(value))
            total = total + value
        print("TOTAL AMOUNT TO BE PAID: " + str(total))
        file1.close()

        bill_item = open("Bill " + str(j) + ".txt", "w")
        bill_item.write(("==" * 30) + "\n")
        bill_item.write(("\t" * 5) + "BILL DETAILS\n")
        bill_item.write(("==" * 30) + "\n")
        bill_item.write("CUSTOMER NAME: " + c_name + "\n")
        bill_item.write("DATE OF BILLING: " + c_billdate + "\n")
        bill_item.write(("==" * 30) + "\n")
        bill_item.write(("==" * 30) + "\n")
        bill_item.write("Item" + ("\t" * 6) + "Price")
        bill_item.write(("\n"))
        for item, value in dict_bill.items():
            bill_item.write(item + ("\t" * 7) + str(value))
            bill_item.write(("\n"))
        bill_item.write("TOTAL AMOUNT TO BE PAID: " + str(total))
        bill_item.write(("\n"))
        bill_item.write("*******************************END OF BILLING******************************\n")
        bill_item.write("*******************GOODS ONCE SOLD WILL NOT BE TAKEN BACK******************\n")
        bill_item.write("***********************THANK YOU         VISIT AGAIN **********************\n")
        bill_item.close()
        test = int(input("Press 1 to continue billing or 0 to exit: "))
        if test == 1:
            j = j + 1
            bill_medicine(j)
        else:
            break
    menu()



#function for salesman
def bill_medicine1(j):
    while True:
        print("=" * 70)
        print("Welcome to BILLING section...")
        print("=" * 70)
        c_name = input("Enter the customer name: ")
        c_billdate = input("Enter today's date {dd/mm/yyyy}: ")
        i = 1
        item_list = {}
        var = int(input("Enter the number of items: "))
        for i in range(var):
            item_name = input("Enter " + str(i + 1) + " Medicine: ")
            if item_name == "-":
                break
            file1 = open("Medicine Details.txt", "r")
            flag = 0
            index = 0
            for line in file1:
                index += 1
                if item_name in line:
                    flag = 1
                    break
            if flag == 0:
                print('Medicine', item_name, 'Not Found')
                continue
            item_qnty = int(input("Enter the number of units required: "))
            file1 = open("Medicine Details.txt", "r")
            flag1 = 0
            index1 = 0
            for line1 in file1:
                index1 += 1
                if item_name in line1:
                    flag1 = 1
                    break
            if flag1 == 1:
                with open("Medicine Details.txt") as f:
                    lines = f.readlines()
                    str1 = lines[index1 - 1]
                    lines.remove(str1)
                    lst1 = str1.split(" ")
                left = (float(lst1[3]) - float(item_qnty))
                lst1[3] = str(left)
                strg = " ".join(lst1)
                lines.append(strg)
                udate_medicine = open("Medicine Details.txt", "w")
                udate_medicine.truncate(0)
                for item in lines:
                    udate_medicine.write(item)
                udate_medicine.close()
            item_list[item_name] = item_qnty

        print("Total items: " + str(len(item_list)))
        dict_bill = {}
        for item, value in item_list.items():
            file1 = open("Medicine Details.txt", "r")
            flag = 0
            index = 0
            for line in file1:
                index += 1
                if item in line:
                    flag = 1
                    break
            if flag == 0:
                print('Medicine not found', item, 'Not Found')
            else:
                with open("Medicine Details.txt") as f:
                    lines = f.readlines()
                    str1 = lines[index - 1]
                    lst1 = str1.split(" ")
                n = float(lst1[2]) * float(value)
                dict_bill[item] = n
        total = 0
        for item, value in dict_bill.items():
            print(item + ("==" * 30) + str(value))
            total = total + value
        print("TOTAL AMOUNT TO BE PAID: " + str(total))
        file1.close()

        bill_item = open("Bill " + str(j) + ".txt", "w")
        bill_item.write(("==" * 30) + "\n")
        bill_item.write(("\t" * 5) + "BILL DETAILS\n")
        bill_item.write(("==" * 30) + "\n")
        bill_item.write("CUSTOMER NAME: " + c_name + "\n")
        bill_item.write("DATE OF BILLING: " + c_billdate + "\n")
        bill_item.write(("==" * 30) + "\n")
        bill_item.write(("==" * 30) + "\n")
        bill_item.write("Item" + ("\t" * 6) + "Price")
        bill_item.write(("\n"))
        for item, value in dict_bill.items():
            bill_item.write(item + ("\t" * 7) + str(value))
            bill_item.write(("\n"))
        bill_item.write("TOTAL AMOUNT TO BE PAID: " + str(total))
        bill_item.write(("\n"))
        bill_item.write("*******************************END OF BILLING******************************\n")
        bill_item.write("*******************GOODS ONCE SOLD WILL NOT BE TAKEN BACK******************\n")
        bill_item.write("***********************THANK YOU         VISIT AGAIN **********************\n")
        bill_item.close()
        test = int(input("Press 1 to continue billing or 0 to exit: "))
        if test == 1:
            j = j + 1
            bill_medicine1(j)
        else:
            break
    menu1()


def printfile():
    filename = input("Enter the file name: ")
    filecon = (filename + ".txt")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    f = open(filecon, "r")
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')
    pdf.output(filename + ".pdf")


#function for salesman
def printfile1():
    filename = input("Enter the file name: ")
    filecon = (filename + ".txt")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    f = open(filecon, "r")
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')
    pdf.output(filename + ".pdf")


def reg_salesman():
    print("=" * 70)
    print("Register new Salesman")
    print("=" * 70)
    print("Enter new Salesman details")
    while True:
        id = input("Enter ID: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        s_username = input("Enter salesman username: ")
        s_password = input("Enter salesman password: ")
        qualification = input("Enter qualification: ")
        phno = input("Enter Phone No:")
        salesman_details = open("Salesman Details.txt", "a")
        salesman_details.writelines(
            [id + " ", name + " ", age + " ", s_username + " ", s_password + " ", qualification + " ", phno + "\n"])
        salesman_details.close()
        test = int(input("Press 1 to continue or 0 to exit: "))
        if test == 1:
            continue
        else:
            break
    menu()


def delete_salesman():
    file1 = open("Salesman Details.txt", "r")
    tempfile = open("Del Sale Det.txt", "w")
    delsale = input("Enter salesman id to delete: ")
    s = ' '
    while s:
        s = file1.readline()
        L = s.split(" ")
        if len(s) > 0:
            if L[0] != delsale:
                tempfile.write(s)
    tempfile.close()
    file1.close()
    os.remove("Salesman Details.txt")
    os.rename("Del Sale Det.txt", "Salesman Details.txt")
    test = int(input("Press 1 to continue delete medicine or Press 0 to exit: "))
    if test == 1:
        delete_salesman()
    else:
        menu()


def log_out():
    exit(0)


login()