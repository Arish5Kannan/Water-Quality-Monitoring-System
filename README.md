
## **🌟 WQMS - Water Quality Monitoring System**  

WQMS (Water Quality Monitoring System) is a **full-stack web application** built using **Python, Django, MySQL, HTML, CSS, JavaScript, and Bootstrap**. It provides a **real-time dashboard** to monitor water quality parameters such as **pH level, turbidity, temperature, and dissolved oxygen**. 📊🚰  

It integrates **email services**, **WhatsApp API**, and **Chart.js** to provide instant alerts and data visualization. The system ensures that users can make data-driven decisions about water quality management.  

---

## **🚀 Features**
✅ **Real-time Water Quality Monitoring** (pH, Turbidity, Temperature, etc.)  
✅ **Interactive Dashboard** with **Chart.js** for data visualization 📊  
✅ **Email Notifications** 📧 for critical alerts  
✅ **WhatsApp API Integration** 📱 for instant messaging alerts  
✅ **User Authentication** (Login/Register) 🔐  
✅ **Dynamic Reports & Data Logs** 📄  
✅ **Font Awesome Icons** for UI enhancement 🎨  
✅ **Bootstrap for Responsive Design** 📱  

---

## **🛠️ Tech Stack**
| Technology | Purpose |
|------------|---------|
| **Python** | Backend Logic |
| **Django** | Web Framework |
| **MySQL** | Database |
| **HTML, CSS, JavaScript** | Frontend |
| **Bootstrap** | Responsive UI |
| **Chart.js** | Data Visualization |
| **Font Awesome** | UI Icons |
| **WhatsApp API** | Alerts & Notifications |
| **Email Services** | User Notifications |

---

## **📂 Project Structure**
```
📦 WQMS
 ┣ 📂 static/               # CSS, JavaScript, Images, Icons
 ┣ 📂 templates/            # HTML Files
 ┣ 📂 wqms/                 # Django App
 ┃ ┣ 📜 settings.py         # Project Settings
 ┃ ┣ 📜 urls.py             # URL Routing
 ┃ ┣ 📜 views.py            # Business Logic
 ┃ ┣ 📜 models.py           # Database Models
 ┃ ┣ 📜 forms.py            # Django Forms
 ┃ ┣ 📜 api.py              # WhatsApp API Integration
 ┣ 📜 manage.py             # Django Management Script
 ┣ 📜 README.md             # Project Documentation
 ┣ 📜 requirements.txt      # Dependencies
 ┣ 📜 db.sqlite3            # Database File (For Development)
```

---

## **⚡ Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/wqms.git
cd wqms
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure the Database**
- Open `settings.py` and update **DATABASES**:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wqms_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
- Run Migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Create a Superuser (Admin Panel)**
```bash
python manage.py createsuperuser
```
Follow the prompt and enter **username, email, and password**.

### **6️⃣ Run the Server**
```bash
python manage.py runserver
```
Now, open **`http://127.0.0.1:8000/`** in your browser.

---

## **📌 Dependencies**
Ensure you have the following installed:
```
Django==4.2
mysqlclient==2.1.1
requests==2.28.1   # For API calls
django-whitenoise  # For static files
chart.js           # For charts
font-awesome       # For icons
```
Install them using:
```bash
pip install django mysqlclient requests django-whitenoise
```

---

## **📧 Email & WhatsApp API Setup**
### **Email Services**
- Configure SMTP in `settings.py`
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
```
- Don't forget to enable **"Less secure apps"** in Gmail.

### **WhatsApp API**
- Use `requests` to send messages:
```python
import requests

def send_whatsapp_alert(number, message):
    url = "https://api.whatsapp.com/send?phone={}&text={}".format(number, message)
    response = requests.get(url)
    return response.status_code
```

---

## **🛠️ Contributing**
1. Fork the repo 🍴  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Make changes & commit (`git commit -m "Added feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Create a Pull Request ✅  

---

## **📝 License**
This project is **open-source** and available under the **MIT License**.

---

## **💬 Contact**
📩 Email: [arishkannan941@gmail.com](mailto:arishkannan941@gmail.com)  
🔗 LinkedIn: [Arish Kannan](https://www.linkedin.com/in/arish-kannan-859b10285/)  
🚀 GitHub: [Arish5Kannan](https://github.com/Arish5Kannan)  

---

