# 个人Scrapy爬虫存档

`Scrapy` `Selenium` `Gerapy`

---

目前写了爬取javbus当日的高清磁力链

### 目录结构

| 目录        | 备注            |
|-----------|---------------|
| javScrapy | 爬取javbus的项目   |
| scrapyd   | docer化scrapyd |

scrapyd 用于爬虫守护进程，建议配合 gerapy 使用。

### 调试命令

``` bash
cd $项目文件夹
scrapy crawl javid  # 开始spider任务
```

### Scrapy常用命令

``` bash
# 开启新项目
scrapy startproject xxx
# 新建新的爬虫任务（模版文件）
scrapy genspider $任务名 $DOMAIN
```
### 部署

``` bash
# 若新开发了爬虫需要重新拉依赖
# cd javScrapy
# pip install pipreqs
# pipreqs .
# mv requirements.txt ../scrapyd
cd scrapyd
docker build -t .
docker compose up -d
```
