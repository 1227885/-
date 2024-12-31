import pymysql

# 数据库连接配置
db_config = {
    "host": "localhost",  # MySQL 主机
    "user": "root",       # 用户名
    "password": "123456",   # 密码
    "database": "library"  # 数据库名
}

# 连接数据库
def get_db_connection():
    connection = pymysql.connect(**db_config)
    return connection

# 主菜单
def main_menu():
    while True:
        print("\n==================== 图书管理系统 ====================")
        print("1. 用户管理")
        print("2. 图书管理")
        print("3. 借书还书管理")
        print("4. 查询功能")
        print("5. 借阅图书")
        print("6. 归还图书")
        print("7. 查询图书")
        print("8. 查询个人借阅记录")
        print("9. 为图书添加评分")
        print("10. 查看图书评分")
        print("11. 获取图书推荐")
        print("12. 预约图书")
        print("13. 查看个人预约记录")
        print("14. 修改个人信息")
        print("15. 退出系统")
        choice = input("请输入选择（1-15）: ")
        
        if choice == '1':
            user_management()
        elif choice == '2':
            book_management()
        elif choice == '3':
            borrow_return_management()
        elif choice == '4':
            query_function()
        elif choice == '5':
            borrow_book()
        elif choice == '6':
            return_book()
        elif choice == '7':
            query_book()
        elif choice == '8':
            query_borrow_records()
        elif choice == '9':
            rate_book()
        elif choice == '10':
            view_book_rating()
        elif choice == '11':
            get_book_recommendations()
        elif choice == '12':
            reserve_book()
        elif choice == '13':
            view_reservation_records()
        elif choice == '14':
            modify_user_info()
        elif choice == '15':
            print("退出系统")
            break
        else:
            print("无效的选择，请重新输入！")

# 用户管理菜单
def user_management():
    while True:
        print("\n--- 用户管理 ---")
        print("1. 添加用户")
        print("2. 删除用户")
        print("3. 修改用户信息")
        print("4. 查询所有用户")
        print("0. 返回主菜单")
        choice = input("请输入选择: ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            modify_user_info()
        elif choice == '4':
            query_all_users()
        elif choice == '0':
            break
        else:
            print("无效选择，重新输入！")

# 图书管理菜单
def book_management():
    while True:
        print("\n--- 图书管理 ---")
        print("1. 添加图书")
        print("2. 删除图书")
        print("3. 修改图书信息")
        print("4. 查询所有图书")
        print("0. 返回主菜单")
        choice = input("请输入选择: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            delete_book()
        elif choice == '3':
            modify_book_info()
        elif choice == '4':
            query_all_books()
        elif choice == '0':
            break
        else:
            print("无效选择，重新输入！")

# 借书还书管理菜单
def borrow_return_management():
    while True:
        print("\n--- 借书还书管理 ---")
        print("1. 借书")
        print("2. 还书")
        print("0. 返回主菜单")
        choice = input("请输入选择: ")
        
        if choice == '1':
            borrow_book()
        elif choice == '2':
            return_book()
        elif choice == '0':
            break
        else:
            print("无效选择，重新输入！")

# 查询功能菜单
def query_function():
    while True:
        print("\n--- 查询功能 ---")
        print("1. 查询用户信息")
        print("2. 查询图书信息")
        print("3. 查询借阅记录")
        print("4. 查询预约记录")
        print("0. 返回主菜单")
        choice = input("请输入选择: ")
        
        if choice == '1':
            query_user_info()
        elif choice == '2':
            query_book_info()
        elif choice == '3':
            query_borrow_records()
        elif choice == '4':
            query_reservation_records()
        elif choice == '0':
            break
        else:
            print("无效选择，重新输入！")

# 添加用户
def add_user():
    print("\n--- 添加用户 ---")
    username = input("请输入用户名: ")
    email = input("请输入邮箱: ")
    phone = input("请输入电话: ")
    role = input("请输入角色 (admin/user): ")
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO users (username, email, phone, role)
        VALUES (%s, %s, %s, %s)
    """, (username, email, phone, role))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    print("用户添加成功!")

# 删除用户
def delete_user():
    user_id = int(input("请输入要删除的用户ID: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    print("用户删除成功!")

# 修改用户
def modify_user_info():
    user_id = int(input("请输入要修改的用户ID: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    if user:
        print(f"当前信息：用户名: {user[1]}, 邮箱: {user[2]}, 电话: {user[3]}, 角色: {user[4]}")
        email = input("请输入新的邮箱: ")
        phone = input("请输入新的电话: ")
        
        cursor.execute("""
            UPDATE users 
            SET email = %s, phone = %s
            WHERE id = %s
        """, (email, phone, user_id))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("用户信息修改成功!")
    else:
        print("未找到该用户!")

# 添加图书
def add_book():
    title = input("请输入书名: ")
    author = input("请输入作者: ")
    isbn = input("请输入国际标准书号: ")
    publisher = input("请输入出版社: ")
    publish_date = input("请输入出版日期: ")
    total_stock = int(input("请输入总库存: "))
    available_stock = total_stock  # 初始时可借数量等于总库存
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO books (title, author, isbn, publisher, publish_date, total_stock, available_stock)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (title, author, isbn, publisher, publish_date, total_stock, available_stock))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"图书 {title} 添加成功!")

# 查询所有用户
def query_all_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, username, role FROM users")
    users = cursor.fetchall()
    
    for user in users:
        print(f"ID: {user[0]}, 用户名: {user[1]}, 角色: {user[2]}")
    
    cursor.close()
    connection.close()

def add_book():
    print("\n--- 添加图书 ---")
    title = input("请输入书名: ")
    author = input("请输入作者: ")
    isbn = input("请输入ISBN: ")
    publisher = input("请输入出版社: ")
    total_stock = int(input("请输入总库存量: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO books (title, author, isbn, publisher, total_stock, available_stock)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, author, isbn, publisher, total_stock, total_stock))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    print("图书添加成功!")

def delete_book():
    book_id = int(input("请输入要删除的图书ID: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    print("图书删除成功!")

def modify_book_info():
    book_id = int(input("请输入要修改的图书ID: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    
    if book:
        print(f"当前图书信息：书名: {book[1]}, 作者: {book[2]}, ISBN: {book[3]}, 出版社: {book[4]}, 总库存: {book[5]}, 可借库存: {book[6]}")
        
        title = input("请输入新的书名: ")
        author = input("请输入新的作者: ")
        publisher = input("请输入新的出版社: ")
        total_stock = int(input("请输入新的总库存量: "))
        
        cursor.execute("""
            UPDATE books 
            SET title = %s, author = %s, publisher = %s, total_stock = %s, available_stock = %s
            WHERE id = %s
        """, (title, author, publisher, total_stock, total_stock, book_id))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("图书信息修改成功!")
    else:
        print("未找到该图书!")


# 查询所有图书
def query_all_books():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, title, author, isbn, publisher FROM books")
    books = cursor.fetchall()
    
    for book in books:
        print(f"ID: {book[0]}, 书名: {book[1]}, 作者: {book[2]}, ISBN: {book[3]}, 出版社: {book[4]}")
    
    cursor.close()
    connection.close()

# 示例：借书功能
def borrow_book():
    user_id = int(input("请输入用户ID: "))
    book_id = int(input("请输入图书ID: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT available_stock FROM books WHERE id = %s", (book_id,))
    available_stock = cursor.fetchone()[0]
    
    if available_stock > 0:
        cursor.execute("""
            INSERT INTO borrow_records (user_id, book_id, borrow_date, return_date)
            VALUES (%s, %s, NOW(), NULL)
        """, (user_id, book_id))
        
        cursor.execute("""
            UPDATE books SET available_stock = available_stock - 1 WHERE id = %s
        """, (book_id,))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("借书成功!")
    else:
        print("该书已借完!")

def query_book():
    book_id = int(input("请输入要查询的图书ID: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT id, title, author, isbn, publisher, total_stock, available_stock
        FROM books
        WHERE id = %s
    """, (book_id,))
    
    book = cursor.fetchone()
    
    if book:
        print(f"图书信息：")
        print(f"ID: {book[0]}, 书名: {book[1]}, 作者: {book[2]}, ISBN: {book[3]}, 出版社: {book[4]}")
        print(f"总库存: {book[5]}, 可借库存: {book[6]}")
    else:
        print("未找到该图书!")
    
    cursor.close()
    connection.close()

# 还书功能
def return_book():
    borrow_id = int(input("请输入借阅记录ID: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # 获取借阅记录中的图书ID
    cursor.execute("SELECT book_id FROM borrow_records WHERE id = %s", (borrow_id,))
    book_id = cursor.fetchone()[0]  # 提取 book_id
    
    if book_id is None:
        print("未找到该借阅记录!")
        cursor.close()
        connection.close()
        return
    
    # 更新借阅记录的还书日期
    cursor.execute("""
        UPDATE borrow_records 
        SET return_date = NOW() 
        WHERE id = %s
    """, (borrow_id,))
    
    # 更新图书的可借库存
    cursor.execute("""
        UPDATE books 
        SET available_stock = available_stock + 1 
        WHERE id = %s
    """, (book_id,))
    
    # 提交事务
    connection.commit()
    
    cursor.close()
    connection.close()
    
    print("还书成功!")

def reserve_book():
    user_id = int(input("请输入用户ID: "))
    book_id = int(input("请输入图书ID: "))
    
    # 检查图书是否可借
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT available_stock FROM books WHERE id = %s
    """, (book_id,))
    available_stock = cursor.fetchone()
    
    if available_stock and available_stock[0] == 0:
        # 如果库存为0，则允许预约
        cursor.execute("""
            INSERT INTO reservations (user_id, book_id, reservation_date)
            VALUES (%s, %s, NOW())
        """, (user_id, book_id))
        
        connection.commit()
        print("图书预约成功!")
    else:
        print("该图书可借，无法预约!")
    
    cursor.close()
    connection.close()

def view_reservation_records():
    user_id = int(input("请输入用户ID: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT reservations.id, books.title, reservations.reservation_date
        FROM reservations
        JOIN books ON reservations.book_id = books.id
        WHERE reservations.user_id = %s
    """, (user_id,))
    
    records = cursor.fetchall()
    
    if records:
        print("\n预约记录：")
        for record in records:
            print(f"预约ID: {record[0]}, 书名: {record[1]}, 预约日期: {record[2]}")
    else:
        print("没有预约记录!")
    
    cursor.close()
    connection.close()

def query_user_info():
    user_id = int(input("请输入用户ID查询: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, username, email, phone, role FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    if user:
        print(f"ID: {user[0]}, 用户名: {user[1]}, 邮箱: {user[2]}, 电话: {user[3]}, 角色: {user[4]}")
    else:
        print("未找到该用户!")
    
    cursor.close()
    connection.close()

def query_book_info():
    book_id = int(input("请输入图书ID查询: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, title, author, isbn, publisher, total_stock, available_stock FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    
    if book:
        print(f"ID: {book[0]}, 书名: {book[1]}, 作者: {book[2]}, ISBN: {book[3]}, 出版社: {book[4]}, 总库存: {book[5]}, 可借库存: {book[6]}")
    else:
        print("未找到该图书!")
    
    cursor.close()
    connection.close()

def query_borrow_records():
    user_id = int(input("请输入用户ID查询借阅记录: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT borrow_records.id, books.title, borrow_records.borrow_date, borrow_records.return_date
        FROM borrow_records
        JOIN books ON borrow_records.book_id = books.id
        WHERE borrow_records.user_id = %s
    """, (user_id,))
    
    records = cursor.fetchall()
    
    if records:
        for record in records:
            print(f"借阅ID: {record[0]}, 书名: {record[1]}, 借阅日期: {record[2]}, 归还日期: {record[3]}")
    else:
        print("未找到该用户的借阅记录!")
    
    cursor.close()
    connection.close()

def rate_book():
    user_id = int(input("请输入用户ID: "))
    book_id = int(input("请输入图书ID: "))
    rating = int(input("请输入评分（1-5）: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO book_ratings (user_id, book_id, rating)
        VALUES (%s, %s, %s)
    """, (user_id, book_id, rating))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    print("评分提交成功!")

def view_book_rating():
    book_id = int(input("请输入图书ID: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT AVG(rating) FROM book_ratings WHERE book_id = %s
    """, (book_id,))
    
    avg_rating = cursor.fetchone()[0]
    
    if avg_rating:
        print(f"图书的平均评分是: {avg_rating:.2f}")
    else:
        print("该图书没有评分!")
    
    cursor.close()
    connection.close()


def query_reservation_records():
    user_id = int(input("请输入用户ID查询预约记录: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT reservation_records.id, books.title, reservation_records.reserve_date
        FROM reservation_records
        JOIN books ON reservation_records.book_id = books.id
        WHERE reservation_records.user_id = %s
    """, (user_id,))
    
    records = cursor.fetchall()
    
    if records:
        for record in records:
            print(f"预约ID: {record[0]}, 书名: {record[1]}, 预约日期: {record[2]}")
    else:
        print("未找到该用户的预约记录!")
    
    cursor.close()
    connection.close()

def modify_user_info():
    user_id = int(input("请输入用户ID修改信息: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, username, email, phone, role FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    if user:
        print(f"当前用户信息: 用户名: {user[1]}, 邮箱: {user[2]}, 电话: {user[3]}, 角色: {user[4]}")
        
        email = input("请输入新的邮箱: ")
        phone = input("请输入新的电话: ")
        
        cursor.execute("""
            UPDATE users SET email = %s, phone = %s WHERE id = %s
        """, (email, phone, user_id))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("用户信息更新成功!")
    else:
        print("未找到该用户!")

def get_book_recommendations():
    user_id = int(input("请输入用户ID获取推荐图书: "))
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT books.title, COUNT(*) as borrow_count
        FROM borrow_records
        JOIN books ON borrow_records.book_id = books.id
        WHERE borrow_records.user_id = %s
        GROUP BY books.title
        ORDER BY borrow_count DESC
        LIMIT 5
    """, (user_id,))
    
    recommendations = cursor.fetchall()
    
    if recommendations:
        print("根据您的借阅历史，推荐以下图书:")
        for book in recommendations:
            print(f"书名: {book[0]}, 借阅次数: {book[1]}")
    else:
        print("未找到相关的借阅记录，无法推荐图书!")
    
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main_menu()


