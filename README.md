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
- [🖼️ Screenshots](#️-screenshots)
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

# 🚀 How to Run

### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
