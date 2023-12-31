import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import pandas as pd

class Summarizer:
    def download_nltk(self):
        nltk.download("punkt")

    def __init__(self, filename, nltk_download=False):
        self.filename = filename
        self.df = pd.read_excel(self.filename)
        self.summarizer = LsaSummarizer()

        if nltk_download:
            self.download_nltk()

    def summarize_article(self, summary_column, content_column, num_sentences):
        for i, row in self.df.iterrows():
            news_article = row[content_column]
            parser = PlaintextParser.from_string(news_article, Tokenizer("english"))
            summary = self.summarizer(parser.document, num_sentences)
            summary_strings = [str(sentence) for sentence in summary]
            combined_text = " ".join(summary_strings)
            self.df.at[i, summary_column] = combined_text

    def write_to_excel(self):
        self.df.to_excel(self.filename, index=False)
