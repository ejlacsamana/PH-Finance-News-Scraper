import pandas as pd
from transformers import BertTokenizer, BertModel
import torch
class Ranker():
    def __init__(self, filename, interests):
        self.filename = filename
        self.df = pd.read_excel(filename)
        self.interests = interests
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')
        
    def calculate_relevance_bert(self, text):
        interests_tokens = self.tokenizer(self.interests, return_tensors = 'pt', padding = True, truncation = True)
        text_tokens = self.tokenizer(text, return_tensors = 'pt', padding = True, truncation = True)
        with torch.no_grad():
            interests_embeddings = self.model(**interests_tokens).last_hidden_state.mean(dim = 1)
            text_embedding = self.model(**text_tokens).last_hidden_state.mean(dim = 1)
        similarity = torch.nn.functional.cosine_similarity(interests_embeddings, text_embedding).mean().item()
        return similarity
    
    def save_to_excel(self):
        self.df['Relevance Score BERT'] = self.df['Content'].apply(self.calculate_relevance_bert)
        self.df = self.df.sort_values(by='Relevance Score BERT', ascending=False).reset_index(drop=True)
        self.df['Rank'] = self.df['Relevance Score BERT'].rank(ascending=False)
        self.df.to_excel(self.filename, index=False)

