import pandas as pd
import numpy as np
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Download NLTK resources
nltk.download("stopwords")
from nltk.corpus import stopwords

# Load preprocessed data
df = pd.read_csv("data/cleaned_topics.csv")

# 🔄 Convert topics to numerical representation (TF-IDF)
vectorizer = TfidfVectorizer(stop_words=stopwords.words("english"))
X = vectorizer.fit_transform(df["Cleaned_Topics"])

# 🏷️ Creating dummy labels (since we don’t have scores yet)
y = np.random.randint(1, 6, df.shape[0])  # Assigning random scores between 1 and 5

# 📊 Split dataset for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🤖 Train a simple model (Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# ✅ Evaluate model
accuracy = model.score(X_test, y_test)
print(f"\n✅ Model Training Complete! Accuracy: {accuracy:.2f}")

# Save model and vectorizer
import joblib
joblib.dump(model, "model/essay_scoring_model.pkl")
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")
print("\n✅ Model and Vectorizer saved successfully!")
import os
import joblib

# Ensure the 'model' directory exists
os.makedirs("model", exist_ok=True)

# Save the trained model and vectorizer
joblib.dump(model, "model/essay_scoring_model.pkl")
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")

print("\n✅ Model and Vectorizer saved successfully!")
