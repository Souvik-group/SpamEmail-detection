import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

# Sample data
sample_data = {
    'message': [
        'Free money! Click here now!',
        'Hello, how are you today?',
        'URGENT: You have won $1000000!',
        'Meeting scheduled for tomorrow at 3pm',
        'Limited time offer! Buy now!',
        'Thanks for your help yesterday',
        'Congratulations winner! Claim prize now!',
        'Can we reschedule our meeting?',
        'Act fast! Limited offer expires soon!',
        'Hope you are doing well'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(sample_data)

X = df['message']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

vectorizer = TfidfVectorizer(
    stop_words='english',
    max_df=0.95,
    min_df=1,
    lowercase=True
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved successfully!")