# Text Analysis

This repository provides a detailed explanation of the methodology used for performing text analysis to derive sentimental opinions, sentiment scores, readability, passive words, personal pronouns, and more. The analysis is designed for financial texts, and it encompasses several key aspects, as outlined below:

## Table of Contents
1. [Sentiment Analysis](#1-sentiment-analysis)
1.1. [Cleaning using Stop Words Lists](#11-cleaning-using-stop-words-lists)
1.2. [Creating a dictionary of Positive and Negative words](#12-creating-a-dictionary-of-positive-and-negative-words)
1.3. [Extracting Derived Variables](#13-extracting-derived-variables)
2. [Analysis of Readability](#2-analysis-of-readability)
3. [Average Number of Words Per Sentence](#3-average-number-of-words-per-sentence)
4. [Complex Word Count](#4-complex-word-count)
5. [Word Count](#5-word-count)
6. [Syllable Count Per Word](#6-syllable-count-per-word)
7. [Personal Pronouns](#7-personal-pronouns)
8. [Average Word Length](#8-average-word-length)

## 1. Sentiment Analysis
Sentimental analysis is the process of determining whether a piece of writing is positive, negative, or neutral, primarily focused on financial texts. The following steps are involved:

### 1.1 Cleaning using Stop Words Lists
Stop Words Lists, located in the "StopWords" folder, are used to clean the text by excluding words found in these lists. This cleaning step prepares the text for sentiment analysis.

### 1.2 Creating a Dictionary of Positive and Negative Words
The Master Dictionary, found in the "MasterDictionary" folder, is utilized to create a dictionary of positive and negative words. Only words not found in the Stop Words Lists are added to this dictionary.

### 1.3 Extracting Derived Variables
The text is tokenized using the nltk tokenize module, and the following variables are calculated:

- **Positive Score:** The score is calculated by assigning a value of +1 for each word found in the Positive Dictionary and then summing up all the values.
- **Negative Score:** This score is calculated by assigning a value of -1 for each word found in the Negative Dictionary and then summing up all the values (multiplied by -1 to make it positive).
- **Polarity Score:** Determines if the text is positive or negative, calculated as `(Positive Score – Negative Score) / ((Positive Score + Negative Score) + 0.000001)`. The range is from -1 to +1.
- **Subjectivity Score:** This score determines if the text is objective or subjective, calculated as `(Positive Score + Negative Score) / (Total Words after cleaning + 0.000001)`. The range is from 0 to +1.

## 2. Analysis of Readability
Readability is calculated using the Gunning Fox index formula:

- **Average Sentence Length:** Calculated as the number of words divided by the number of sentences.
- **Percentage of Complex Words:** Calculated as the number of complex words divided by the number of words.
- **Fog Index:** Calculated as `0.4 * (Average Sentence Length + Percentage of Complex Words)`.

## 3. Average Number of Words Per Sentence
Calculated as the total number of words divided by the total number of sentences.

## 4. Complex Word Count
Complex words are defined as words with more than two syllables.

## 5. Word Count
Total cleaned words present in the text after removing stop words and punctuation.

## 6. Syllable Count Per Word
Counting the number of syllables in each word, including exceptions like words ending with "es" or "ed."

## 7. Personal Pronouns
Using regex to count personal pronouns in the text while excluding country names like "US."

## 8. Average Word Length
Calculated as the sum of the total number of characters in each word divided by the total number of words.

This repository provides comprehensive insights into the text analysis process, making it easier to understand and reproduce the results.
