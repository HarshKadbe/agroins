

# 🌾 AgroIns - Agricultural Insurance System 🚜

**AgroIns** is a Django-based web application designed to provide secure and efficient agricultural insurance services. It enables farmers to register, apply for insurance, and track claims seamlessly. 🌱💰

## 📌 Features

✅ **User Authentication & Role Management** 🔑  
✅ **Insurance Policy Management** 📄  
✅ **Claims Processing & Status Tracking** 🏦  
✅ **Django Admin Panel for Management** ⚙️  
✅ **SQLite Database Integration** 🗄️

## 🏗️ Project Structure

```
agroins-main
│── agroins/          # Main Django application
│   ├── settings.py   # Project settings
│   ├── urls.py       # URL routing
│   ├── wsgi.py       # WSGI application entry point
│── db.sqlite3        # SQLite database
│── manage.py         # Django management script
│── .gitignore        # Git ignore file
```

## ⚡ Tech Stack

🔹 **Django** - Python web framework  
🔹 **SQLite** - Database for storage  
🔹 **Django Admin** - Backend management  
🔹 **HTML, CSS, JavaScript** - Frontend

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/HarshKadbe/AgroIns.git
cd agroins-main
```

### 2️⃣ Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Apply Migrations & Run the Server

```bash
python manage.py migrate
python manage.py runserver
```

### 4️⃣ Access the Application

Open your browser and go to:  
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

## 🔐 Admin Panel Access

```bash
python manage.py createsuperuser
```

Login at **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

## 🏗️ Contributing

👨‍💻 Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License

📝 This project is licensed under the MIT License.

