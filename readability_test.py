import textstat

# Sample essay (replace with your actual third essay)
essay = """Technology has changed the way people live in many ways. It has made communication faster, work more efficient, and learning more accessible. For example, the internet allows people to connect with others worldwide instantly."""

# Check Readability Score
readability_score = textstat.flesch_reading_ease(essay)
print("Readability Score:", readability_score)

# Debug readability calculation
print("Number of Sentences:", textstat.sentence_count(essay))
print("Number of Words:", textstat.lexicon_count(essay, removepunct=True))
print("Number of Syllables:", textstat.syllable_count(essay))
