# Usage:
```bash
scrapy crawl Parsley -o results/nytimes.jl -a parselet="`cat parselets/nytimes.yml`" -a item_key='items' -a domain='nytimes.com' -a url='http://www.nytimes.com/pages/technology/'
# -a domain='www.coolblue.nl'
```
