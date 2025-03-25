
```
# Hospital Management System

This is a Hospital Management System implemented in Python using MySQL as the database. The system allows user registration, authentication, and management of hospital staff (doctors, nurses, other workers) and patients.

---

## Features

- User Registration and Authentication  
- Staff Management (Doctors, Nurses, Other Workers)  
- Patient Management  
- MySQL Database Connectivity  
- Table Creation and Data Storage  

---

## Tech Stack

- Backend: Python  
- Database: MySQL  

---

## Installation and Setup

### 1. Prerequisites

Ensure you have the following installed:
- Python (>= 3.x)  
- MySQL Server  
- mysql-connector-python package  

### 2. Clone the Repository
```
git clone <repository_link>
cd hospital-management-system
```

### 3. Install Required Packages
Run the following command to install the MySQL connector:
```
pip install mysql-connector-python
```

### 4. Create the MySQL Database
Open MySQL and create the database:
```
CREATE DATABASE hospital_db;
```

### 5. Update MySQL Credentials
In the Python code, replace the placeholder values with your MySQL credentials:
```
connection = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="hospital_db",
    connect_timeout=10
)
```

### 6. Run the Program
Execute the Python file:
```
python hospital_management.py
```

---

## Usage

1. Sign Up: Register a new user by providing a username and password.  
2. Sign In: Log in with your registered credentials.  
3. Manage Data:  
   - Add new doctors, nurses, or other workers.  
   - Manage patient records.  
4. Exit: You can exit the application by selecting the appropriate option.  

---

## Database Schema

**Users Table:**  
- username: VARCHAR(50), PRIMARY KEY  
- password: VARCHAR(255), NOT NULL  

**Doctors Table:**  
- id: INT, AUTO_INCREMENT, PRIMARY KEY  
- name: VARCHAR(100), NOT NULL  
- specialisation: VARCHAR(100)  
- age: INT  
- address: VARCHAR(255)  
- contact: VARCHAR(15)  
- fees: DECIMAL(10,2)  
- monthly_salary: DECIMAL(10,2)  

**Nurses Table:**  
- id: INT, AUTO_INCREMENT, PRIMARY KEY  
- name: VARCHAR(100), NOT NULL  
- age: INT  
- address: VARCHAR(255)  
- contact: VARCHAR(15)  
- monthly_salary: DECIMAL(10,2)  

**Other Workers Table:**  
- id: INT, AUTO_INCREMENT, PRIMARY KEY  
- name: VARCHAR(100), NOT NULL  
- age: INT  
- address: VARCHAR(255)  
- contact: VARCHAR(15)  
- monthly_salary: DECIMAL(10,2)  

**Patients Table:**  
- id: INT, AUTO_INCREMENT, PRIMARY KEY  
- patient_id: VARCHAR(50), UNIQUE  
- name: VARCHAR(100), NOT NULL  
- age: INT  
- address: VARCHAR(255)  
- doctor_recommended: VARCHAR(100)  

---
