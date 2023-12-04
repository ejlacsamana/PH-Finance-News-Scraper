from requests_html import HTMLSession
session = HTMLSession()

url = 'https://business.inquirer.net/category/latest-stories'
news_list = []

for i in range(2, 5):
    r = session.get(url)
    articles = r.html.find('#ch-ls-head')

    for item in articles:
        news_item = item.find('h2', first=True)
        news_date = item.find('#ch-postdate', first=True)
        result = news_date.text.split('BY:\xa0 ')
        news_article = {
        'title': news_item.text,
        'link': news_item.absolute_links,
        'date': result[0]
        }
        news_list.append(news_article)
    url = f'https://business.inquirer.net/category/latest-stories/page/{i}'