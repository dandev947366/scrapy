# Scrapy
 Web Scraping with Scrapy, Python

## Add shell in scrapy.cfg file
Under *[settings]*, add
`shell = ipython`

## Run shell
>start shell 
`scrapy shell`

>fetch web page
`fetch('https://books.toscrape.com/')`

>return list of books
`response.css('article.product_pod')`

>return first book
`response.css('article.product_pod').get()`

>make books variable
`books = response.css('article.product_pod')`

>check length
`len(books)`

>return 1st book in a variable
`book = books[0]`

>return title of 1st book
`book.css('h3 a::text').get()`

>return price of 1st book
`book.css('.product_price .price_color::text').get()`

>return href attribute 
`book.css('h3 a').attrib['href']`

>return href for next page
`response.css('li.next a ::attr(href)').get()`

>return *text* from xpath
`response.xpath('/html/body/div[1]/div/ul/li[3]/a/*text()*').get()`

>return book description from xpath
`response.xpath('//*[@id="content_inner"]/article/p/*text()*').get()`

>return table_rows from url
`table_rows = response.css('table tr')`

>return 2nd row text
`table_rows[1].css('td ::text').get()`

>return star rating
`response.css('p.star-rating').attrib['class']`

>exit shell
`exit()` or `CRL D`

## Bookspider.py
>add code to **parse** function

>run from bookscraper terminal
`scrapy crawl bookspider`