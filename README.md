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



⚠️ **IMPORTANT**  
Outer ```text aur inner ```text dono rehna chahiye — warna GitHub formatting toot jayega.

---

## 🧠 PKL FILES EXPLANATION (VERY IMPORTANT)

README me ye section **zaroor add karo** 👇

```md
## 🧠 Model Files

- **model.pkl**  
  Trained Machine Learning model (Multinomial Naive Bayes)

- **vectorizer.pkl**  
  TF-IDF vectorizer used to transform email text into numerical features

These files are loaded directly in `app.py` for prediction without retraining.

▶️ How App Works (Simple Flow)
## ⚙️ How It Works

1. User uploads or enters email content
2. Text is transformed using `vectorizer.pkl`
3. Transformed data is passed to `model.pkl`
4. Model predicts:
   - 🚨 Spam
   - ✅ Legitimate
5. Result displayed on web interface

▶️ Run Instructions (Your Structure ke hisab se)
## 🚀 Run the Application

```bash
pip install -r requirements.txt
cd spam_detector
python app.py


Open browser:

http://127.0.0.1:5000
