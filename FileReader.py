import json
import os

import pymysql

path = "E:/war"
conn = pymysql.connect(host='sh-cdb-75vlqi3r.sql.tencentcdb.com', port=63169, user='root', passwd='root1234', db='yc')
cur = conn.cursor()
for filename in os.listdir(path):
    file = open(path + '/' + filename, mode='r', encoding='UTF-8')
    filecontent = file.read()
    jsonObject = json.loads(filecontent)
    for obj in jsonObject:
        querystr = "'" + obj['query'] + "'"
        datestr = "'" + filename.replace(".json", "").replace("-", "") + "'"
        url = "'http://www.zhihu.com/search?q=" + obj['query'] + "'"
        sql = 'insert into zhihu_trending(query, date,url) values(%s, %s,%s) ' % (querystr, datestr, url)
        cur.execute(sql)
    conn.commit()
