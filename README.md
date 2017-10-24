# Usage:
```bash
scrapy crawl Kafka -a crawl='y' 
scrapy crawl Parsley -a parselet='parselets/nytimes.yml' 
-a domain='nytimes.com' -a url='http://www.nytimes.com/pages/technology/' -t jl -o -
 > results/nytimes.jl
```
