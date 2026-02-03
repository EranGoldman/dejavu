# 🧠 DejaVu — Personal Visual Memory Assistant

DejaVu is an open‑source project that combines a wearable camera device and an intelligent backend to help users recall daily visual moments. The system continuously captures images, tags them with semantic labels, and enables natural‑language search such as _“When did I last see my keys?”_ or _“Did I close the front door?”_

---

## 🌐 Architecture Overview

**DejaVu** consists of two main components:

### 1. Edge Device (Wearable)
- Runs on Raspberry Pi Zero 2 W or ESP32‑CAM  
- Captures images every 1–2 seconds  
- Stores images locally (SD card)  
- Automatically uploads when connected to a trusted Wi‑Fi network  

### 2. Backend (Flask API)
- Receives uploaded images from the device  
- Uses vision models (e.g., CLIP, TensorFlow, OpenAI API) to tag images  
- Stores metadata (timestamp, objects, location)  
- Supports natural‑language search for object recall  
- Optionally exposes a lightweight web interface or API for queries  

**Optional Components**
- `frontend/` – Simple web UI to visualize images and search results  
- `ai/` – Local or remote image labeling and semantic embedding services  

---

## 🧩 Project Structure

```
dejavu/
├── device/                # Wearable edge code (Pi Zero / ESP32)
│   ├── capture.py
│   ├── uploader.py
│   └── config/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── vision.py
│   ├── db/
│   │   └── schema.sql
│   ├── tests/
│   │   └── test_api.py
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── js/
│       └── main.js
├── docs/
│   └── architecture.md
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

---

## ⚙️ Deployment (Docker Compose)

```bash
git clone https://github.com/EranGoldman/dejavu.git
cd dejavu
cp .env.example .env
docker compose up --build
```

**Services:**
- `flask` – API Server (Port 5000)  
- `db` – PostgreSQL/SQLite  
- `vision` – Optional image tagging microservice  

---

## 👨‍💻 Contribution Guide

1. Fork the repository  
2. Create a feature branch  
3. Commit changes with clear messages  
4. Open a Pull Request  

Before submitting:
- Ensure code passes linting/tests  
- Update documentation in `/docs`  
- Provide descriptive PR comments  

---

## 🧠 Roadmap

- [ ] Object and facial recognition  
- [ ] Natural‑language question parser  
- [ ] Mobile dashboard  
- [ ] Encrypted local storage  

---

## 📜 License

This project is licensed under the **Apache License 2.0**.  
Full text in [`LICENSE`](./LICENSE).

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.apache.org/licenses/LICENSE-2.0
```

---

## ⚖️ Disclaimer

This project was **conceptualized and written by a human developer**, with text formatting and documentation **edited and refined by AI assistance**.  
All code and original content remain human‑authored and community‑maintained.

---

## 💡 Acknowledgments

- Inspired by lifelogging and quantified‑self projects  
- Uses open‑source vision & Flask ecosystem  
- Privacy‑focused and locally deployable  

---

## 🚀 Quick Links

- **Docs:** [`/docs/architecture.md`](./docs/architecture.md)  
- **Issues:** [GitHub Issues](https://github.com/EranGoldman/dejavu/issues)  
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
```

***
