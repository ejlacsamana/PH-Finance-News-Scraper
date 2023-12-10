import pandas as pd
from news_scraper import NewsScraper

class ExcelWriter:
    def __init__(self, data, columns, filename):
        self.data = data
        self.columns = columns
        self.filename = filename

    def write_to_excel(self):
        df = pd.DataFrame(self.data, columns=self.columns)
        df.to_excel(self.filename, index=False)
