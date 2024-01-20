import tkinter as tk, csv, Password, ShortestPath, Sorting, Searching, Knapsack
from tkinter import messagebox,ttk
from PIL import ImageTk, Image

#PRE PROCESS
def CheckLogin(bin): #RAKA
    username = bin[4].get()
    password = bin[5].get()
    region = var3.get()
    if username == '' or username == ' Nama pengguna':
        messagebox.showwarning("Peringatan", "Nama pengguna tidak boleh kosong.")
    elif password == '' or password == ' Kata sandi':
        messagebox.showwarning("Peringatan", "Kata sandi tidak boleh kosong.")
    else:
        authentication = Password.Login(username,password)
        if authentication == True:
            global Items, Columns
            Items,Columns = [],[]
            with open(f'{region}.csv', 'r') as file:
                read, index = csv.reader(file), 0
                for i in read:
                    if index == 0:
                        Columns,index = i,1
                        continue
                    Items.append(i)
            MainMenu(Items,Columns,region,bin,username,0)
        else:
            messagebox.showerror("Gagal", "Nama pengguna atau Kata sandi salah.")

def CreateTable(window,items,columns): #DINAR/DEVINA
    columns.insert(0,'No')
    table_frame = tk.Frame(window)
    table_frame.place(relx=0.12,y=40,height=548)
    table = ttk.Treeview(table_frame)
    headingStyle = ttk.Style()
    columnStyle = ttk.Style()
    headingStyle.configure('Treeview.Heading',font=('Montserrat',10))
    columnStyle.configure('Treeview',font=('Montserrat',10))
    table['columns'] = columns
    table.column('#0', width=0, stretch=tk.NO)
    for column in columns:
        table.column(column, anchor=tk.CENTER, width=110)
    table.heading('#0', text='', anchor=tk.CENTER)
    for column in columns:
        table.heading(column, text=column, anchor=tk.CENTER)
    for i in range(len(items)):
        items[i].insert(0,i+1)
        table.insert(parent='', index='end', iid=i, text='', values=items[i])
        items[i].remove(i+1)
    columns.remove('No')
    table.pack(side='right',fill='both')
    return table_frame

def Exit(bin): #FEBY
    box_exit = messagebox.askokcancel('Keluar','Apakah anda yakin?')
    if box_exit == True:
        for i in bin:
            i.destroy()
        SignInPage()

def MainMenu(items,columns,region,bin,username,choice=None,message=None): #DINAR/DEVINA/FEBY/FAQIH
    for i in bin:
        i.destroy()
    bin = []
    button_frame = tk.Frame(root,width=130,height=600)
    button_frame.pack(side='left', fill='y')
    button1 = tk.Button(button_frame,font=('Montserrat',10), text="Pengiriman Barang",bg='#c9c9c9',command=lambda:MainMenu(items,columns,region,bin,username,1))
    button1.place(x=5,y=40,width=130)
    button2 = tk.Button(button_frame,font=('Montserrat',10), text="Manajemen Gudang",bg='#c9c9c9',command=lambda:CRUDMenu(items,columns,region,bin,username))
    button2.place(x=5,y=80,width=130)
    button3 = tk.Button(button_frame,font=('Montserrat',10), text=" Ubah Kata sandi ",bg='#c9c9c9',command=lambda:MainMenu(items,columns,region,bin,username,3))
    button3.place(x=5,y=120,width=130)
    button4 = tk.Button(button_frame,font=('Montserrat',10), text="Credits",bg='#c9c9c9', command=lambda:MainMenu(items,columns,region,bin,username,5))
    button4.place(x=5,y=160,width=130)
    button5 = tk.Button(button_frame,font=('Montserrat',10), text="Keluar",bg='red',fg='white', command=lambda:Exit(bin))
    button5.place(x=5,y=560,width=130)

    bin.append(button_frame)
    bin.append(button1)
    bin.append(button2)
    bin.append(button3)
    bin.append(button4)
    bin.append(button5)
    
    if choice == 1:
        input_frame = tk.Frame(root,relief=tk.GROOVE, bd=3)
        input_frame.place(relx=0.12,y=5)
        input_frame.columnconfigure(0,weight=1)
        input_frame.columnconfigure(1,weight=1)
        input_frame.columnconfigure(2,weight=1)
        input_frame.columnconfigure(3,weight=1)
        input_frame.columnconfigure(4,weight=1)
        entry_kotaKeberangkatan = tk.Entry(input_frame,font=('Montserrat',10))
        entry_kotaKeberangkatan.grid(column=1,row=0,sticky='we')
        entry_kotaTujuan = tk.Entry(input_frame,font=('Montserrat',10))
        entry_kotaTujuan.grid(column=3,row=0,sticky='we')
        label_kotaKeberangkatan = tk.Label(input_frame,text='Kota keberangkatan',font=('Montserrat',10))
        label_kotaKeberangkatan.grid(column=0,row=0)
        label_kotaTujuan = tk.Label(input_frame,text='      Kota tujuan',font=('Montserrat',10))
        label_kotaTujuan.grid(column=2,row=0)
        button_knapsack = tk.Button(input_frame, text='Ajukan pengiriman',font=('Montserrat',10),bg='#c9c9c9', command=lambda:SendGoods(items,columns,region,bin,username))
        button_knapsack.grid(column=4,row=0, sticky='e',padx=3)

        bin.insert(0,entry_kotaKeberangkatan)
        bin.insert(1,entry_kotaTujuan)
        bin.append(label_kotaKeberangkatan)
        bin.append(input_frame)
        bin.append(entry_kotaTujuan)
        bin.append(button_knapsack)
    
    elif choice == 3:
        var1.set('Kata sandi lama')
        var2.set('Kata sandi baru')
        changePassword = tk.Label(button_frame,font=('Montserrat',10),text='Gunakanlah\nkombinasi kata\nsandi yang kuat!')
        changePassword.place(x=5,y=200,width=130)
        entry_oldPassword = tk.Entry(button_frame,font=('Montserrat',10),fg='grey',textvariable=var1)
        entry_oldPassword.place(x=5,y=260,width=130)
        entry_oldPassword.bind('<FocusIn>',oldPasswordBind)
        entry_oldPassword.bind('<FocusOut>',oldPasswordBind)
        entry_newPassword = tk.Entry(button_frame,font=('Montserrat',10),fg='grey',textvariable=var2)
        entry_newPassword.place(x=5,y=280,width=130)
        entry_newPassword.bind('<FocusIn>',newPasswordBind)
        entry_newPassword.bind('<FocusOut>',newPasswordBind)
        button_cancelChange = tk.Button(button_frame,text='Batal',font=('Montserrat',10),bg='#c9c9c9',command=lambda:MainMenu(items,columns,region,bin,username))
        button_cancelChange.place(x=10,y=310,width=50)
        button_doChange = tk.Button(button_frame,text='Ganti',font=('Montserrat',10),bg='#c9c9c9',command=lambda:ChangePassword(items,columns,region,bin,username))
        button_doChange.place(x=75,y=310,width=50)

        bin.append(changePassword)
        bin.append(button_cancelChange)
        bin.append(button_doChange)
        bin.insert(0,entry_oldPassword)
        bin.insert(1,entry_newPassword)

    elif choice == 0:
        label_welcome = tk.Label(root,font='Montserrat 12 bold',text=f'Selamat datang {username.capitalize()} !')
        label_welcome.place(relx=0.12,y=7)
        bin.append(label_welcome)

    table_frame = CreateTable(root,items,columns)
    bin.append(table_frame)

    if choice == 5:
        tk.Label(root,font='Poppins 12 bold',text='Developed by').place(x=5,y=210)
        tk.Label(root,font='Montserrat 10',text='@rakafebriansy',fg='green').place(x=5,y=240)

    if choice == 2:
        messagebox.showinfo("Pemberitahuan",message)
    elif choice == 4:
        messagebox.showinfo("Pemberitahuan",message)

    choice = None
    root.mainloop()

def SendGoods(items,columns,region,bin,username,kotaKeberangkatan=None,kotaTujuan=None): #DINAR/DEVINA/FEBY/FAQIH
    if kotaKeberangkatan == None and kotaTujuan == None:
        kotaKeberangkatan,kotaTujuan = bin[0].get(),bin[1].get()
    selected_items = Searching.SendSearch(items,6,7,kotaKeberangkatan,kotaTujuan)
    if kotaKeberangkatan == '' or kotaTujuan == '':
        messagebox.showwarning("Peringatan", "Data tidak boleh kosong.")
    elif selected_items == False:
        messagebox.showerror("Peringatan", "Data tidak ditemukan.")
    else:
        for i in bin:
            i.destroy()
        bin = []
        knapsacked_items = Knapsack.Greedy(selected_items)
        button_frame = tk.Frame(root,width=130,height=600)
        button_frame.pack(side='left', fill='y')
        button1 = tk.Button(button_frame, text="Kirim",bg='#4F9BFC',fg='white',font=('Montserrat',10), command=lambda:SendIt(items,columns,region,bin,username,kotaKeberangkatan,kotaTujuan,selected_items))
        button1.place(x=5,y=40,width=130)
        button2 = tk.Button(button_frame, text="Tampilkan peta",bg='#c9c9c9',font=('Montserrat',10), command=lambda:Dijkstra(items,columns,region,bin,username,kotaKeberangkatan,kotaTujuan))
        button2.place(x=5,y=80,width=130)
        button3 = tk.Button(button_frame, text="Kembali",bg='#c9c9c9',font=('Montserrat',10), command=lambda:MainMenu(items,columns,region,bin,username))
        button3.place(x=5,y=560,width=130)

        table_frame = CreateTable(root,knapsacked_items,columns)

        bin.append(button_frame)
        bin.append(button1)
        bin.append(button2)
        bin.append(button3)
        bin.append(table_frame)
        root.mainloop()

def Dijkstra(items,columns,region,bin,username,kotaKeberangkatan,kotaTujuan): #RAKA
    listEdge, listNode = ShortestPath.DataInput(region)
    idKeberangkatan, idTujuan = '',''
    for i in range(len(listNode)):
        if listNode[i].split('.')[0].lower() == kotaKeberangkatan.lower():
            idKeberangkatan = int(i)
        if listNode[i].split('.')[0].lower() == kotaTujuan.lower():
            idTujuan = int(i)

    for i in bin:
        i.destroy()
    button_frame = tk.Frame(root,width=130,height=600)
    button_frame.pack(side='left', fill='y')
    button1 = tk.Button(button_frame, text="Kembali",bg='#c9c9c9',font=('Montserrat',10), command=lambda:SendGoods(items,columns,region,bin,username,kotaKeberangkatan,kotaTujuan))
    button1.place(x=5,y=560,width=130)

    canvas = tk.Canvas(root, width=1000,height=800,)
    canvas.pack(side='right',fill='both')

    sorted_table = ShortestPath.TotalWeight(listEdge,idKeberangkatan,idTujuan)
    sorted_table = ShortestPath.MinimumWeight(sorted_table)
    list_coordinate = []
    coordinates = []
    for node in listNode:
        label = node.split('.')[0]
        Xaxis = int(node.split('.')[1])
        Yaxis = int(node.split('.')[2])
        list_coordinate.append([Xaxis,Yaxis])
        canvas.create_oval(Xaxis-5,Yaxis-5,Xaxis+5,Yaxis+5,fill='black')
        canvas.create_text(Xaxis-20,Yaxis-20,text=str(label),fill='black')
    for i in listEdge.keys():
        for j in listEdge[i].keys():
            coordinate = [i,j,listEdge[i][j]]
            coordinates.append(coordinate)
    for k in coordinates:
        for l in range(len(k)-1):
            k[l] = list_coordinate[k[l]]
    for j in range(len(sorted_table[0])):
        sorted_table[0][j] = list_coordinate[sorted_table[0][j]]
    all_paths, shortest_path = coordinates, sorted_table[0]

    for i in range(len(all_paths)):
        Xaxis1, Yaxis1, Xaxis2, Yaxis2 = all_paths[i][0][0], all_paths[i][0][1], all_paths[i][1][0], all_paths[i][1][1]
        canvas.create_line(Xaxis1, Yaxis1, Xaxis2, Yaxis2, fill='black')
        canvas.create_text((Xaxis1+Xaxis2)/2,(Yaxis1+Yaxis2)/2,text=str(all_paths[i][2]),fill='black')
    for i in range(len(shortest_path)-1):
        if i == len(shortest_path)-2:
            canvas.create_oval(shortest_path[i+1][0]-5, shortest_path[i+1][1]-5, shortest_path[i+1][0]+5, shortest_path[i+1][1]+5,fill='orange')
        canvas.create_oval(shortest_path[i][0]-5, shortest_path[i][1]-5, shortest_path[i][0]+5, shortest_path[i][1]+5,fill='orange')
        canvas.create_line(shortest_path[i][0], shortest_path[i][1], shortest_path[i+1][0], shortest_path[i+1][1], fill='orange')
    bin.append(button_frame)
    bin.append(button1)
    bin.append(canvas)
    root.mainloop()

def SendIt(items,columns,region,bin,username,kotaKeberangkatan,kotaTujuan,selected_items): #FEBY/FAQIH
    with open(f'{region}.csv', 'w',newline='') as file:
        write = csv.writer(file)
        write.writerow(columns)
        for item in selected_items:
            if item[6].lower() == kotaKeberangkatan.lower() and item[7].lower() == kotaTujuan.lower():
                Items.remove(item)
        for item in Items:
            write.writerow(item)
    MainMenu(items,columns,region,bin,username,2,'Barang telah dihapus dari database\ndan siap dikirimkan.')
    
def ChangePassword(items,columns,region,bin,username): #FEBY/FAQIH
    old_password,new_password = bin[0].get(),bin[1].get()
    if old_password == '' or old_password == 'Kata sandi lama' or new_password == '' or new_password == 'Kata sandi baru':
        messagebox.showwarning('Peringatan','Kata sandi tidak boleh kosong.')
    else:
        result = Password.Change(username,old_password,new_password)
        if result == True:
            message = "Kata sandi telah diperbarui."
            MainMenu(items,columns,region,bin,username,4,message)
        else:
            messagebox.showerror("Gagal", "Kata sandi salah.")
        
def CRUDMenu(items,columns,region,bin,username,choice=''): #DINAR/DEVINA/FEBY/FAQIH
    for i in bin:
        i.destroy()
    bin = []
    button_frame = tk.Frame(root,width=130,height=600)
    button_frame.pack(side='left', fill='y')
    button1 = tk.Button(button_frame,font=('Montserrat',10),bg='#c9c9c9',text="       Urutkan data      ",command=lambda:CRUDMenu(items,columns,region,bin,username,1))
    button1.place(x=5,y=40,width=130)
    button2 = tk.Button(button_frame,font=('Montserrat',10),bg='#c9c9c9', text="Cari data",command=lambda:CRUDMenu(items,columns,region,bin,username,2))
    button2.place(x=5,y=80,width=130)
    button3 = tk.Button(button_frame,font=('Montserrat',10),bg='#c9c9c9', text="Ubah data",command=lambda:CRUDMenu(items,columns,region,bin,username,3))
    button3.place(x=5,y=120,width=130)
    button4 = tk.Button(button_frame,font=('Montserrat',10),bg='#c9c9c9', text="Refresh", command=lambda:CRUDMenu(Items,columns,region,bin,username))
    button4.place(x=5,y=160,width=130)
    button5 = tk.Button(button_frame,font=('Montserrat',10),bg='#c9c9c9', text="Kembali", command=lambda:MainMenu(items,columns,region,bin,username))
    button5.place(x=5,y=560,width=130)

    bin.append(button_frame)
    bin.append(button1)
    bin.append(button2)
    bin.append(button3)
    bin.append(button4)
    bin.append(button5)

    if choice == 1:
        input_frame = tk.Frame(root,relief=tk.GROOVE, bd=3)
        input_frame.place(relx=0.12,y=5)
        input_frame.columnconfigure(0,weight=1)
        input_frame.columnconfigure(1,weight=1)
        input_frame.columnconfigure(2,weight=1)
        input_frame.columnconfigure(3,weight=1)
        input_frame.columnconfigure(4,weight=1)
        entry_pilihKolom = tk.Entry(input_frame,font=('Montserrat',10))
        entry_pilihKolom.grid(column=1,row=0,sticky='we')
        label_pilihKolom = tk.Label(input_frame,font=('Montserrat',10),text='Pilih kolom')
        label_pilihKolom.grid(column=0,row=0)
        label_urutBerdasarkan = tk.Label(input_frame,font=('Montserrat',10),text='      Urut berdasarkan')
        label_urutBerdasarkan.grid(column=2,row=0)
        button_ascending = tk.Button(input_frame,font=('Montserrat',10),bg='#c9c9c9', text='Ascending', command=lambda:Sort(items,columns,region,bin,username,'ascending'))
        button_ascending.grid(column=3,row=0, sticky='e')
        button_descending = tk.Button(input_frame,font=('Montserrat',10),bg='#c9c9c9', text='Descending', command=lambda:Sort(items,columns,region,bin,username,'descending'))
        button_descending.grid(column=4,row=0, sticky='e',padx=3)

        bin.append(input_frame)
        bin.append(label_pilihKolom)
        bin.insert(0,entry_pilihKolom)
        bin.append(label_urutBerdasarkan)
        bin.append(button_ascending)
        bin.append(button_descending)

    elif choice == 2:
        input_frame = tk.Frame(root,relief=tk.GROOVE, bd=3)
        input_frame.place(relx=0.12,y=5)
        input_frame.columnconfigure(0,weight=1)
        input_frame.columnconfigure(1,weight=1)
        input_frame.columnconfigure(2,weight=1)
        input_frame.columnconfigure(3,weight=1)
        input_frame.columnconfigure(4,weight=1)
        label_pilihKolom = tk.Label(input_frame,font=('Montserrat',10),text='Pilih kolom')
        label_pilihKolom.grid(column=0,row=0)
        entry_pilihKolom = tk.Entry(input_frame,font=('Montserrat',10))
        entry_pilihKolom.grid(column=1,row=0,sticky='we')
        label_kataKunci = tk.Label(input_frame,font=('Montserrat',10),text='      Kata kunci')
        label_kataKunci.grid(column=2,row=0)
        entry_kataKunci = tk.Entry(input_frame,font=('Montserrat',10))
        entry_kataKunci.grid(column=3,row=0, sticky='e')
        button_search = tk.Button(input_frame, text='Cari',bg='#c9c9c9', command=lambda:Search(items,columns,region,bin,username))
        button_search.grid(column=4,row=0, sticky='e',padx=3)

        bin.append(input_frame)
        bin.append(label_pilihKolom)
        bin.append(label_kataKunci)
        bin.append(button_search)
        bin.insert(0,entry_pilihKolom)
        bin.insert(1,entry_kataKunci)

    elif choice == 3:
        input_frame = tk.Frame(root,relief=tk.GROOVE, bd=3)
        input_frame.place(relx=0.12,y=5)
        input_frame.columnconfigure(0,weight=1)
        input_frame.columnconfigure(1,weight=1)
        input_frame.columnconfigure(2,weight=1)
        input_frame.columnconfigure(3,weight=1)
        input_frame.columnconfigure(4,weight=1)
        input_frame.columnconfigure(5,weight=1)
        input_frame.columnconfigure(6,weight=1)
        input_frame.columnconfigure(7,weight=1)
        input_frame.columnconfigure(8,weight=1)
        label_namaPengirim = tk.Label(input_frame,font=('Montserrat',10),text='Nama pengirim')
        label_namaPengirim.grid(column=0,row=0)
        entry_namaPengirim = tk.Entry(input_frame,font=('Montserrat',10))
        entry_namaPengirim.grid(column=1,row=0,sticky='we')
        label_namaPenerima = tk.Label(input_frame,font=('Montserrat',10),text=' Nama penerima')
        label_namaPenerima.grid(column=2,row=0)
        entry_namaPenerima = tk.Entry(input_frame,font=('Montserrat',10))
        entry_namaPenerima.grid(column=3,row=0, sticky='e')
        label_pilihKolom = tk.Label(input_frame,font=('Montserrat',10),text=' Pilih kolom')
        label_pilihKolom.grid(column=4,row=0)
        entry_pilihKolom = tk.Entry(input_frame,font=('Montserrat',10))
        entry_pilihKolom.grid(column=5,row=0, sticky='e')
        label_kataBaru = tk.Label(input_frame,font=('Montserrat',10),text=' Kata baru')
        label_kataBaru.grid(column=6,row=0)
        entry_kataBaru = tk.Entry(input_frame,font=('Montserrat',10))
        entry_kataBaru.grid(column=7,row=0, sticky='e')
        button_edit = tk.Button(input_frame,font=('Montserrat',10),bg='#c9c9c9', text='Ganti', command=lambda:Edit(items,columns,region,bin,username))
        button_edit.grid(column=8,row=0, sticky='e',padx=3)

        bin.append(input_frame)
        bin.append(label_namaPengirim)
        bin.append(label_namaPenerima)
        bin.append(label_pilihKolom)
        bin.append(label_kataBaru)
        bin.append(button_edit)
        bin.insert(0,entry_namaPengirim)
        bin.insert(1,entry_namaPenerima)
        bin.insert(2,entry_pilihKolom)
        bin.insert(3,entry_kataBaru)


    table_frame = CreateTable(root,items,columns)
    if choice == 4:
        messagebox.showinfo("Pemberitahuan", "Data telah diperbarui.")

    bin.append(table_frame)
    root.mainloop()

def Sort(items,columns,region,bin,username,urutBerdasarkan): #FEBY/FAQIH
    pilihKolom = bin[0].get()
    if pilihKolom.capitalize() in columns:
        sorted_items = Sorting.ItemSort(items,columns,pilihKolom,urutBerdasarkan)
        CRUDMenu(sorted_items,columns,region,bin,username,1)
    else:
        if pilihKolom == '':
            messagebox.showwarning("Peringatan", "Data tidak boleh kosong.")
        else:
            messagebox.showerror("Gagal", "Data tidak ditemukan.")

def Search(items,columns,region,bin,username): #FEBY/FAQIH
    pilihKolom,kataKunci = bin[0].get(),bin[1].get()
    column_index = 0
    if pilihKolom.capitalize() in columns:
        for i in range(len(columns)):
            if columns[i] == pilihKolom.capitalize():
                column_index += i
        founded_items = Searching.ItemSearch(items,column_index,kataKunci)
        if founded_items == False:
            messagebox.showerror("Gagal", "Data tidak ditemukan.")
        else:
            CRUDMenu(founded_items,columns,region,bin,username,2)
    else:
        if pilihKolom == '' or kataKunci == '':
            messagebox.showwarning("Peringatan", "Data tidak boleh kosong.")
        else:
            messagebox.showerror("Gagal", "Data tidak ditemukan.")

def Edit(items,columns,region,bin,username): #FEBY/FAQIH
    column_index = 0
    namaPengirim,namaPenerima,pilihKolom,kataBaru = bin[0].get(),bin[1].get(),bin[2].get(),bin[3].get()
    if pilihKolom.capitalize() in columns:
        for i in range(len(columns)):
                if columns[i] == pilihKolom.capitalize():
                    column_index += i
        result = Searching.CRUDSearch(items,region,columns,namaPengirim,namaPenerima,column_index,kataBaru)
        if result == False:
            messagebox.showerror("Gagal", "Data tidak ditemukan.")
        else:
            new_items = []
            with open(f'{region}.csv', 'r') as file:
                read, boolean = csv.reader(file), True
                for i in read:
                    if boolean == True:
                        boolean = False
                        continue
                    new_items.append(i)
            CRUDMenu(new_items,columns,region,bin,username,4)
    else:
        if pilihKolom == '' or namaPenerima == '' or pilihKolom == '' or kataBaru == '':
            messagebox.showwarning("Peringatan", "Data tidak boleh kosong.")
        else:
            messagebox.showerror("Gagal", "Data tidak ditemukan.")

def usernameBind(e): #RAKA
    if var1.get() == ' Nama pengguna':
        var1.set('')
    elif var1.get() == '':
        var1.set(' Nama pengguna')

def passwordBind(e): #RAKA
    if var2.get() == ' Kata sandi':
        entry_password.configure(show='*')
        var2.set('')
    elif var2.get() == '':
        entry_password.configure(show=entry_password.get())
        var2.set(' Kata sandi')

def oldPasswordBind(e): #RAKA
    if var1.get() == 'Kata sandi lama':
        var1.set('')
    elif var1.get() == '':
        var1.set('Kata sandi lama')

def newPasswordBind(e): #RAKA
    if var2.get() == 'Kata sandi baru':
        var2.set('')
    elif var2.get() == '':
        var2.set('Kata sandi baru')
        
def emailBind(e): #RAKA
    if var1.get() == ' Alamat e-mail':
        var1.set('')
    elif var1.get() == '':
        var1.set(' Alamat e-mail')

def phoneNumberBind(e): #RAKA
    if var2.get() == ' Nomor telepon':
        var2.set('')
    elif var2.get() == '':
        var2.set(' Nomor telepon')

def forgotPasswordBind(e): #RAKA
    if var3.get() == ' Kata sandi baru':
        var3.set('')
    elif var3.get() == '':
        var3.set(' Kata sandi baru')
    
def forgotButton(e): #RAKA
    banner = None
    Forgot[0].configure(foreground='white')
    for i in range(len(Forgot)):
        if type(Forgot[i]) == list:
            banner = i
            for j in range(len(Forgot[i])):
                if j > 3:
                    Forgot[i][j].destroy()
            break
    var1.set(' Alamat e-mail')
    var2.set(' Nomor telepon')
    var3.set(' Kata sandi baru')
    Forgot[banner][1].configure(width=236,text='RESET KATA SANDI')
    entry_email = tk.Entry(Forgot[banner][0],textvariable=var1,fg='grey',font='Montserrat 12')
    entry_email.place(relx=0.32, y=200,height=30,width=236)
    entry_email.bind('<FocusIn>',emailBind)
    entry_email.bind('<FocusOut>',emailBind)
    entry_phoneNumber = tk.Entry(Forgot[banner][0],textvariable=var2,fg='grey',font='Montserrat 12')
    entry_phoneNumber.place(relx=0.32, y=250,height=30,width=236)
    entry_phoneNumber.bind('<FocusIn>',phoneNumberBind)
    entry_phoneNumber.bind('<FocusOut>',phoneNumberBind)
    entry_forgotPassword = tk.Entry(Forgot[banner][0],textvariable=var3,fg='grey',font='Montserrat 12')
    entry_forgotPassword.place(relx=0.32, y=300,height=30,width=236)
    entry_forgotPassword.bind('<FocusIn>',forgotPasswordBind)
    entry_forgotPassword.bind('<FocusOut>',forgotPasswordBind)
    button_forgotPassword = tk.Button(Forgot[banner][0],text='Reset',fg='white',bg='#DC1C13',font='Montserrat 12',command=lambda:ForgotPassword(Forgot))
    button_forgotPassword.place(relx=0.32, y=350,height=30,width=236)
    button_forgotPassword.configure(activeforeground='#DC1C13',activebackground='white')
    global button_forgot
    button_forgot = tk.Label(Forgot[banner][0], text="Kembali",font='Montserrat 10 underline',bg='#F24C4C',fg='blue')
    button_forgot.place(x=366,y=387)
    button_forgot.bind('<Button>',backBind)
    button_forgot.bind('<Enter>',forgotEnter)
    button_forgot.bind('<Leave>',forgotLeave)

    Forgot.append(Forgot[0])
    Forgot.insert(0,entry_email)
    Forgot.insert(1,entry_phoneNumber)
    Forgot.insert(2,entry_forgotPassword)
    Forgot.append(button_forgotPassword)
    Forgot.append(button_forgot)

def forgotEnter(e): #RAKA
    button_forgot.configure(fg='white')
    
def forgotLeave(e): #RAKA
    button_forgot.configure(fg='blue')

def backBind(e): #RAKA
    SignInPage()

def ForgotPassword(bin): #RAKA
    result = False
    email,phoneNumber,forgotPassword = bin[0].get(),bin[1].get(),bin[2].get()
    if email == '' or email == ' Alamat e-mail':
        messagebox.showwarning('Peringatan','Alamat e-mail tidak boleh kosong.')
    elif phoneNumber == '' or phoneNumber == ' Nomor telepon':
        messagebox.showwarning('Peringatan','Nomor telepon tidak boleh kosong.')
    elif forgotPassword == '' or forgotPassword == ' Kata sandi baru':
        messagebox.showwarning('Peringatan','Kata sandi tidak boleh kosong.')
    else:
        result = Password.Forgot(email,phoneNumber,forgotPassword)
    if result == True:
        SignInPage()
    elif result == False:
        pass
    else:
        messagebox.showwarning('Peringatan',result)

def OpenIMG(): #DINAR/DEVINA
    heroImage = Image.open('satsetheroimg.png')
    hero = heroImage.resize((570,600))
    hero = ImageTk.PhotoImage(hero)
    return hero

def OpenVector(): #DINAR/DEVINA
    heroImage = Image.open('vector.png')
    vector = heroImage.resize((570,600))
    vector = ImageTk.PhotoImage(vector)
    return vector

def SignInPage(): #RAKA
    global Forgot
    for i in range(len(Forgot)):
        if type(Forgot[-1]) == list:
            for j in Forgot[-1]:
                j.destroy()
            Forgot.pop()
            continue
        Forgot[-1].destroy()
        Forgot.pop()

    login_frame = tk.Frame(root,bg='#F24C4C')
    login_frame.place(relx=0.5,y=0,relwidth=0.5,height=600)
    vector = OpenVector()
    vectorImg = tk.Label(login_frame, image=vector)
    vectorImg.configure(background='#F24C4C')
    vectorImg.image = vector
    vectorImg.place(x=-2,y=-2)
    hero = OpenIMG()
    heroImg = tk.Label(root, image=hero)
    heroImg.configure(background='#F24C4C')
    heroImg.image = hero
    heroImg.place(x=-2,y=-2)
    
    var1.set(' Nama pengguna')
    var2.set(' Kata sandi')
    var3.set('Jabodetabek')
    entry_username = tk.Entry(login_frame,textvariable=var1,fg='grey',font='Montserrat 12')
    entry_username.place(relx=0.32, y=200,height=30,width=236)
    entry_username.bind('<FocusIn>',usernameBind)
    entry_username.bind('<FocusOut>',usernameBind)
    global entry_password
    entry_password = tk.Entry(login_frame,textvariable=var2,fg='grey',font='Montserrat 12')
    entry_password.place(relx=0.32, y=250,height=30,width=236)
    entry_password.bind('<FocusIn>',passwordBind)
    entry_password.bind('<FocusOut>',passwordBind) 
    dropdown_region = tk.OptionMenu(login_frame ,var3, *options)
    dropdown_region.place(relx=0.32,y=300,width=120)
    dropdown_region.config(bg='white',highlightthickness=0,activeforeground='grey',activebackground='white',fg='black')
    label_signin = tk.Label(login_frame,text='SIGN IN',font='Bahnschrift 20 bold', bg='#F24C4C',fg='white')
    label_signin.place(x=168,y=150,width=265)
    button_login = tk.Button(login_frame, text="Masuk",font='Montserrat 12', command=lambda:CheckLogin(bin),bg='#293462',fg='white')
    button_login.place(relx=0.32,y=380,width=236)
    button_login.config(activebackground='white', activeforeground='#293462')
    global button_forgot
    button_forgot = tk.Label(login_frame, text="Lupa kata sandi?",font='Montserrat 10 underline',bg='#F24C4C',fg='Blue')
    button_forgot.place(x=314,y=420)
    bin = [login_frame,label_signin,vectorImg,heroImg,entry_username,entry_password,dropdown_region,button_login,button_forgot]
    Forgot.append(button_forgot)
    Forgot.append(bin)
    button_forgot.bind('<Button>',forgotButton)
    button_forgot.bind('<Enter>',forgotEnter)
    button_forgot.bind('<Leave>',forgotLeave)
    root.mainloop()

#PROCESS
options = ['Jabodetabek','Jawa Barat','Jawa Tengah']
Columns,Items,Forgot = None,None,[]
root = tk.Tk()
SCREENWIDTH = root.winfo_screenwidth()
SCREENHEIGHT = root.winfo_screenheight()
WIDTH, LENGTH  = 1140, 600
XAXIS, YAXIS = int(SCREENWIDTH/2 - WIDTH/2), int(SCREENHEIGHT/2 - LENGTH/2 -50)
root.geometry(f'{WIDTH}x{LENGTH}+{XAXIS}+{YAXIS}')
root.resizable(width=False,height=False)
root.wm_iconbitmap('satsetlogo.ico')
root.wm_title('Si Satset')
var1,var2,var3,var4 = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
SignInPage()