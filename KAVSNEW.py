import mysql.connector

def connect_db():
    print("Connecting to MySQL...")
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kavanami@123",
            database="hospital_db",
            connect_timeout=10  # Timeout after 10 seconds
        )
        print("Connected successfully!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None



def create_tables():
    db = connect_db()
    cursor = db.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(50) PRIMARY KEY,
        password VARCHAR(255) NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        specialisation VARCHAR(100),
        age INT,
        address VARCHAR(255),
        contact VARCHAR(15),
        fees DECIMAL(10,2),
        monthly_salary DECIMAL(10,2)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nurses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        address VARCHAR(255),
        contact VARCHAR(15),
        monthly_salary DECIMAL(10,2)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS other_workers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        address VARCHAR(255),
        contact VARCHAR(15),
        monthly_salary DECIMAL(10,2)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id VARCHAR(50) UNIQUE,
        name VARCHAR(100),
        age INT,
        address VARCHAR(255),
        doctor_recommended VARCHAR(100)
    )
    """)
    
    db.commit()
    cursor.close()
    db.close()

def register_user(username, password):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()
    cursor.close()
    db.close()

def validate_user(username, password):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    db.close()
    return user

def main():
    create_tables()
    print("WELCOME TO KMI HOSPITALS PVT. LTD.")
    
    while True:
        print("\n1. SIGN IN (LOGIN)\n2. SIGN UP (REGISTER)\n3. EXIT APPLICATION")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 3:
                print("Thank you for using KMI Hospital Management System. Goodbye!")
                break
            elif choice == 2:
                username = input("ENTER YOUR PREFERRED USERNAME: ")
                password = input("ENTER YOUR PREFERRED PASSWORD: ")
                register_user(username, password)
                print("REGISTERED SUCCESSFULLY!")
            elif choice == 1:
                username = input("ENTER YOUR USERNAME: ")
                password = input("ENTER YOUR PASSWORD: ")
                if validate_user(username, password):
                    print("LOGIN SUCCESSFUL!")
                else:
                    print("Invalid username or password. Please try again.")
            else:
                print("Invalid choice. Please enter 1, 2, or 3")
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()

try:
    create_tables()
except Exception as e:
    print("Error:", e)
mysql.connector.connect(
    host="localhost",
    user="root",
    password="kavanami@123",
    database="hospital_db",
    connect_timeout=10  # Fail if no response in 10 seconds
)
