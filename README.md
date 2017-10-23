# Usage:
```bash
scrapy crawl Parsley -a parselet='parselets/nytimes.yml' -a domain='nytimes.com' -a url='http://www.nytimes.com/pages/technology/' -t json -o - > results/nytimes.json
# -a domain='www.coolblue.nl'
```
