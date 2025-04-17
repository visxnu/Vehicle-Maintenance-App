# 🚗 Pro-Mechanic: Vehicle Maintenance App

Welcome to **Pro-Mechanic**, an intelligent and interactive Django-based web application designed to streamline vehicle maintenance for users and mechanics. Whether it's scheduling services, tracking repairs, or managing your vehicle history — Pro-Mechanic makes it all easier.

## 🛠️ Features

- 🔧 **User & Mechanic Roles** – Dual-role login system with dedicated dashboards.
- 🗓️ **Service Booking** – Users can schedule appointments for various services.
- 📊 **Maintenance History** – Track service history, parts replaced, and more.
- 🧰 **Mechanic Dashboard** – View assigned tasks, update status, and manage bookings.
- 📩 **Notifications** – Stay updated with appointment status & reminders.
- 🎨 **Beautiful UI** – Clean, responsive, and intuitive interface for smooth navigation.

## 🧑‍💻 Tech Stack

- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Backend:** Django (Python)
- **Database:** SQLite (can be upgraded to PostgreSQL)
- **Others:** Django Admin, Authentication, Forms, Responsive Design

---

## 🚀 Getting Started

### 🔗 Clone the repository

```bash
git clone https://github.com/visxnu/Vehicle-Maintenance-App.git
cd Vehicle-Maintenance-App
```

### 📦 Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 🔧 Install requirements

```bash
pip install -r requirements.txt
```

### 🛠️ Run the server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to explore the app locally.

---

## 🔐 Credentials (for testing)

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin123` |
| User | `user1` | `userpass` |
| Mechanic | `mech1` | `mechpass` |

> *You can add new users and roles via Django Admin Panel.*

---

## 📂 Folder Structure

```bash
├── vehicle_maintenance/
│   ├── static/
│   ├── templates/
│   ├── users/
│   ├── services/
│   ├── mechanics/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📌 Future Enhancements

- ✅ Email & SMS notifications
- ✅ Rating and reviews for mechanics
- ✅ Payment gateway integration
- ✅ Vehicle document storage
- ✅ Auto-reminders for service intervals

---

## 👨‍💻 Developed By

**Vishnu**  
📧 [Connect on LinkedIn](www.linkedin.com/in/visxu)  
🔗 [Portfolio](https://profile-vishnu-v.vercel.app/)

---

## ⭐ Give it a Star!

If you like this project, don’t forget to ⭐ the repo!

---

Let me know if you want to include demo videos, deploy it on a cloud server (like Render/Heroku), or turn this into a portfolio-ready presentation. I can also help create a logo or interface screenshots if needed.
