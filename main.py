import tkinter
from tkinter import ttk, messagebox
from tkinter import *
import sqlite3
import ctypes

try:
    import customtkinter

except:
    import os
    os.startfile("customtkinter.bat")


# Hàm lấy các thông tin của người được chọn
def GetValue(event):
    global cid
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['Họ & tên đệm'])
    e2.insert(0, select['Tên'])
    e3.insert(0, select['CCCD'])
    e4.insert(0, select['SĐT'])
    e5.insert(0, select['Email'])
    e6.insert(0, select['Mã tour'])
    e7.insert(0, select['Ngày khởi hành'])
    e8.insert(0, select['Ghi chú'])
    cid = select['ID']


#Hàm thêm thông tin khách hàng
def Add():
    check = 1
    hvtd = e1.get()
    ten = e2.get()
    cccd = e3.get()
    sdt = e4.get()
    email = e5.get()
    matour = e6.get()
    ngaykhoihanh = e7.get()
    ghichu = e8.get()
    if (ten == '') or (cccd == '') or (sdt == '') or (matour == '') or (ngaykhoihanh == ''):
        check = 0
    mysqldb = sqlite3.connect("khachhang.db")
    mycursor = mysqldb.cursor()
    if check == 1:
        try:
            sql = "INSERT INTO KH (Ho_va_ten_dem,Ten,Cccd,SDT,Email,Matour,Ngaykhoihanh,Ghichu) VALUES (\'"+hvtd+"\', \'"+ten+"\',\'"+cccd+"\',\'"+sdt+"\',\'"+email+"\',\'"+matour+"\',\'"+ngaykhoihanh+"\',\'"+ghichu+"\')"
            mycursor.execute(sql)
            mysqldb.commit()
            messagebox.showinfo("Thêm", "Thêm thông tin khách hàng thành công")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e8.delete(0, END)
            e1.focus_set()
            show()
            mysqldb.close()

        except Exception as e:
            #print(e)
            mysqldb.rollback()
            mysqldb.close()
    else:
        messagebox.showinfo("Thêm", "Thông tin khách hàng còn thiếu!")


#Hàm cập nhật thông tin khách hàng
def update():
    check = 1
    hvtd = e1.get()
    ten = e2.get()
    cccd = e3.get()
    sdt = e4.get()
    email = e5.get()
    matour = e6.get()
    ngaykhoihanh = e7.get()
    ghichu = e8.get()

    if (ten == '') or (cccd == '') or (sdt == '') or (matour == '') or (ngaykhoihanh == ''):
        check = 0

    mysqldb = sqlite3.connect("khachhang.db")
    mycursor = mysqldb.cursor()

    if check == 1:
        try:
            sql = "Update KH set Ho_va_ten_dem = \'"+hvtd+"\', Ten= \'"+ten+"\', Cccd = \'"+cccd+"\', SDT = \'"+sdt+"\', Email = \'"+email+"\', Matour = \'"+matour+"\', Ngaykhoihanh = \'"+ngaykhoihanh+"\', Ghichu = \'"+ghichu+"\' WHERE ID= \'"+cid+"\'"
            mycursor.execute(sql)
            mysqldb.commit()
            messagebox.showinfo("Cập nhập", "Cập nhập thông tin khách hàng thành công")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e8.delete(0, END)
            e1.focus_set()
            show()
            mysqldb.close()

        except Exception as e:
            #print(e)
            mysqldb.rollback()
            mysqldb.close()
    else:
        messagebox.showinfo("Cập nhập", "Thông tin khách hàng còn thiếu!")

#Hàm tìm kiếm thông tin khách hàng
def find(r):
    listBox.delete(*listBox.get_children())

    mysqldb = sqlite3.connect("khachhang.db")
    mycursor = mysqldb.cursor()
    if r == 1:
        ten = e2.get()
        sql = "SELECT * FROM KH where Ten = \'"+ten+"\'"
        mycursor.execute(sql)
        records = mycursor.fetchall()
        mysqldb.commit()
        for i, (ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu) in enumerate(records, start=1):
            listBox.insert("", "end", values=(ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu))
        mysqldb.commit()
        messagebox.showinfo("Tìm kiếm", "Kết quả tìm kiếm khách hàng có tên: {}".format(ten))
        mysqldb.close()

    if r == 2:
        cccd = e3.get()
        sql = "SELECT * FROM KH where Cccd = \'"+cccd+"\'"
        mycursor.execute(sql)
        records = mycursor.fetchall()
        mysqldb.commit()
        for i, (ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu) in enumerate(records, start=1):
            listBox.insert("", "end", values=(ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu))
        mysqldb.commit()
        messagebox.showinfo("Tìm kiếm", "Kết quả tìm kiếm khách hàng có CCCD: {}".format(cccd))
        mysqldb.close()

    if r == 3:
        sdt = e4.get()
        sql = "SELECT * FROM KH where SDT = \'"+sdt+"\'"
        mycursor.execute(sql)
        records = mycursor.fetchall()
        mysqldb.commit()
        for i, (ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu) in enumerate(records, start=1):
            listBox.insert("", "end", values=(ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu))
        mysqldb.commit()
        messagebox.showinfo("Tìm kiếm", "Kết quả tìm kiếm khách hàng có SĐT: {}".format(sdt))
        mysqldb.close()

    if r == 4:
        matour = e6.get()
        ngaykhoihanh = e7.get()
        if matour == '':
            sql = "SELECT * FROM KH WHERE Ngaykhoihanh = \'"+ngaykhoihanh+"\'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            mysqldb.commit()
            for i, (ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu) in enumerate(records, start=1):
                listBox.insert("", "end", values=(ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu))
            mysqldb.commit()
            messagebox.showinfo("Tìm kiếm", "Kết quả tìm kiếm khách hàng trong tour: vào {}".format(ngaykhoihanh))
            mysqldb.close()
        elif ngaykhoihanh == '':
            sql = "SELECT * FROM KH WHERE Matour = \'" + matour + "\'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            mysqldb.commit()
            for i, (ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu) in enumerate(records,start=1):
                listBox.insert("", "end",values=(ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu))
            mysqldb.commit()
            messagebox.showinfo("Tìm kiếm", "Kết quả tìm kiếm khách hàng trong tour: {}".format(matour))
            mysqldb.close()
        else:
            sql = "SELECT * FROM KH WHERE Matour = \'" + matour + "\' AND Ngaykhoihanh = \'" + ngaykhoihanh + "\'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            mysqldb.commit()
            for i, (ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu) in enumerate(records, start=1):
                listBox.insert("", "end",values=(ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu))
            mysqldb.commit()
            messagebox.showinfo("Tìm kiếm","Kết quả tìm kiếm khách hàng trong tour: {} vào {}".format(matour, ngaykhoihanh))
            mysqldb.close()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e1.focus_set()


#Hàm xóa thông tin khách hàng
def delete():
    mysqldb = sqlite3.connect("khachhang.db")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from KH where ID = \'"+cid+"\'"
        mycursor.execute(sql)
        mysqldb.commit()
        messagebox.showinfo("Xóa", "Xóa thông tin khách hàng thành công")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e1.focus_set()
        show()
        mysqldb.close()

    except Exception as e:
        #print(e)
        mysqldb.rollback()
        mysqldb.close()


#Hàm hiển thị tất cả thông tin khách hàng - Tải lại
def show():
    listBox.delete(*listBox.get_children())
    mysqldb = sqlite3.connect("khachhang.db")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT ID,Ho_va_ten_dem,Ten,Cccd,SDT,Email,Matour,Ngaykhoihanh,Ghichu FROM KH")
    records = mycursor.fetchall()
    mysqldb.commit()
    for i, (ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu) in enumerate(records, start=1):
        listBox.insert("", "end", values=(ID, Ho_va_ten_dem, Ten, Cccd, SDT, Email, Matour, Ngaykhoihanh, Ghichu))
    mysqldb.close()


ctypes.windll.shcore.SetProcessDpiAwareness(2)
#MAIN
#Khai báo giao diện
root = customtkinter.CTk()
root.title("Saigontourist: Quản lý khách hàng")
root.iconbitmap('icon.ico')
width = root.winfo_screenwidth()/1366
height = root.winfo_screenheight()/768
wx = int(900*width)
wy = int(460*height)
geo = str(wx)+'x'+str(wy)
root.geometry(geo)
#Khai báo các biến global
global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8
global cid
global r

#Tạo Label giữ text
customtkinter.CTkLabel(root, text="Họ và tên đệm").place(x=int(10*width), y=int(10*height))
customtkinter.CTkLabel(root, text="Tên").place(x=int(10*width), y=int(40*height))
customtkinter.CTkLabel(root, text="CCCD").place(x=int(10*width), y=int(70*height))
customtkinter.CTkLabel(root, text="SĐT").place(x=int(10*width), y=int(100*height))
customtkinter.CTkLabel(root, text="Email").place(x=int(470*width), y=int(10*height))
customtkinter.CTkLabel(root, text="Mã tour").place(x=int(470*width), y=int(40*height))
customtkinter.CTkLabel(root, text="Ngày khởi hành").place(x=int(470*width), y=int(70*height))
customtkinter.CTkLabel(root, text="Ghi chú").place(x=int(470*width), y=int(100*height))

#Tạo các entry để nhập/giữ thông tin khách hàng
e1 = customtkinter.CTkEntry(root, width=int(250*width))
e1.place(x=int(140*width), y=int(10*height))

e2 = customtkinter.CTkEntry(root, width=int(250*width))
e2.place(x=int(140*width), y=int(40*height))

e3 = customtkinter.CTkEntry(root, width=int(250*width))
e3.place(x=int(140*width), y=int(70*height))

e4 = customtkinter.CTkEntry(root, width=int(250*width))
e4.place(x=int(140*width), y=int(100*height))

e5 = customtkinter.CTkEntry(root, width=int(250*width))
e5.place(x=int(600*width), y=int(10*height))

e6 = customtkinter.CTkEntry(root, width=int(250*width))
e6.place(x=int(600*width), y=int(40*height))

e7 = customtkinter.CTkEntry(root, width=int(250*width))
e7.place(x=int(600*width), y=int(70*height))

e8 = customtkinter.CTkEntry(root, width=int(250*width))
e8.place(x=int(600*width), y=int(100*height))

#Biến cho hàm tìm kiếm
r = IntVar()
r.set("1")

#Các Button
customtkinter.CTkButton(root, text="Thêm", command=Add, height=int(40*height), width=int(80*width)).place(x=int(30*width), y=int(150*height))
customtkinter.CTkButton(root, text="Sửa", command=update, height=int(40*height), width=int(80*width)).place(x=int(170*width), y=int(150*height))
customtkinter.CTkButton(root, text="Xóa", command=delete, height=int(40*height), width=int(80*width)).place(x=int(310*width), y=int(150*height))
customtkinter.CTkButton(root, text="Tải lại", command=show, height=int(40*height), width=int(80*width)).place(x=int(450*width), y=int(150*height))
customtkinter.CTkRadioButton(root, text="Tìm theo tên", variable=r, value=1).place(x=int(590*width), y=int(130*height))
customtkinter.CTkRadioButton(root, text="Tìm theo CCCD", variable=r, value=2).place(x=int(590*width), y=int(150*height))
customtkinter.CTkRadioButton(root, text="Tìm theo SĐT", variable=r, value=3).place(x=int(590*width), y=int(170*height))
customtkinter.CTkRadioButton(root, text="Tìm theo Tour", variable=r, value=4).place(x=int(590*width), y=int(190*height))
customtkinter.CTkButton(root, text="Tìm kiếm", command=lambda: find(r.get()), height=int(40*height), width=int(80*width)).place(x=int(730*width), y=int(150*height))

#Bảng hiện thị thông tin khách hàng
cols = ('ID', 'Họ & tên đệm', 'Tên', 'CCCD', 'SĐT', 'Email', 'Mã tour', 'Ngày khởi hành', 'Ghi chú')
listBox = ttk.Treeview(root, columns=cols, show='headings')
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=int(10*width), y=int(220*height))
    listBox.column(col, width=int(100*width), anchor=tkinter.CENTER)
listBox.column('ID', width=int(20*width), anchor=tkinter.CENTER)
listBox.column('Họ & tên đệm', width=int(90*width), anchor=tkinter.CENTER)
listBox.column('Tên', width=int(70*width), anchor=tkinter.CENTER)
listBox.column('Ghi chú', width=int(200*width), anchor=tkinter.CENTER)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
