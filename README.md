# 🧠 Scholarly: A Django-Based Discussion Hub

Scholarly is a full-featured web application built with Django, designed to foster meaningful discussions in structured, topic-based chat rooms. Users can browse and participate in conversations even without logging in, while registered users can create rooms, post messages, and manage their profiles.

---

## 🚀 Features

- 🔐 **User Authentication** (Login, Register, Logout)
- 💬 **Real-time Discussion Rooms**
- 🔎 **Search Functionality** across rooms, topics, and messages
- 🧵 **Topic-Based Filtering** for organized content
- 📝 **User Profiles** with activity overview
- ➕ **Room Creation & Editing** (only for authenticated users)
- ❌ **Message/Room Deletion** with proper permissions
- 📂 **Topic Browser & Activity Feed**
- 🌐 **Guest Mode** — Explore without logging in

---

## 🛠️ Tech Stack

| Tech         | Purpose                        |
|--------------|--------------------------------|
| Python 3.x   | Core language                  |
| Django       | Web framework (views, models)  |
| SQLite       | Default lightweight database   |
| HTML/CSS     | Frontend structure & styling   |
| Bootstrap    | Responsive UI design           |
| Django ORM   | Database querying & relations  |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/scholarly.git
cd scholarly
```

### 2. Set up a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, run:
> ```bash
> pip freeze > requirements.txt
> ```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Then visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Testing / Demo

- You can **browse rooms and topics** without logging in.
- **Creating rooms, posting messages**, and **editing your profile** require login.
- No test accounts are pre-configured — you can register manually from the app.

---

## 🔒 Notes

- No `.env` file or secret management is used — but you’re encouraged to use one in production.
- CSRF protection and authentication checks are implemented via Django's decorators.

---

