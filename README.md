# Employee Directory Web Application with Selenium Automation on AWS EC2

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Selenium](https://img.shields.io/badge/Testing-Selenium-orange)
![Pytest](https://img.shields.io/badge/Test%20Runner-pytest-yellow)
![AWS](https://img.shields.io/badge/Cloud-AWS%20EC2-red)

## 📌 Project Overview

This project is a simple Employee Directory web application developed using Python Flask and SQLite.
It allows users to add employee names and view the updated employee list.

The application is deployed on an AWS EC2 Ubuntu instance and tested using Selenium automation with pytest.

---

## 🎯 Features

* Add Employee Name
* Display Employee List
* Store Data in SQLite Database
* Publicly Accessible using AWS EC2 Public IP
* Automated UI Testing using Selenium
* CLI Test Execution using pytest

---

## 🛠️ Tech Stack

* Python 3
* Flask
* SQLite
* Selenium WebDriver
* pytest
* AWS EC2 (Ubuntu Linux)

---

## 🏗️ Project Structure

```text
employee-directory/
│── app.py
│── requirements.txt
│── employees.db
│── templates/
│   └── index.html
└── tests/
    └── test_app.py
```

---

## 🚀 Application Deployment

Hosted on AWS EC2 Instance:

```text
http://3.110.163.78:5000
```

---

## ▶️ Run Application

```bash
python3 app.py
```

---

## 🧪 Run Automated Tests

```bash
pytest -v
```

### Test Result

```text
tests/test_app.py::test_add_employee PASSED
1 passed
```

---

## 🤖 Selenium Test Scenario

* Open Employee Directory using EC2 Public IP
* Enter employee name
* Click Add Employee
* Verify employee appears in list

---

## 📸 Screenshots

### Application Running on AWS EC2

*Add browser screenshot here*

### Selenium Test Execution

*Add terminal screenshot here*

---

## ☁️ AWS Configuration

* EC2 Ubuntu Instance
* Security Group Rules:

  * Port 22 (SSH)
  * Port 5000 (Application Access)

---

## 📚 Learning Outcomes

* Web Application Deployment on AWS
* Flask Application Hosting
* SQLite Database Integration
* Selenium Automation Testing
* CLI Test Execution
* Cloud Troubleshooting & Debugging

---

## 👨‍💻 Author

Siva Sai Teja Gurram
