# scrapy
 Web Scraping with Scrapy, Python

## Add shell in scrapy.cfg file
Under [settings], add
shell = ipython

## Run shell
scrapy shell

>fetch web page
`fetch('https://books.toscrape.com/')`

>return list of books
`response.css('article.product_pod')`

>return first book
`response.css('article.product_pod').get()`

>make books variable
`books = response.css('article.product_pod')`