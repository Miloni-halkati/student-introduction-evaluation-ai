# 🌟 AI-Powered Student Introduction Scoring Tool

[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

An AI-driven evaluation system that scores a student's self-introduction transcript using a detailed rubric.  
It provides a **final score out of 100**, along with a **complete breakdown of all communication and language metrics**.

---

# 📑 Table of Contents
- [✨ Overview](#-overview)
- [🧠 Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 How to Run](#-how-to-run)
- [📊 Evaluation Rubric](#-evaluation-rubric)
- [🌐 Deployment](#-deployment)
- [📄 License](#-license)
- [👩‍💻 Author](#-author)

---

# ✨ Overview

This tool evaluates student introductions based on:
- Content completeness  
- Delivery style  
- Grammar accuracy  
- Vocabulary richness  
- Speech clarity  
- Positivity and engagement  

It provides:
- A numeric score  
- Category-wise scoring  
- JSON output for analysis  
- Clear UI to input or upload transcripts  

Ideal for **schools, educators, NGOs, interviewers, and training programs**.

---

# 🧠 Features

### 🔹 Content & Structure
- Salutation scoring  
- Mandatory keyword detection  
- Good-to-have keyword scoring  
- Flow / structural correctness

### 🔹 Language & Delivery
- Words Per Minute (WPM) calculation  
- Grammar scoring (LanguageTool)  
- TTR (Vocabulary richness)

### 🔹 Clarity & Engagement
- Filler word density  
- Sentiment positivity (VADER compound)

---

# 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend UI | Streamlit |
| Language Processing | NLTK, Sentence Transformers |
| Grammar Engine | LanguageTool |
| Sentiment Engine | VADER |
| Backend Logic | Python |
| Deployment | Streamlit Cloud |

---

# 🚀 **How to Run**

### **1️⃣ Clone Repository**

```bash
git clone https://github.com/Miloni-halkati/student-introduction-evaluation-ai.git
cd student-introduction-evaluation-ai
```

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Streamlit App**

```bash
streamlit run app.py
```

### **4️⃣ Use the Application**

You can:

* Paste transcript text
* Upload a `.txt` file
* Enter audio duration for accurate WPM scoring

The tool will display:

* Final evaluation score
* Section-wise breakdown
* Raw JSON output

---

# 📦 **Project Structure**

```
student-introduction-evaluation-ai/
│
├── app.py                     # Streamlit UI
├── scoring.py                 # Core scoring logic
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
├── sample_transcript.txt      # Sample transcript for testing
├── rubric.xlsx                # Provided rubric file
│
└── assets/ (optional)         # Screenshots for README
```

---

# 📊 **Evaluation Rubric (Summary)**

| Category            | Metric                       | Max Score |
| ------------------- | ---------------------------- | --------- |
| Content & Structure | Salutation / Keywords / Flow | 40        |
| Speech Rate         | WPM                          | 10        |
| Language Quality    | Grammar / Vocabulary         | 20        |
| Clarity             | Filler Word Rate             | 15        |
| Engagement          | Sentiment Positivity         | 15        |
| **TOTAL**           |                              | **100**   |

---

# 🌐 **Deployment**

Your app is deployed live on Streamlit Cloud.

### 🔗 Live App:

```
https://student-introduction-evaluation-ai-ea7qhq6j58jyjeaqewwbpo.streamlit.app/
```

### 🚀 Deployment Steps:

1. Push all files to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Select repo → select `main` branch
4. Set `app.py` as the entry file
5. Deploy

---

# 📄 **License**

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute the project for educational or personal use.

---

# 👩‍💻 **Author**

**Miloni Halkati**
Built as part of the **Nirmaan AI Internship Case Study**.

Feel free to connect for collaboration!

---

