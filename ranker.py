# import pandas as pd
# import spacy

# filename = r'D:\Documents\Finance News.xlsx'
# interests = ['stock markets', 'effect of global economy to the Philippines', 'one-man business models', 'financial technology', 'philippines']

# df = pd.read_excel(filename)

# nlp = spacy.load('en_core_web_sm')

# def preprocess_text(text):
#     doc = nlp(text)
#     return ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

# df['Processed Content'] = df['Content'].apply(preprocess_text)

# def calculate_relevance(text):
#     doc = nlp(text)
#     return sum(1 for token in doc if token.lemma_ in interests)

# df['Relevance Score'] = df['Processed Content'].apply(calculate_relevance)

# ranked_df = df.sort_values(by='Relevance Score', ascending=False)
# print(ranked_df[['Content', 'Relevance Score']])

import pandas as pd
from transformers import BertTokenizer, BertModel
import torch

filename = r'D:\Documents\Finance News.xlsx'
interests = ['stock markets', 'effect of global economy to the Philippines', 'one-man business models', 'financial technology', 'philippines']

df = pd.read_excel(filename)

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Tokenize and encode your interests
interests_tokens = tokenizer(interests, return_tensors='pt', padding=True, truncation=True)

# Calculate embeddings for interests
with torch.no_grad():
    interests_embeddings = model(**interests_tokens).last_hidden_state.mean(dim=1)

def calculate_relevance_bert(text):
    text_tokens = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        text_embedding = model(**text_tokens).last_hidden_state.mean(dim=1)

    # Calculate cosine similarity between interests and text
    similarity = torch.nn.functional.cosine_similarity(interests_embeddings, text_embedding).mean().item()
    
    return similarity

df['Relevance Score BERT'] = df['Content'].apply(calculate_relevance_bert)
df = df.sort_values(by='Relevance Score BERT', ascending=False).reset_index(drop=True)
df['Rank'] = df['Relevance Score BERT'].rank(ascending=False)
df.to_excel(filename, index=False)