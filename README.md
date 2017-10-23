# Usage:
```bash
scrapy crawl NYTimes -o results/nytimes.jl -a item_key='newsitems' -a parselet="`cat parselets/nytimes__technology.let.yml`"
```
