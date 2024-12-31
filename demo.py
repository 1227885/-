import tkinter as tk
from tkinter import messagebox
import pymysql

# 数据库连接配置（请根据实际情况调整）
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "library"  # 假设数据库名为 library_system
}

# 创建数据库连接
def get_db_connection():
    connection = pymysql.connect(**db_config)
    return connection

# 弹出消息框
def show_message(title, message):
    messagebox.showinfo(title, message)

# 进入用户管理界面
def user_management():
    user_management_window = tk.Toplevel(root)
    user_management_window.title("用户管理")
    user_management_window.geometry("400x300")
    
    def add_user():
        username = entry_username.get()
        email = entry_email.get()
        phone = entry_phone.get()
        role = entry_role.get()
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, email, phone, role) VALUES (%s, %s, %s, %s)",
                       (username, email, phone, role))
        connection.commit()
        cursor.close()
        connection.close()
        show_message("成功", "用户添加成功！")
    
    # 用户管理界面
    label_username = tk.Label(user_management_window, text="用户名")
    label_username.pack(pady=5)
    entry_username = tk.Entry(user_management_window)
    entry_username.pack(pady=5)
    
    label_email = tk.Label(user_management_window, text="邮箱")
    label_email.pack(pady=5)
    entry_email = tk.Entry(user_management_window)
    entry_email.pack(pady=5)
    
    label_phone = tk.Label(user_management_window, text="电话")
    label_phone.pack(pady=5)
    entry_phone = tk.Entry(user_management_window)
    entry_phone.pack(pady=5)
    
    label_role = tk.Label(user_management_window, text="角色(admin/user)")
    label_role.pack(pady=5)
    entry_role = tk.Entry(user_management_window)
    entry_role.pack(pady=5)
    
    button_add_user = tk.Button(user_management_window, text="添加用户", command=add_user)
    button_add_user.pack(pady=20)

# 进入图书管理界面
def book_management():
    book_management_window = tk.Toplevel(root)
    book_management_window.title("图书管理")
    book_management_window.geometry("400x300")
    
    def add_book():
        title = entry_title.get()
        author = entry_author.get()
        isbn = entry_isbn.get()
        publisher = entry_publisher.get()
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books (title, author, isbn, publisher) VALUES (%s, %s, %s, %s)",
                       (title, author, isbn, publisher))
        connection.commit()
        cursor.close()
        connection.close()
        show_message("成功", "图书添加成功！")
    
    # 图书管理界面
    label_title = tk.Label(book_management_window, text="书名")
    label_title.pack(pady=5)
    entry_title = tk.Entry(book_management_window)
    entry_title.pack(pady=5)
    
    label_author = tk.Label(book_management_window, text="作者")
    label_author.pack(pady=5)
    entry_author = tk.Entry(book_management_window)
    entry_author.pack(pady=5)
    
    label_isbn = tk.Label(book_management_window, text="ISBN")
    label_isbn.pack(pady=5)
    entry_isbn = tk.Entry(book_management_window)
    entry_isbn.pack(pady=5)
    
    label_publisher = tk.Label(book_management_window, text="出版社")
    label_publisher.pack(pady=5)
    entry_publisher = tk.Entry(book_management_window)
    entry_publisher.pack(pady=5)
    
    button_add_book = tk.Button(book_management_window, text="添加图书", command=add_book)
    button_add_book.pack(pady=20)

# 进入借书还书界面
def borrow_return_management():
    borrow_return_window = tk.Toplevel(root)
    borrow_return_window.title("借书还书管理")
    borrow_return_window.geometry("400x300")
    
    def borrow_book():
        user_id = entry_user_id.get()
        book_id = entry_book_id.get()
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT available_stock FROM books WHERE id = %s", (book_id,))
        available_stock = cursor.fetchone()[0]
        
        if available_stock > 0:
            cursor.execute("INSERT INTO borrow_records (user_id, book_id, borrow_date) VALUES (%s, %s, NOW())",
                           (user_id, book_id))
            cursor.execute("UPDATE books SET available_stock = available_stock - 1 WHERE id = %s", (book_id,))
            connection.commit()
            show_message("成功", "借书成功！")
        else:
            show_message("失败", "该书已借完！")
        
        cursor.close()
        connection.close()
    
    def return_book():
        borrow_id = entry_borrow_id.get()
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT book_id FROM borrow_records WHERE id = %s", (borrow_id,))
        book_id = cursor.fetchone()[0]
        
        if book_id is None:
            show_message("失败", "未找到该借阅记录！")
        else:
            cursor.execute("UPDATE borrow_records SET return_date = NOW() WHERE id = %s", (borrow_id,))
            cursor.execute("UPDATE books SET available_stock = available_stock + 1 WHERE id = %s", (book_id,))
            connection.commit()
            show_message("成功", "还书成功！")
        
        cursor.close()
        connection.close()

    label_user_id = tk.Label(borrow_return_window, text="用户ID")
    label_user_id.pack(pady=5)
    entry_user_id = tk.Entry(borrow_return_window)
    entry_user_id.pack(pady=5)
    
    label_book_id = tk.Label(borrow_return_window, text="图书ID")
    label_book_id.pack(pady=5)
    entry_book_id = tk.Entry(borrow_return_window)
    entry_book_id.pack(pady=5)
    
    button_borrow_book = tk.Button(borrow_return_window, text="借书", command=borrow_book)
    button_borrow_book.pack(pady=5)
    
    label_borrow_id = tk.Label(borrow_return_window, text="借阅记录ID")
    label_borrow_id.pack(pady=5)
    entry_borrow_id = tk.Entry(borrow_return_window)
    entry_borrow_id.pack(pady=5)
    
    button_return_book = tk.Button(borrow_return_window, text="还书", command=return_book)
    button_return_book.pack(pady=20)

# 主界面
root = tk.Tk()
root.title("图书管理系统")
root.geometry("600x400")

# 主菜单按钮
button_user_management = tk.Button(root, text="用户管理", width=20, height=2, command=user_management)
button_user_management.pack(pady=10)

button_book_management = tk.Button(root, text="图书管理", width=20, height=2, command=book_management)
button_book_management.pack(pady=10)

button_borrow_return_management = tk.Button(root, text="借书还书管理", width=20, height=2, command=borrow_return_management)
button_borrow_return_management.pack(pady=10)

# 退出按钮
button_exit = tk.Button(root, text="退出系统", width=20, height=2, command=root.quit)
button_exit.pack(pady=10)

root.mainloop()
