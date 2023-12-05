import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import pandas as pd

nltk.download('punkt')

def summarize(news_article):
    content = news_article
    num_sentences = 3
    parser = PlaintextParser.from_string(content, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    summary_strings = [str(sentence) for sentence in summary]
    combined_text = ' '.join(summary_strings)
    return combined_text

filename = r"D:\Documents\Finance News.xlsx"
df = pd.read_excel(filename)

for i, row in df.iterrows():
    news_article = row[3]
    summary = summarize(news_article)
    df.at[i, 'Summary'] = summary

df.to_excel(filename, index=False)