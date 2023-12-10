import pandas as pd
from requests_html import HTMLSession
from news_scraper import NewsScraper
from excel_writer import ExcelWriter

class ContentScraper:
    def __init__(self, filename):
        self.session = HTMLSession()
        self.filename = filename
        self.df = pd.read_excel(filename)
    
    def scrape_content(self, link_column, content_column):
        for i, row in self.df.iterrows():
            link = row[link_column]
            r = self.session.get(link)
            scraped_content = r.html.find("p")
            r.close()
            article_content = []
            for element in scraped_content:
                text = element.text
                if "Subscribe to our daily newsletter" in text or "By providing an email address. I agree to the Terms of Use and acknowledge that I have read the Privacy Policy." in text or "Subscribe to our business news" in text or "We use cookies to ensure you get the best experience on our website." in text or "READ: " in text or "/File photo" in text or "/File Photo" in text or "THIS IMAGE WAS PROVIDED BY A THIRD PARTY" in text or "AP Photo/" in text or "REUTERS/" in text or text == "":
                    pass
                else:
                    article_content.append(text)
            merged_content = "\n".join(article_content)
            self.df.at[i, content_column] = merged_content
    
    def save_to_excel(self):
        self.df.to_excel(self.filename, index=False)
        


