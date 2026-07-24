# 🚀 DevRoute

> **Building the easiest way to discover tech events in Brazil.**

DevRoute is a modern platform that helps developers discover technology events, conferences, hackathons, meetups and communities across Brazil.

Our mission is to connect developers with opportunities through a fast, intuitive and centralized experience.

---

# ✨ Features

- 🔎 Search technology events
- 📅 Upcoming events
- 📍 Filter by state, city and modality
- ⚡ FastAPI REST API
- 🎨 Modern React interface
- 📄 Pagination
- 🚧 Continuous development

---

# 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688)
![React](https://img.shields.io/badge/React-19-61DAFB)
![Vite](https://img.shields.io/badge/Vite-Latest-646CFF)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![Docker](https://img.shields.io/badge/Docker-Latest-2496ED)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

---

# 🏗️ Architecture

```text
                    DevRoute

        +---------------------------+
        |      React + Vite         |
        +---------------------------+
                     │
                Axios / HTTP
                     │
                     ▼
        +---------------------------+
        |      FastAPI Backend      |
        +---------------------------+
                     │
            Service Layer
                     │
                     ▼
          Repository Layer
                     │
                     ▼
        +---------------------------+
        |        events.json        |
        +---------------------------+

          PostgreSQL (Coming Soon)
```

---

# 📂 Project Structure

```text
DevRoute
│
├── backend
│   ├── api
│   ├── core
│   ├── data
│   ├── database
│   ├── models
│   ├── repositories
│   ├── routers
│   ├── schemas
│   ├── services
│   ├── utils
│   └── main.py
│
└── frontend
    ├── components
    ├── pages
    ├── services
    ├── assets
    └── App.jsx
```

---

# 🚀 Getting Started

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

API:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Application:

```
http://localhost:5173
```

---

# 🔄 User Flow

```text
Landing
    │
    ▼
Search Events
    │
    ▼
Apply Filters
    │
    ▼
View Event
    │
    ▼
Travel Information
    │
    ▼
Favorite
    │
    ▼
Participate
```

---

# 🗺️ Roadmap

## ✅ Completed

- FastAPI Backend
- React Frontend
- Event Cards
- API Pagination
- Search
- Basic Filters
- REST API
- Project Structure

---

## 🚧 In Progress

- Event Status
- Skeleton Loading
- Advanced Search
- Better Filters
- Backend Refactor

---

## 🔮 Planned

- PostgreSQL
- Docker
- Authentication
- User Favorites
- Interactive Map
- AI Recommendations
- Progressive Web App (PWA)
- CI/CD Pipeline

---

# 📈 Project Status

🚧 **Active Development**

Current Version:

```
v0.3.0
```

Last Update:

```
July 2026
```

---

# 🎯 Vision

DevRoute aims to become the leading platform for discovering technology events in Brazil, connecting developers with conferences, meetups, hackathons and networking opportunities through a fast and intuitive experience.

---

# 🤝 Contributing

Contributions, suggestions and feedback are always welcome.

Feel free to open an Issue or submit a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

> **"Connecting developers with opportunities."**
