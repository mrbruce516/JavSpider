import logging
from datetime import date
from .database import DBConnection

def write_magnet():
    db = DBConnection(host='localhost')
    # 写入待aria2下载的txt文件
    magnet_sql = "SELECT magnet FROM javscrapy WHERE status = 0"
    magnet = db.execute(magnet_sql)
    update_sql = "UPDATE javscrapy SET status = 1 WHERE magnet = %s"
    with open(str(date.today()) + ".magnet.txt", "a") as file:
        if not magnet:
            logging.info("今日养生，无新增种子")
        else:
            for link in magnet:
                file.write(link['magnet'] + '\n')
                # TODO 之后写到单独的aira下载完成校验的程序中
                db.execute(update_sql, link['magnet'])
            logging.info("今日抓取到" + str(len(magnet)) + "个种子")
    db.disconnect()
