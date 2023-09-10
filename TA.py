import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from textstat import syllable_count, gunning_fog, textstat

nltk.download('punkt')

# Define paths to your StopWords and MasterDictionary folders
stopwords_folder = r"C:\Users\manoj\OneDrive - Zoro\Desktop\Work\BlackCoffer\20211030 Test Assignment\StopWords"
master_dictionary_folder = r"C:\Users\manoj\OneDrive - Zoro\Desktop\Work\BlackCoffer\20211030 Test Assignment\MasterDictionary"

# Function to load stopwords from a given file in the stopwords folder
def load_stopwords(folder, filename):
    with open(os.path.join(folder, filename), "r") as file:
        stopwords = file.read().splitlines()
    return stopwords

# Load specific stopwords files
stop_words_names = load_stopwords(stopwords_folder, "StopWords_Names.txt")
stop_words_geographic = load_stopwords(stopwords_folder, "StopWords_Geographic.txt")
stop_words_generic_long = load_stopwords(stopwords_folder, "StopWords_GenericLong.txt")
stop_words_generic = load_stopwords(stopwords_folder, "StopWords_Generic.txt")
stop_words_dates_numbers = load_stopwords(stopwords_folder, "StopWords_DatesandNumbers.txt")
stop_words_currencies = load_stopwords(stopwords_folder, "StopWords_Currencies.txt")
stop_words_auditor = load_stopwords(stopwords_folder, "StopWords_Auditor.txt")

# Load the positive and negative words from the MasterDictionary folder
def load_sentiment_words(filename):
    with open(os.path.join(master_dictionary_folder, filename), "r") as file:
        sentiment_words = file.read().splitlines()
    return sentiment_words

positive_words = load_sentiment_words("positive-words.txt")
negative_words = load_sentiment_words("negative-words.txt")

# Function to clean text using stopwords
def clean_text(text, stopwords):
    words = word_tokenize(text)
    cleaned_words = [word.lower() for word in words if word.lower() not in stopwords]
    return cleaned_words

# Function to calculate sentimental analysis
def calculate_sentiment_analysis(text, positive_words, negative_words, stopwords):
    cleaned_text = clean_text(text, stopwords)
    positive_score = sum(1 for word in cleaned_text if word in positive_words)
    negative_score = sum(1 for word in cleaned_text if word in negative_words)
    
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(cleaned_text) + 0.000001)
    
    return {
        "Positive Score": positive_score,
        "Negative Score": negative_score,
        "Polarity Score": polarity_score,
        "Subjectivity Score": subjectivity_score
    }

# Function to analyze readability
def analyze_readability(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    average_sentence_length = len(words) / len(sentences)
    complex_word_count = sum(1 for word in words if syllable_count(word) > 2)
    
    fog_index = 0.4 * (average_sentence_length + (complex_word_count / len(words)))
    
    return {
        "Average Sentence Length": average_sentence_length,
        "Percentage of Complex Words": complex_word_count / len(words),
        "Fog Index": fog_index
    }

# Function to count personal pronouns
def count_personal_pronouns(text):
    pronouns = ["i", "we", "my", "ours", "us"]
    words = word_tokenize(text.lower())
    pronoun_count = sum(1 for word in words if word in pronouns)
    return pronoun_count

# Function to calculate average word length
def average_word_length(text):
    words = word_tokenize(text)
    total_word_length = sum(len(word) for word in words)
    avg_word_len = total_word_length / len(words)
    return avg_word_len

# Example text for analysis (you can replace this with your actual text)
text = """
Text analysis is a fascinating field of study in natural language processing. It allows us to gain insights from written or spoken language data. Whether you're analyzing customer reviews, news articles, or social media posts, understanding sentiment and readability is crucial.

Sentimental Analysis:
Sentiment analysis involves evaluating text to determine whether it expresses a positive, negative, or neutral sentiment. In the context of financial texts, this can be particularly useful. Let's consider a hypothetical financial report:

"Company XYZ reported record-breaking profits in the last quarter, leading to a surge in its stock price."

Using sentiment analysis, we can determine that this statement is positive, as it discusses record-breaking profits and a surge in stock price. We can break down the analysis as follows:

- Positive Score: 2 (for "record-breaking" and "surge")
- Negative Score: 0
- Polarity Score: 1.0 (indicating a strongly positive sentiment)
- Subjectivity Score: 0.666667 (indicating some subjectivity)

Readability Analysis:
Readability analysis focuses on assessing the complexity and ease of understanding of a text. Different readability metrics exist, such as the Gunning Fog Index. Let's analyze a sample paragraph:

"Despite its intricate technical details, the whitepaper provides a comprehensive overview of blockchain technology and its potential applications. It discusses concepts like distributed ledgers, consensus algorithms, and smart contracts."

The readability analysis yields the following metrics:

- Average Sentence Length: 23 words per sentence
- Percentage of Complex Words: 42.86% (due to technical terms)
- Fog Index: 10.86 (indicating a moderately complex text)

Personal Pronoun Count:
Personal pronouns like "I," "we," "my," "ours," and "us" can indicate a personal perspective. For instance, consider this passage:

"I believe we should invest in renewable energy for our future. Our company's success depends on it."

In this case, the personal pronoun count would be 5.

Average Word Length:
The average word length is calculated by summing the number of characters in all words and dividing by the total word count. For example, in the sentence "The quick brown fox jumps," the average word length would be (3 + 5 + 5 + 3 + 5) / 5 = 4.2 characters per word.

You can use this extended sample text to replace the placeholder text in the code and perform text analysis on it.
"""


# Perform sentimental analysis
sentiment_analysis_result = calculate_sentiment_analysis(text, positive_words, negative_words, stop_words_generic)

# Perform readability analysis
readability_result = analyze_readability(text)

# Count personal pronouns
pronoun_count = count_personal_pronouns(text)

# Calculate average word length
avg_word_len = average_word_length(text)

# Print results
print("Sentimental Analysis:")
for key, value in sentiment_analysis_result.items():
    print(f"{key}: {value}")

print("\nReadability Analysis:")
for key, value in readability_result.items():
    print(f"{key}: {value}")

print("\nPersonal Pronoun Count:", pronoun_count)
print("\nAverage Word Length:", avg_word_len)
