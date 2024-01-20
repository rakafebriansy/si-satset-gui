import csv
columns = []
admin_data = []
with open('Administrator.csv', 'r') as file:
        read, boolean = csv.reader(file), True
        for i in read:
            if boolean == True:
                columns = i
                boolean = False
                continue
            admin_data.append(i)
def Login(username,password) :
    for admin in admin_data:
        if admin[0] == username:
            if admin[1] == password:
                return True
    return False,'NAMA ATAU KATA SANDI SALAH!'
def Change(name,old_password,new_password):
    for admin in range(len(admin_data)):
        if admin_data[admin][0] == name and admin_data[admin][1] == old_password:
            admin_data[admin][1] = new_password
            with open('Administrator.csv', 'w', newline='') as file:
                write = csv.writer(file)
                write.writerow(columns)
                for admin in admin_data:
                    write.writerow(admin)
            return True
    return False
def Forgot(email,number,new_password):
    status = True
    for i in range(len(admin_data)):
        if admin_data[i][2] == email:
            if number == admin_data[i][3]:
                admin_data[i][1] = new_password
                with open('Administrator.csv', 'w', newline='') as file:
                    write = csv.writer(file)
                    write.writerow(columns)
                    for admin in admin_data:
                        write.writerow(admin)
                status = True
                break
            else:
                status = 'Nomor telepon tidak terdaftar.'
                break
        else:
            status = 'E-mail tidak terdaftar.'
    return status