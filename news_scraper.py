from requests_html import HTMLSession
from news_article import NewsArticle

class NewsScraper:
    def __init__(self, base_url, start_page, end_page):
        self.base_url = base_url
        self.start_page = start_page
        self.end_page = end_page
        self.session = HTMLSession()

    def scrape_articles(self):
        news_list = []

        for i in range(self.start_page, self.end_page + 1):
            url = f"{self.base_url}/page/{i}"
            r = self.session.get(url)
            articles = r.html.find("#ch-ls-head")

            for item in articles:
                news_item = item.find("h2", first=True)
                news_date = item.find("#ch-postdate", first=True)
                result = news_date.text.split("BY:\xa0 ")
                news_article = NewsArticle(
                    title = news_item.text,
                    link = list(news_item.absolute_links).pop(),
                    date_published= result[0]
                )
                news_list.append(news_article)
        
        return news_list