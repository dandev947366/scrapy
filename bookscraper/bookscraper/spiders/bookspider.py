import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        base_url = 'https://books.toscrape.com/'
        books = response.css('article.product_pod')
        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()
            if 'catalogue/' in relative_url:
                book_url = base_url + relative_url
            else :
                book_url = base_url + 'catalogue/' + relative_url
            yield response.follow(book_url, callback=self.parse_book_page)
            
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = base_url + next_page
            else :
                next_page_url = base_url + 'catalogue/' + next_page
            yield response.follow(next_page_url, callback=self.parse)
    
    def parse_book_page(self, response):
        pass
        
  