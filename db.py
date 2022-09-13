import pymysql


def getConnect():
    conn = pymysql.connect(host='sh-cdb-75vlqi3r.sql.tencentcdb.com', port=63169, user='root', passwd='root1234',
                           db='yc')
    return conn


def savedata(query, date, url, count, excerpt):
    sql = 'insert into zhihu_trending(query, date,url,count,excerpt) values(%s, %s,%s,%s,%s) ' % (
        query, date, url, count, excerpt)
    conn = getConnect()
    curr = conn.cursor()
    curr.execute(sql)
    conn.commit()
