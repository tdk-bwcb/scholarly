# 🧠 Scholarly: A Campus Discussion Platform

Scholarly is a robust, role-based discussion hub engineered to facilitate academic discourse. Built on the **Django MVT architecture**, it provides a structured environment for students and faculty to engage in topic-based dialogue with high-performance search and granular access controls.

---

## 🚀 Key Engineering Highlights

- 🔐 **Advanced RBAC (Role-Based Access Control):** Implemented a granular permission system to enforce specific capabilities for **Faculty, Moderators, and Students**.
- 🔎 **High-Performance Discovery:** Engineered **PostgreSQL Full-Text Search** with vector indexing, enabling ranked results and efficient content discovery across thousands of threads.
- ⚡ **Database Optimization:** Leveraged Django ORM optimization techniques, including **Indexing strategies** and `select_related`/`prefetch_related` to minimize N+1 query problems and reduce lookup latency.
- 📊 **Analytics Dashboards:** Designed interactive views to track user activity metrics and real-time thread engagement.
- 🎨 **Modular UI Architecture:** Utilized **Tailwind CSS** and Django’s modular template inheritance to create a responsive, maintainable frontend.

---

## 🛠️ Tech Stack

| Component      | Technology                                     |
| :------------- | :--------------------------------------------- |
| **Backend** | Python, Django (MVT Architecture)              |
| **Database** | PostgreSQL (Full-Text Search, Vector Indexing)  |
| **Frontend** | JavaScript, Tailwind CSS, HTML5                |
| **Permissions**| Django Contrib Auth (RBAC)                     |

---

## ⚙️ Setup Instructions

### 1. Environment Configuration
```bash
git clone [https://github.com/](https://github.com/)<your-username>/scholarly.git
cd scholarly
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Database Initialization
Ensure your PostgreSQL instance is running and update the DATABASES configuration in settings.py.
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Execution

```bash
python manage.py runserver
```
## 🏛️ System Architecture

> **Role-Based Management:** Engineered a structured content management system using Django's MVT architecture to ensure only authorized users (Faculty, Moderators, Students) can perform CRUD operations on specific categories.
>
> **Search Engine:** Utilizes PostgreSQL's native `SearchVector` and `SearchQuery` for linguistic-aware searching, stemming, and ranking, ensuring highly relevant discussion retrieval.
>
> **Performance Optimization:** Implemented a streamlined query layer using indexing and pre-fetching strategies to handle concurrent discussions with minimal database overhead and low latency.

---

## 🔒 Security & Performance Notes

* **Access Control:** Robust security via CSRF protection and custom role-specific decorators implemented across all sensitive API and View endpoints.
* **Scalability:** The schema is fully optimized for a PostgreSQL backend to support high-concurrency environments typical of large-scale campus deployments.
* **Modular Design:** Employs modular template inheritance and Tailwind CSS for a maintainable, dry, and scalable frontend architecture.
