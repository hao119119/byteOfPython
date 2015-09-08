import MySQLdb
import random
import time


try:
    conn = MySQLdb.connect(host='localhost', user='root',
                           passwd='hao119119', db='iop_dev', port=3306)
    cur = conn.cursor()


    # resource loop
    id = 1
    for i in range(1, 1000):
        # meter loop
        for j in range(1, 20):
            values = []
            for k in range(1, 200):
                id += 1
                values.append((id, i, j, time.strftime('%Y-%m-%d %H:%M:%S'), random.random(),  'env1'))
            cur.executemany('insert into mon_statistic_day values(%s,%s,%s,%s,%s,%s)', values)
            conn.commit()

    cur.close()
    conn.close()

except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
