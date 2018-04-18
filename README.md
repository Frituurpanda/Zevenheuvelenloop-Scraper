# Zevenheuvelenloop Uitslag Scraper
Automated scraper build with <a href="https://scrapy.org/" alt="Scrapy">Scrapy</a> that scrapes data from the running event Zevenheuvelenloop. The data gets scraped from <a href="http://evenementen.uitslagen.nl/2016/zevenheuvelenloop/" alt="evenementen-uitslagen">http://evenementen.uitslagen.nl/</a>.

<br>The scraper process works as follows: <br>
<ul>
  <li> The allowed domain gets set to <a href="http://evenementen.uitslagen.nl">evenementen.uitslagen.nl</a> </li>
  <li> The max_id value should be changed to the maximum amount of pages that you want to have scraped.</li>
  <li> An example of the final url can be <a href="http://evenementen.uitslagen.nl/2016/zevenheuvelenloop/uitslag01233.html">~uitslag01233.html"</li>
  <li> The scraper will scrape the set amount of pages and add  those to the csv file until done. </li>
</ul>

#### Example with Airbnb's Superset
<img src="img/Example1.png" alt="Example1">

### Why???
After competing in the event myself I wanted to have some answers based on the data that resulted from the competition. This included questions like:
<ul>
  <li> What was the average finish time of a certain category.</li>
  <li> How much people did a person overtake in his own category.</li>
  <li> How much people did a person overtake given all categories</li>
  <li> Etc etc..</li>
</ul>


### How to use
You can use the scraper by using the command
```bash
scrapy runspider ZevenHeuvelSpider_spider.py -o zevenheuvel.csv
```
After completion, you can open the zevenheuvel.csv for inspection.

### Resources Used
- <a href="https://scrapy.org/" alt="scrapy">Scrapy</a>
- <a href="https://github.com/airbnb/superset" alt="SuperSet">Airbnb's SuperSet</a>
- <a href="http://evenementen.uitslagen.nl/2016/zevenheuvelenloop/" alt="evenementen.uitslagen.nl">evenementen.uitslagen.nl</a>
