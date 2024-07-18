import re
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer


def remove_punctuation(text):
    """
    Takes in a text string and returns a string with all the punctuation removed.
    """
    pattern = re.compile(r"[^a-zA-Z0-9 ]")
    cleaned_doc = re.sub(pattern, "", text)
    return cleaned_doc


def normalize_case(text):
    """
    Takes in a text string and returns a string with all characters in lower case.
    """
    return text.lower()


def tokenize_text(text):
    """
    Takes in a text string and returns a list where each item corresponds to a token.
    """
    tokenized_text = word_tokenize(text)
    return tokenized_text


def remove_stopwords(tokenized_text):
    """
    Takes in a list of text, and returns another list where the stop words have been removed.
    """
    text_tokenized_filter = [
        word for word in tokenized_text if word not in stopword_list
    ]
    return text_tokenized_filter


def lemmatize_text(tokenized_text):
    """
    Takes in a list of text, and returns another list where each word has been lemmatized.
    """
    text_lemmatized = [lemmatizer.lemmatize(token) for token in text_tokenized_filter]
    return text_lemmatized


def process_text(text):
    """
    Takes in a raw text document and performs the following steps in order:
    - punctuation removal
    - case normalization
    - tokenization
    - remove stopwords
    - lemmatization

    Then returns a string containing the processed text
    """
    cleaned_text = remove_punctuation(text)
    normalized_text = normalize_case(cleaned_text)
    tokenized_text = tokenize_text(normalized_text)
    text_without_stopwords = remove_stopwords(tokenized_text)
    lemmatized_text = lemmatize_text(text_without_stopwords)
    processed_text = " ".join(lemmatized_text)
    return processed_text
