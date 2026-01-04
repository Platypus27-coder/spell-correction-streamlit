# Spell Correction with Levenshtein Distance (Streamlit)

This project is a simple **spell correction application** built using  
**Levenshtein Distance (Edit Distance)** and **Streamlit**.

The app takes a user-input word and suggests the most similar correct word
from a given vocabulary file.

---

## 🚀 Features

- Compute **Levenshtein distance** using Dynamic Programming
- Suggest the **closest matching word**
- Simple and interactive **Streamlit web interface**
- Lightweight and easy to extend

---

## 🧠 Algorithm

The core algorithm used in this project is **Levenshtein Distance**, which
measures the minimum number of operations required to transform one string
into another.

Allowed operations:
- Insert
- Delete
- Replace

Time Complexity: **O(m × n)**  
where `m` and `n` are the lengths of the two words.

---
## P/S: You can find this problem in LeetCode (Edit Distance)
## 📁 Project Structure

---

## ⚙️ Installation
```
spell-correction-streamlit/
│
├── app.py # Main Streamlit application
├── vocab.txt # Vocabulary file (one word per line)
├── README.md # Project documentation
### 1️⃣ Clone the repository

```
Run the Application:
  streamlit run levenshtein_distance.py

