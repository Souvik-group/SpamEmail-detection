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
SPAM_EMAIL/
│
├── archive/
│
├── spam_detector/
│   ├── static/
│   ├── templates/
│   ├── uploads/
│   ├── app.py              # Flask main application
│   ├── model.pkl           # Trained ML model
│   ├── vectorizer.pkl      # TF-IDF vectorizer
│   ├── save_model.py       # Save trained model
│   ├── train_model.py      # Train model script
│   ├── train_new.py        # Retraining / experimentation
│   ├── sample_emails.csv   # Sample input emails
│   ├── sample_spam.eml     # Example spam email
│   ├── sample_legitimate.eml # Example legitimate email
│
├── spam.csv                # Dataset
├── Untitled1.ipynb         # Model experimentation notebook
├── requirements.txt        # Project dependencies
└── README.md

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


