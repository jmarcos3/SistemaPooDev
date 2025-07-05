# 🏍️ Motorcycle Dealership Management System

## 📋 Overview

This management system was developed as part of the **Object-Oriented Programming Paradigms for Software Development** course in the **Computer Science** program at the **Universidade Estadual do Norte Fluminense (UENF)**.

Built in **Python** with a **Tkinter** GUI and **SQLite** for persistence, the application models the key operations of a motorcycle dealership. It applies core OOP principles—encapsulation, inheritance and responsibility segregation—by defining distinct user roles (Manager, Salesperson, Mechanic, Secretary), each with tailored permissions.

---

## 🎯 Role-Based Features

### Manager
- Full system access
- Create, read, update, delete (CRUD) for:
  - Motorcycles
  - Customers
  - Sales
  - Service appointments
  - Employees

### Salesperson
- Browse available motorcycles
- Add & edit customer records
- Register and view sales

### Mechanic
- View scheduled service appointments
- Update service status

### Secretary
- View motorcycles and sales
- Schedule and view service appointments

---

## 📦 Core Functionality

1. **Customer Management**  
   - Add, update, list and remove customers  
   - Captures: name, CPF, email

2. **Motorcycle Inventory**  
   - Add new bikes with model, year, color, price and chassis  
   - Update details or remove stock

3. **Sales Processing**  
   - Record sales by linking customer CPF to motorcycle chassis  
   - View and edit completed transactions

4. **Service Scheduling**  
   - Create appointments tied to a customer (CPF) and motorcycle (chassis)  
   - Assign a mechanic and set the service date  
   - Track service status

5. **Employee Directory**  
   - Manage staff records (name, CPF, role)  

---

## 🛠️ Technologies

- **Python** — Core application logic  
- **Tkinter** — Native GUI toolkit  
- **SQLite** — Lightweight embedded database  

---

## 🔍 Key Learnings

- Designing modular, role-based systems with clear separation of concerns  
- Applying OOP principles (encapsulation, inheritance, polymorphism) in Python  
- Building desktop GUIs with Tkinter  
- Persisting data in an embedded database with SQLite  
- Structuring code for maintainability and scalability  

---

