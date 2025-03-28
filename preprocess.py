import pandas as pd
import re

# Load dataset
file_path = "data/speaking_topics.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# 🔄 Function to clean text
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = text.strip()  # Remove extra spaces
    return text

# Apply text cleaning
df["Cleaned_Topics"] = df["Topics"].apply(clean_text)

# Show sample
print("\n✅ Cleaned First 5 Rows:")
print(df[["Topics", "Cleaned_Topics"]].head())

# Save cleaned dataset
df.to_csv("data/cleaned_topics.csv", index=False)
print("\n✅ Cleaned dataset saved successfully!")
