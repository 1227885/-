import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pymysql
import datetime

# 连接到MySQL数据库
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='library'
)


class LibraryManager:
    def __init__(self, root):
        self.root = root
        self.root.title("图书管理系统")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)

        self.user_tab = ttk.Frame(tab_control)
        self.book_tab = ttk.Frame(tab_control)
        self.borrow_tab = ttk.Frame(tab_control)
        self.query_tab = ttk.Frame(tab_control)
        self.rating_tab = ttk.Frame(tab_control)

        tab_control.add(self.user_tab, text='用户管理')
        tab_control.add(self.book_tab, text='图书管理')
        tab_control.add(self.borrow_tab, text='借书还书管理')
        tab_control.add(self.query_tab, text='查询功能')
        tab_control.add(self.rating_tab, text='评分功能')
        tab_control.pack(expand=1, fill='both')

        self.create_user_interface()
        self.create_book_interface()
        self.create_borrow_interface()
        self.create_query_interface()
        self.create_rating_interface()

    def create_user_interface(self):
        # 用户管理界面
        user_frame = tk.LabelFrame(self.user_tab, text="用户管理")
        user_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(user_frame, text="用户名:").grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(user_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(user_frame, text="密码:").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(user_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(user_frame, text="邮箱:").grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(user_frame)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(user_frame, text="电话:").grid(row=3, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(user_frame)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(user_frame, text="角色:").grid(row=4, column=0, padx=10, pady=5)
        self.role_entry = tk.Entry(user_frame)
        self.role_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(user_frame, text="添加用户", command=self.add_user).grid(row=5, column=0, columnspan=2, padx=10,
                                                                           pady=10)
        tk.Button(user_frame, text="查询所有用户信息", command=self.get_all_users).grid(row=6, column=0, columnspan=2,
                                                                                        padx=10, pady=10)

    def create_book_interface(self):
        # 图书管理界面
        book_frame = tk.LabelFrame(self.book_tab, text="图书管理")
        book_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(book_frame, text="书名:").grid(row=0, column=0, padx=10, pady=5)
        self.title_entry = tk.Entry(book_frame)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(book_frame, text="作者:").grid(row=1, column=0, padx=10, pady=5)
        self.author_entry = tk.Entry(book_frame)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(book_frame, text="ISBN:").grid(row=2, column=0, padx=10, pady=5)
        self.isbn_entry = tk.Entry(book_frame)
        self.isbn_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(book_frame, text="出版社:").grid(row=3, column=0, padx=10, pady=5)
        self.publisher_entry = tk.Entry(book_frame)
        self.publisher_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(book_frame, text="出版日期:").grid(row=4, column=0, padx=10, pady=5)
        self.publish_date_entry = tk.Entry(book_frame)
        self.publish_date_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(book_frame, text="总库存:").grid(row=5, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(book_frame)
        self.quantity_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(book_frame, text="可借数量:").grid(row=6, column=0, padx=10, pady=5)
        self.available_entry = tk.Entry(book_frame)
        self.available_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Button(book_frame, text="添加图书", command=self.add_book).grid(row=7, column=0, columnspan=2, padx=10,
                                                                           pady=10)
        tk.Button(book_frame, text="查询所有图书信息", command=self.get_all_books).grid(row=8, column=0, columnspan=2,
                                                                                        padx=10, pady=10)

    def create_borrow_interface(self):
        # 借书还书管理界面
        borrow_frame = tk.LabelFrame(self.borrow_tab, text="借书管理")
        borrow_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(borrow_frame, text="用户ID:").grid(row=0, column=0, padx=10, pady=5)
        self.borrow_user_id_entry = tk.Entry(borrow_frame)
        self.borrow_user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(borrow_frame, text="图书ID:").grid(row=1, column=0, padx=10, pady=5)
        self.borrow_book_id_entry = tk.Entry(borrow_frame)
        self.borrow_book_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(borrow_frame, text="借书", command=self.borrow_book).grid(row=2, column=0, columnspan=2, padx=10,
                                                                            pady=10)

        return_frame = tk.LabelFrame(self.borrow_tab, text="还书管理")
        return_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(return_frame, text="借阅记录ID:").grid(row=0, column=0, padx=10, pady=5)
        self.return_record_id_entry = tk.Entry(return_frame)
        self.return_record_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(return_frame, text="还书", command=self.return_book).grid(row=1, column=0, columnspan=2, padx=10,
                                                                            pady=10)

    def create_query_interface(self):
        # 查询功能界面
        query_frame = tk.LabelFrame(self.query_tab, text="查询功能")
        query_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(query_frame, text="查询条件:").grid(row=0, column=0, padx=10, pady=5)
        self.query_entry = tk.Entry(query_frame)
        self.query_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(query_frame, text="查询用户信息", command=self.query_user_info).grid(row=1, column=0, columnspan=2,
                                                                                       padx=10, pady=5)
        tk.Button(query_frame, text="查询图书信息", command=self.query_book_info).grid(row=2, column=0, columnspan=2,
                                                                                       padx=10, pady=5)
        tk.Button(query_frame, text="查询借阅记录", command=self.query_borrow_records).grid(row=3, column=0,
                                                                                            columnspan=2, padx=10,
                                                                                            pady=5)

    def create_rating_interface(self):
        # 评分功能界面
        rating_frame = tk.LabelFrame(self.rating_tab, text="评分功能")
        rating_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(rating_frame, text="用户ID:").grid(row=0, column=0, padx=10, pady=5)
        self.rating_user_id_entry = tk.Entry(rating_frame)
        self.rating_user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(rating_frame, text="图书ID:").grid(row=1, column=0, padx=10, pady=5)
        self.rating_book_id_entry = tk.Entry(rating_frame)
        self.rating_book_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(rating_frame, text="评分(1-5):").grid(row=2, column=0, padx=10, pady=5)
        self.rating_entry = tk.Entry(rating_frame)
        self.rating_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(rating_frame, text="添加评分", command=self.add_rating).grid(row=3, column=0, columnspan=2, padx=10,
                                                                               pady=10)
        tk.Button(rating_frame, text="查看图书评分", command=self.view_book_ratings).grid(row=4, column=0, columnspan=2,
                                                                                          padx=10, pady=10)

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        role = self.role_entry.get()
        with connection.cursor() as cursor:
            query = "INSERT INTO users (username, password, email, phone, role) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (username, password, email, phone, role))
        connection.commit()
        messagebox.showinfo("成功", "用户添加成功！")

    def get_all_users(self):
        with connection.cursor() as cursor:
            query = "SELECT * FROM users"
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                result_str = "\n".join([str(row) for row in result])
                messagebox.showinfo("所有用户信息", result_str)
            else:
                messagebox.showinfo("提示", "无用户信息")

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        publisher = self.publisher_entry.get()
        publish_date = self.publish_date_entry.get()
        quantity = self.quantity_entry.get()
        available = self.available_entry.get()
        with connection.cursor() as cursor:
            query = "INSERT INTO books (title, author, isbn, publisher, publish_date, quantity, available) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (title, author, isbn, publisher, publish_date, quantity, available))
        connection.commit()
        messagebox.showinfo("成功", "图书添加成功！")

    def get_all_books(self):
        with connection.cursor() as cursor:
            query = "SELECT * FROM books"
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                result_str = "\n".join([str(row) for row in result])
                messagebox.showinfo("所有图书信息", result_str)
            else:
                messagebox.showinfo("提示", "无图书信息")

    def borrow_book(self):
        user_id = self.borrow_user_id_entry.get()
        book_id = self.borrow_book_id_entry.get()
        with connection.cursor() as cursor:
            # 检查图书是否可借阅
            check_query = "SELECT available FROM books WHERE book_id = %s"
            cursor.execute(check_query, (book_id,))
            result = cursor.fetchone()
            if result and result[0] > 0:
                # 更新图书可借阅数量
                update_query = "UPDATE books SET available = available - 1 WHERE book_id = %s"
                cursor.execute(update_query, (book_id,))
                # 插入借阅记录
                insert_query = "INSERT INTO borrow_records (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (user_id, book_id, datetime.date.today()))
                connection.commit()
                messagebox.showinfo("成功", "借书成功！")
            else:
                messagebox.showwarning("失败", "图书不可借阅！")

    def return_book(self):
        record_id = self.return_record_id_entry.get()
        with connection.cursor() as cursor:
            # 检查借阅记录是否存在且未归还
            check_query = "SELECT book_id FROM borrow_records WHERE record_id = %s AND return_date IS NULL"
            cursor.execute(check_query, (record_id,))
            result = cursor.fetchone()
            if result:
                book_id = result[0]
                # 更新借阅记录的归还日期
                update_query = "UPDATE borrow_records SET return_date = %s WHERE record_id = %s"
                cursor.execute(update_query, (datetime.date.today(), record_id))
                # 更新图书可借阅数量
                book_update_query = "UPDATE books SET available = available + 1 WHERE book_id = %s"
                cursor.execute(book_update_query, (book_id,))
                connection.commit()
                messagebox.showinfo("成功", "还书成功！")
            else:
                messagebox.showwarning("失败", "无效的借阅记录ID或图书已归还！")

    def query_user_info(self):
        query_condition = self.query_entry.get()
        with connection.cursor() as cursor:
            query = "SELECT * FROM users WHERE username LIKE %s OR email LIKE %s"
            cursor.execute(query, (f"%{query_condition}%", f"%{query_condition}%"))
            result = cursor.fetchall()
            if result:
                result_str = "\n".join([str(row) for row in result])
                messagebox.showinfo("用户信息", result_str)
            else:
                messagebox.showinfo("提示", "无用户信息")

    def query_book_info(self):
        query_condition = self.query_entry.get()
        with connection.cursor() as cursor:
            query = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s OR isbn LIKE %s OR publisher LIKE %s"
            cursor.execute(query, (
            f"%{query_condition}%", f"%{query_condition}%", f"%{query_condition}%", f"%{query_condition}%"))
            result = cursor.fetchall()
            if result:
                result_str = "\n".join([str(row) for row in result])
                messagebox.showinfo("图书信息", result_str)
            else:
                messagebox.showinfo("提示", "无图书信息")

    def query_borrow_records(self):
        query_condition = self.query_entry.get()
        with connection.cursor() as cursor:
            query = "SELECT * FROM borrow_records WHERE user_id = %s OR book_id = %s OR borrow_date = %s OR return_date = %s"
            cursor.execute(query, (query_condition, query_condition, query_condition, query_condition))
            result = cursor.fetchall()
            if result:
                result_str = "\n".join([str(row) for row in result])
                messagebox.showinfo("借阅记录", result_str)
            else:
                messagebox.showinfo("提示", "无借阅记录")

    def add_rating(self):
        user_id = self.rating_user_id_entry.get()
        book_id = self.rating_book_id_entry.get()
        rating = self.rating_entry.get()
        with connection.cursor() as cursor:
            query = "INSERT INTO ratings (user_id, book_id, rating, created_at) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (user_id, book_id, rating, datetime.datetime.now()))
        connection.commit()
        messagebox.showinfo("成功", "评分添加成功！")

    def view_book_ratings(self):
        book_id = self.rating_book_id_entry.get()
        with connection.cursor() as cursor:
            query = "SELECT rating FROM ratings WHERE book_id = %s"
            cursor.execute(query, (book_id,))
            result = cursor.fetchall()
            if result:
                ratings = [row[0] for row in result]
                avg_rating = sum(ratings) / len(ratings)
                messagebox.showinfo("图书评分", f"平均评分：{avg_rating:.2f}\n评分详情：{ratings}")
            else:
                messagebox.showinfo("提示", "无评分记录")

    def create_update_info_interface(self):
        update_info_frame = tk.LabelFrame(self.update_info_tab, text="修改个人信息")
        update_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(update_info_frame, text="用户ID:").grid(row=0, column=0, padx=10, pady=5)
        self.update_user_id_entry = tk.Entry(update_info_frame)
        self.update_user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(update_info_frame, text="选择要修改的信息:").grid(row=1, column=0, padx=10, pady=5)
        self.update_field = ttk.Combobox(update_info_frame, values=["用户名", "密码", "邮箱", "电话"])
        self.update_field.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(update_info_frame, text="新信息:").grid(row=2, column=0, padx=10, pady=5)
        self.new_info_entry = tk.Entry(update_info_frame)
        self.new_info_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(update_info_frame, text="确认修改", command=self.update_user_info).grid(row=3, column=0, columnspan=2,
                                                                                          padx=10, pady=10)

    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)

        self.user_tab = ttk.Frame(tab_control)
        self.book_tab = ttk.Frame(tab_control)
        self.borrow_tab = ttk.Frame(tab_control)
        self.query_tab = ttk.Frame(tab_control)
        self.rating_tab = ttk.Frame(tab_control)
        self.update_info_tab = ttk.Frame(tab_control)  # 添加修改个人信息的标签页

        tab_control.add(self.user_tab, text='用户管理')
        tab_control.add(self.book_tab, text='图书管理')
        tab_control.add(self.borrow_tab, text='借书还书管理')
        tab_control.add(self.query_tab, text='查询功能')
        tab_control.add(self.rating_tab, text='评分功能')
        tab_control.add(self.update_info_tab, text='修改个人信息')  # 添加标签页
        tab_control.pack(expand=1, fill='both')

        self.create_user_interface()
        self.create_book_interface()
        self.create_borrow_interface()
        self.create_query_interface()
        self.create_rating_interface()
        self.create_update_info_interface()  # 创建修改个人信息界面

    def update_user_info(self):
        user_id = self.update_user_id_entry.get()
        field = self.update_field.get()
        new_info = self.new_info_entry.get()

        if field == "用户名":
            db_field = "username"
        elif field == "密码":
            db_field = "password"
        elif field == "邮箱":
            db_field = "email"
        elif field == "电话":
            db_field = "phone"
        else:
            messagebox.showwarning("警告", "请选择要修改的信息")
            return

        with connection.cursor() as cursor:
            query = f"UPDATE users SET {db_field} = %s, updated_at = NOW() WHERE id = %s"
            cursor.execute(query, (new_info, user_id))
        connection.commit()
        messagebox.showinfo("成功", "用户信息更新成功")

    def update_user_info(self):
        user_id = self.update_user_id_entry.get()
        field = self.update_field.get()
        new_info = self.new_info_entry.get()

        if field == "用户名":
            db_field = "username"
        elif field == "密码":
            db_field = "password"
        elif field == "邮箱":
            db_field = "email"
        elif field == "电话":
            db_field = "phone"
        else:
            messagebox.showwarning("警告", "请选择要修改的信息")
            return

        with connection.cursor() as cursor:
            query = f"UPDATE users SET {db_field} = %s, updated_at = NOW() WHERE id = %s"
            cursor.execute(query, (new_info, user_id))
        connection.commit()
        messagebox.showinfo("成功", "用户信息更新成功")

    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)

        self.user_tab = ttk.Frame(tab_control)
        self.book_tab = ttk.Frame(tab_control)
        self.borrow_tab = ttk.Frame(tab_control)
        self.query_tab = ttk.Frame(tab_control)
        self.rating_tab = ttk.Frame(tab_control)
        self.update_info_tab = ttk.Frame(tab_control)  # 添加修改个人信息的标签页
        self.reservation_tab = ttk.Frame(tab_control)  # 添加查看个人预约记录的标签页

        tab_control.add(self.user_tab, text='用户管理')
        tab_control.add(self.book_tab, text='图书管理')
        tab_control.add(self.borrow_tab, text='借书还书管理')
        tab_control.add(self.query_tab, text='查询功能')
        tab_control.add(self.rating_tab, text='评分功能')
        tab_control.add(self.update_info_tab, text='修改个人信息')  # 添加标签页
        tab_control.add(self.reservation_tab, text='查看预约记录')  # 添加标签页
        tab_control.pack(expand=1, fill='both')

        self.create_user_interface()
        self.create_book_interface()
        self.create_borrow_interface()
        self.create_query_interface()
        self.create_rating_interface()
        self.create_update_info_interface()  # 创建修改个人信息界面
        self.create_reservation_interface()  # 创建查看预约记录界面

    def create_update_info_interface(self):
        update_info_frame = tk.LabelFrame(self.update_info_tab, text="修改个人信息")
        update_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(update_info_frame, text="用户ID:").grid(row=0, column=0, padx=10, pady=5)
        self.update_user_id_entry = tk.Entry(update_info_frame)
        self.update_user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(update_info_frame, text="选择要修改的信息:").grid(row=1, column=0, padx=10, pady=5)
        self.update_field = ttk.Combobox(update_info_frame, values=["用户名", "密码", "邮箱", "电话"])
        self.update_field.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(update_info_frame, text="新信息:").grid(row=2, column=0, padx=10, pady=5)
        self.new_info_entry = tk.Entry(update_info_frame)
        self.new_info_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(update_info_frame, text="确认修改", command=self.update_user_info).grid(row=3, column=0, columnspan=2,
                                                                                          padx=10, pady=10)

    def create_reservation_interface(self):
        reservation_frame = tk.LabelFrame(self.reservation_tab, text="查看预约记录")
        reservation_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(reservation_frame, text="用户ID:").grid(row=0, column=0, padx=10, pady=5)
        self.reservation_user_id_entry = tk.Entry(reservation_frame)
        self.reservation_user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(reservation_frame, text="查看预约记录", command=self.view_reservations).grid(row=1, column=0,
                                                                                               columnspan=2, padx=10,
                                                                                               pady=10)

    def update_user_info(self):
        user_id = self.update_user_id_entry.get()
        field = self.update_field.get()
        new_info = self.new_info_entry.get()

        if field == "用户名":
            db_field = "username"
        elif field == "密码":
            db_field = "password"
        elif field == "邮箱":
            db_field = "email"
        elif field == "电话":
            db_field = "phone"
        else:
            messagebox.showwarning("警告", "请选择要修改的信息")
            return

        with connection.cursor() as cursor:
            query = f"UPDATE users SET {db_field} = %s, updated_at = NOW() WHERE id = %s"
            cursor.execute(query, (new_info, user_id))
        connection.commit()
        messagebox.showinfo("成功", "用户信息更新成功")

    def view_reservations(self):
        user_id = self.reservation_user_id_entry.get()
        with connection.cursor() as cursor:
            query = """
            SELECT borrow_records.book_id, books.title, borrow_records.borrow_date, borrow_records.return_date
            FROM borrow_records
            JOIN books ON borrow_records.book_id = books.book_id
            WHERE borrow_records.user_id = %s AND borrow_records.borrow_date IS NULL
            """
            cursor.execute(query, (user_id,))
            result = cursor.fetchall()
            if result:
                result_str = "\n".join(
                    [f"图书ID: {row[0]}, 标题: {row[1]}, 预约日期: {row[2]}, 归还日期: {row[3]}" for row in result])
                messagebox.showinfo("预约记录", result_str)
            else:
                messagebox.showinfo("提示", "无预约记录")


   
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManager(root)
    root.mainloop()

    # 关闭数据库连接
    connection.close()