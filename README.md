# Django Scholarship - Projects

A collection of my Django learning projects, experiments, and portfolio pieces.

## 🚀 Quick Start (For Any Project)

### Prerequisites

- Python 3.10 or higher
- Git
- pip (comes with Python)

### Setup a Project

### 1. Navigate to project

```bash
cd <foldername>
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

| Platform  | Script                      |
| --------- | --------------------------- |
| Windows   | `.venv\Scripts\activate `   |
| Mac/Linux | `source .venv/bin/activate` |

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run development server

```bash
python manage.py runserver
```

Now, the project should be running at `http://localhost:8000/`!

You can access the admin panel at `http://localhost:8000/admin/` if you created a superuser.
