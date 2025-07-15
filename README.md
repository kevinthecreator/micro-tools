# 🧰 Micro Tools Web App

A collection of small but useful tools built with **FastAPI**, **HTML/CSS**, and **Bootstrap**.  
Perfect for learning, portfolios, and daily use.

---

## 🔧 Included Tools

| Tool Name           | Description                                         |
|---------------------|-----------------------------------------------------|
| 🔑 Password Generator | Generate strong, random passwords of any length     |
| ✂️ Slug Formatter     | Convert text into URL-friendly slugs               |
| 📖 Lorem Ipsum       | Generate random paragraphs of filler text          |
| 🔁 Unit Converter    | Convert between km/miles and kg/lbs                 |
| 📮 Email Extractor   | Extract emails from large text blocks               |

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Frontend:** Jinja2 + HTML + Bootstrap
- **Styling:** CSS3 + Responsive layout
- **Utilities:** Regex, Random, Lorem Generator

---

## 📦 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/micro-tools.git
cd micro-tools
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn jinja2 lorem
```

### 4. Run the app

```bash
uvicorn main:app --reload
```

### 5. Open in browser

```
http://127.0.0.1:8000
```

---

## 🗂️ Folder Structure

```
micro_tools/
├── main.py
├── templates/
│   ├── base.html
│   ├── home.html
│   └── tools/
├── static/
│   └── style.css
└── README.md
```

---

## 🧑‍💻 Author

**Ravy Sovann** – Master of IT Graduate | Aspiring Software Engineer  
---

## 🪪 License

This project is licensed under the MIT License.
