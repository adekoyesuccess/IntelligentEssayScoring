import joblib
import os
import numpy as np

# Ensure the model directory exists
model_path = "model/essay_scoring_model.pkl"
vectorizer_path = "model/tfidf_vectorizer.pkl"

# Check if the model and vectorizer exist
if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    print("❌ Error: Model or vectorizer not found! Train the model first.")
    exit()

# Load the trained model and vectorizer
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Function to predict the score of an essay
def predict_score(essay):
    essay_vectorized = vectorizer.transform([essay])  # Convert text to numerical representation
    predicted_score = model.predict(essay_vectorized)
    return predicted_score[0]

# Sample essay for testing
sample_essay = "Technology has greatly influenced education by providing students with access to more resources and learning tools."
predicted_score = predict_score(sample_essay)

print(f"\n📝 Sample Essay: {sample_essay}")
print(f"📊 Predicted Score: {predicted_score}")
