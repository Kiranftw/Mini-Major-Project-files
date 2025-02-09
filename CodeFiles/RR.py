from functools import wraps
from docx import Document
from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RelvanceScore(object):
    def __init__(self) -> None:
        self.punctuations = string.punctuation + string.digits + '’' + '“' + '”'
        self.Lemmatizer = WordNetLemmatizer()
        self.stopwords = set(stopwords.words('english'))
        self.Vectorizer = TfidfVectorizer()

    @staticmethod
    def Exception(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (Exception, FileNotFoundError, ValueError, NameError, TypeError) as e:
                return e
        return wrapper
    
    @Exception
    def document_parser(self, document) -> str:
        if document.endswith('.docx'):
            self.doc = Document(document)
            text: str = ''
            for para in self.doc.paragraphs:
                text += para.text
            return text
        elif document.endswith('.pdf'):
            self.PDF = PdfReader(document)
            text = ''
            for page in range(len(self.PDF.pages)):
                text += self.PDF.pages[page].extract_text()
            return text
        elif document.endswith('.txt'):
            with open(document, "r", encoding="utf-8") as file:
                text = file.read()
            return text
        else:
            return 'Invalid File Format'
    @Exception
    def data_preprocessing(self, document: str):
        for token in word_tokenize(document):
            if token not in self.stopwords and token not in self.punctuations and len(token) > 1:
                sub_tokens = re.split(r'[_/\\\-\|]', token)
                for sub_token in sub_tokens:
                    if sub_token not in self.stopwords and len(sub_token) > 1:
                        yield self.Lemmatizer.lemmatize(sub_token.lower())

    @Exception
    def get_score(self, RESUME: list, JD: list):
        # Combine tokens into strings
        CORPUS = [' '.join(RESUME), ' '.join(JD)]
        TFIDF_MATRIX = self.Vectorizer.fit_transform(CORPUS)
        SIMILARITY = cosine_similarity(TFIDF_MATRIX[0], TFIDF_MATRIX[1])
        return round(abs(SIMILARITY[0][0] * 100),2)

    def main(self) -> Exception:
        RESUME = R"C:\Users\uday3\OneDrive\Documents\MAJOR PROJECT\ResumePDF.pdf"
        JD = R"C:\Users\uday3\OneDrive\Documents\MAJOR PROJECT\JD.txt"
        RESUME = self.document_parser(RESUME)
        JD = self.document_parser(JD)
        RESUME = list(self.data_preprocessing(RESUME))
        JD = list(self.data_preprocessing(JD))
        return self.get_score(RESUME, JD)

if __name__ == "__main__":
    obj = RelvanceScore()
    score = obj.main()
    print(score)
