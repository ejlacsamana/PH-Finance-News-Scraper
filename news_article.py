class NewsArticle:
    def __init__(self, title, link, date_published):
        self.title = title
        self.link = link
        self.date_published = date_published

    def __str__(self):
        return f"Title: {self.title}\nLink: {self.link}\nDate Published: {self.date_published}\n"