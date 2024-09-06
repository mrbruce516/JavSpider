# JavSpider - 爬取Javbus磁力链

`Scrapy` `Selenium` `Gerapy`

---

chrome为依赖，若本地无chrome，Selenium无法正常抓取ajax内容。

### TODO
1. 废弃scrapyd，直接通过系统cron调度docker。
2. aria2下载完成后回调数据库，修改下载状态。

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

若使用容器部署，需要在scrapyd目录中使用middleware.py替换项目文件中的对应文件。
