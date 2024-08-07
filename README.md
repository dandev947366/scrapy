# Scrapy
 Web Scraping with Scrapy, Python

## Add shell in scrapy.cfg file
>Under *[settings]*, add
>>`shell = ipython`

## Run shell
>start shell 
>>`scrapy shell`
>
>exit shell
>>`exit()` or `CRL D`

>fetch web page
>>`fetch('https://books.toscrape.com/')`
>
>return list of books
>>`response.css('article.product_pod')`
>
>return first book
>>`response.css('article.product_pod').get()`
>
>make books variable
>>`books = response.css('article.product_pod')`
>
>check length
>>`len(books)`

>return 1st book in a variable
>>`book = books[0]`
>
>return title of 1st book
>>`book.css('h3 a::text').get()`
>
>return price of 1st book
>>`book.css('.product_price .price_color::text').get()`
>
>return href attribute 
>>`book.css('h3 a').attrib['href']`
>
>return href for next page
>>`response.css('li.next a ::attr(href)').get()`

>return category from xpath
>>`//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()`
>
>return book description from xpath
>>`response.xpath('//div[@id='product_description']/following-sibling::p/text()`

>return table_rows from url
>>`table_rows = response.css('table tr')`
>
>return 2nd row text
>>`table_rows[1].css('td ::text').get()`

>return star rating
>>`response.css('p.star-rating').attrib['class']`


## Bookspider.py
>add code to **parse** function
>
>run from bookscraper terminal
>>`scrapy crawl bookspider`
>
>run and save data to csv 
>>`scrapy crawl bookspider -O bookdata.csv`
>
>append data to current csv
>>`scrapy crawl bookspider -o bookdata.csv`
>
>run and save data to json file
>>`scrapy crawl bookspider -O bookdata.json`
