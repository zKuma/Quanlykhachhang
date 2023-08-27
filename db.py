import sqlite3


mysqldb = sqlite3.connect("khachhang.db") #Kết nối database SQLite

mycursor = mysqldb.cursor() #Tạo cursor

#Tạo table
# mycursor.execute("""CREATE TABLE KH (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     Ho_va_ten_dem TEXT,
#     Ten TEXT,
#     Cccd TEXT,
#     SDT TEXT,
#     Email TEXT,
#     Matour TEXT,
#     Ngaykhoihanh TEXT,
#     Ghichu TEXT
# )
#      """)

#Insert dữ liệu

# mycursor.execute("INSERT INTO KH (Ho_va_ten_dem,Ten,Cccd,SDT,Email,Matour,Ngaykhoihanh,Ghichu) VALUES ('Le Viet','Hoang','012345678999','0901234567','lvh@mail.com','VN01','06/06/2023','')")

# hvtd = 'Tran Van'
# ten = 'B'
# cccd = '0123456789996'
# sdt = '0912345676'
# email = 'tva@mail.com'
# matour = 'VN03'
# ngaykhoihanh = '07/06/2023'
# ghichu = ''

# sql = "INSERT INTO KH (Ho_va_ten_dem,Ten,Cccd,SDT,Email,Matour,Ngaykhoihanh,Ghichu) VALUES (\'"+hvtd+"\', \'"+ten+"\',\'"+cccd+"\',\'"+sdt+"\',\'"+email+"\',\'"+matour+"\',\'"+ngaykhoihanh+"\',\'"+ghichu+"\')"

# mycursor.execute(sql) #thực thi lệnh SQL: (ở đây là lệnh INSERT)

#Check dữ liệu

# mycursor.execute("SELECT * FROM KH") #thực thi lệnh SQL: (ở đây là lệnh Query: SELECT)
# fin = mycursor.fetchall() #Lấy kết quả của phép thực thi trên
# for i in fin:
#     print(i)


mysqldb.commit() #Lệnh commit sql

mysqldb.close() #Đóng kết nối database
