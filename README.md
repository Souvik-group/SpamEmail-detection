# 📧 Spam Mail Detection Web App

A machine learning based web application that detects whether an email/message is **Spam** or **Legitimate (Ham)** using **TF-IDF + Multinomial Naive Bayes**, deployed with **Flask**.

---

## 🧠 Tech Stack
- Python
- Pandas
- Scikit-learn
- Flask
- HTML, CSS

---

## 📂 Project Structure

```text
spam-mail-detected/
│
├── spam_detector/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css
│
├── notebook/
│   └── spam_training.ipynb
│
├── dataset/
│   └── spam.csv
│
├── requi

⚙️ Installation & Run

1️⃣ Clone repository

git clone https://github.com/Souvik-group/spam-mail-detected.git
cd spam-mail-detected


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Run Flask app

cd spam_detector
python app.py


4️⃣ Open browser

http://127.0.0.1:5000

🧪 Example

Input:

Congratulations! You have won a free lottery.


Output:

🚨 Spam Email

