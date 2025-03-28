<<<<<<< HEAD
import streamlit as st
import joblib
import textstat
import language_tool_python
from sklearn.feature_extraction.text import TfidfVectorizer

# Load trained model and vectorizer
model = joblib.load("model/essay_scoring_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# Initialize LanguageTool for grammar checking
tool = language_tool_python.LanguageTool("en-US")

# Streamlit App UI
st.title("📝 Intelligent Essay Scoring System")
st.write("Enter your essay below, and the model will predict its score along with writing feedback.")

# Text area for user input
essay = st.text_area("Write or paste your essay here:", height=200)

# Button to trigger scoring
if st.button("Score Essay"):                
    if essay.strip() == "":
        st.warning("Please enter an essay before submitting!")
    else:
        # Preprocess and vectorize input essay
        essay_vector = vectorizer.transform([essay])
        
        # Predict score
        predicted_score = model.predict(essay_vector)[0]

        # Grammar & Readability Analysis
        grammar_errors = tool.check(essay)
        num_errors = len(grammar_errors)

        # Count key readability factors
        num_sentences = textstat.sentence_count(essay)
        num_words = textstat.lexicon_count(essay, removepunct=True)
        num_syllables = textstat.syllable_count(essay)

        # Calculate readability score
        readability_score = textstat.flesch_reading_ease(essay)

        # Debugging logs
        print(f"Essay: {essay}")
        print(f"Readability Score: {readability_score}")
        print(f"Sentences: {num_sentences}, Words: {num_words}, Syllables: {num_syllables}")

        # Display Results
        st.success(f"📊 **Predicted Score: {predicted_score}**")
        st.write(f"📝 **Grammar Issues Detected:** {num_errors}")
        st.write(f"📖 **Readability Score:** {readability_score} (Higher is better)")

        # Suggest improvements
        if num_errors > 0:
            st.subheader("🔍 Suggested Grammar Improvements:")
            for error in grammar_errors[:5]:  # Show top 5 errors
                st.write(f"🔹 {error}")

        # Readability Feedback
        if readability_score < 50:
            st.warning("⚠️ Your essay is difficult to read. Try using shorter sentences and simpler words.")

        st.write("✅ **Tip:** Improve coherence by using transition words and structuring your ideas clearly.")
