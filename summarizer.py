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





# nltk.download('punkt')

# def summarize(news_article):
#     content = news_article
#     num_sentences = 3
#     parser = PlaintextParser.from_string(content, Tokenizer("english"))
#     summarizer = LsaSummarizer()
#     summary = summarizer(parser.document, num_sentences)
#     summary_strings = [str(sentence) for sentence in summary]
#     combined_text = ' '.join(summary_strings)
#     return combined_text

# filename = r"D:\Documents\Finance News.xlsx"
# df = pd.read_excel(filename)

# for i, row in df.iterrows():
#     news_article = row[3]
#     summary = summarize(news_article)
#     df.at[i, 'Summary'] = summary

# df.to_excel(filename, index=False)