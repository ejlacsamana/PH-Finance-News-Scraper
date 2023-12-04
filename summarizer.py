import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

nltk.download('punkt')

news_article = """News article here"""
num_sentences = 3
parser = PlaintextParser.from_string(news_article, Tokenizer("english"))
summarizer = LsaSummarizer()
summary = summarizer(parser.document, num_sentences)

# Print the summary
for sentence in summary:
    print(sentence)