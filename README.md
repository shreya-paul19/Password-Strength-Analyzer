# 🔐 Password Security Analyzer

A cybersecurity-focused web application that evaluates password strength, calculates entropy, estimates crack time, detects breached passwords, generates secure passwords, and visualizes security analytics through an interactive dashboard.

🌐 **Live Demo:** https://password-strength-analyzer-n4q9.onrender.com

---

## 🚀 Features

### ✅ Password Strength Analysis

* Analyzes password complexity
* Classifies passwords as Weak, Medium, or Strong
* Provides a security score

### ✅ Entropy Calculation

* Calculates password entropy
* Measures randomness and resistance against brute-force attacks

### ✅ Crack Time Estimation

* Estimates how long it would take to crack a password
* Displays user-friendly security metrics

### ✅ Common Password Detection

* Identifies commonly used passwords
* Warns users about insecure password choices

### ✅ Password Policy Validation

Checks whether a password satisfies:

* Minimum 12 characters
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

### ✅ Password Breach Detection

* Checks passwords against known data breaches
* Uses the Have I Been Pwned (HIBP) Password API
* Implements k-Anonymity for privacy protection

### ✅ Secure Password Generator

* Generates strong random passwords
* Helps users create secure credentials instantly

### ✅ Security Analytics Dashboard

* Stores analysis results using SQLite
* Displays:

  * Total analyses
  * Weak passwords
  * Medium passwords
  * Strong passwords
* Visualizes data using Chart.js

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript

### Libraries & APIs

* Requests
* Chart.js
* Have I Been Pwned Password API

---

## 📂 Project Structure

```text
Password-Strength-Analyzer/
│
├── app.py
├── breach_checker.py
├── database.py
├── password_checker.py
├── password_generator.py
├── policy_checker.py
├── entropy.py
├── crack_time.py
├── common_passwords.txt
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/shreya-paul19/Password-Strength-Analyzer.git
cd Password-Strength-Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## 📸 Screenshots

Screenshots are available in the `screenshots` folder.

* Home Page
* Password Analysis
* Security Dashboard
* Password Generator

---

## 🔒 Security Concepts Demonstrated

* Password Security Analysis
* Password Entropy Calculation
* Password Breach Detection
* Secure Password Generation
* API Integration
* Database Management
* Security Analytics
* Secure Coding Practices

---

## 🎯 Future Improvements

* User Authentication System
* Password History Tracking
* PDF Security Reports
* Dark/Light Theme Toggle
* Multi-User Dashboard
* AI-Based Password Recommendations

---

## 🏆 Internship Project

This project was developed as part of the **SkillCraft Technology Internship Program** and demonstrates practical cybersecurity concepts including password analysis, breach detection, entropy calculation, secure password generation, and security analytics.

---

## 👩‍💻 Author

**Shreya Paul**

Cybersecurity Student | Security Research Intern

Aspiring SOC Analyst

GitHub: https://github.com/shreya-paul19

---

## 📜 License

This project is developed for educational, learning, and portfolio purposes.
