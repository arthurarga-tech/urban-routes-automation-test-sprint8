
# 🧪 Urban Routes – Automated Testing Project with Selenium

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-automation-green.svg)](https://www.selenium.dev/)


This project automates the end-to-end flow of the Urban Routes ride-hailing application using **Python**, **Selenium**, and **Pytest**. It simulates a complete user journey from route selection to ride confirmation and payment, applying best practices in test automation and project structure.

---

## 🎥 Test Run Preview

Watch the full test execution:

📽️ [Click here to view the video on Loom](https://www.loom.com/share/44837cf21d384af69596ef6b720a103f)

---

## 💻 Tech Stack

- **Language:** Python 3.10+
- **Automation:** Selenium WebDriver
- **Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **Tools:** Virtual Environment (venv), GitHub, VSCode

---

## 📂 Project Structure

urban-routes-automation-test/
│
├── data.py            # Static test data and constants
├── helpers.py         # Utility functions (e.g. server check, SMS code retrieval)
├── pages.py           # Page Object class with locators and methods
├── main.py            # Test class and test functions using Pytest
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

---

## ✅ Test Scenarios

The following scenarios are fully automated and validated:

- 📍 Enter pickup and destination addresses
- 💺 Select the "Comfort" ride plan
- 📱 Fill in phone number and retrieve SMS verification code dynamically
- 💳 Add credit card information via modal
- 📝 Add a custom message for the driver
- 🧣 Request a blanket and tissues
- 🍦 Order two ice creams
- 🚖 Confirm the ride and verify vehicle search modal appears

---

## 🚀 How to Run the Tests Locally

1. **Clone the repository:**
 
   git clone https://github.com/arthurarga-tech/urban-routes-automation-test-sprint8.git
   cd urban-routes-automation-test-sprint8


2. **Create and activate a virtual environment:**

   python -m venv .venv
   .venv\Scripts\activate       # On Windows
   source .venv/bin/activate    # On macOS/Linux


3. **Install the dependencies:**

   pip install -r requirements.txt


4. **Run the tests:**

   pytest main.py


---

## 📌 Key Highlights

- Built using the **Page Object Model (POM)** for better maintainability and separation of concerns.
- Retrieved **real-time SMS codes** via browser logs for verification.
- Managed **dynamic modals** and **focus issues** using Selenium best practices.
- Used `pytest` for structured test execution and reporting.
- Fully structured automation project ready for real-world scenarios.

---

