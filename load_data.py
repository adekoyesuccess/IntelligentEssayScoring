import os
import pandas as pd

print("🔄 Starting script...")  # Debugging print

# Define the correct file path
file_path = "data/speaking_topics.csv"  # Ensure this path is correct

# Check if the file exists before loading
if os.path.exists(file_path):
    print("✅ File found! Attempting to load dataset...")  # Debugging print
    df = pd.read_csv(file_path, encoding="ISO-8859-1")
    
    # Display the first 5 rows
    print("\n✅ First 5 rows of the dataset:")
    print(df.head())

    # Display dataset info
    print("\n✅ Dataset Information:")
    print(df.info())

    # Show number of rows and columns
    print(f"\n✅ Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
else:
    print("❌ Error: File not found! Check the file path.")

print("🔄 Script finished running.")  # Debugging print
import pandas as pd

# Load dataset
file_path = "data/speaking_topics.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# 🔍 Check the first 5 rows
print("\n✅ First 5 rows of the dataset:")
print(df.head())

# 📊 Check column names
print("\n✅ Column names:")
print(df.columns)

# 🔢 Check dataset shape (rows, columns)
print(f"\n✅ Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# 🧐 Check for missing values
print("\n✅ Missing values in dataset:")
print(df.isnull().sum())

# 📈 Check basic statistics
print("\n✅ Dataset summary statistics:")
print(df.describe())
