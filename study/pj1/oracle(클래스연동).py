import cx_Oracle


def makeDic(cursor):
    coluName = [d[0] for d in cursor.description]

    def createRow(*args):
        return dict(zip(coluName, args))
    return createRow()

# con=cx_Oracle.connect('happy/day@localhost:1521/xe')
# cur=con.cursor()
# print('연결성공')

class DBManager:

    def __init__(self):
        self.con=cx_Oracle.connect('happy/day@localhost:1521/xe')
        self.cur=self.con.cursor()
        print('연결성공')
        # self.cur.rowfactory = makeDic(self.cur)
        # rows = self.cur.fachall()
    def __del__(self):
        print('연결헤제')
        self.con.close()

    def selectAll(self):
        # sql="select * from webtoon order by no"
        sql = "select * from webtoon"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        # self.cur.execute(sql)
        # rows = self.cur.fetchall()
        # for row in rows:
        #     print(row[0],row[1],row[2],row[3])
        for row in rows:
            print(row[0], row[1], row[2], row[3])
            # print(row)
    def selectRating(self,rating):
        sql="select * from webtoon where rating>={}"
        self.cur.execute(sql.format(rating))
        rows = self.cur.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3])
            # print(row)
    def insert(self,title,rating,regdate):
        sql="insert into webtoon values (webtoon_seq.nextval,'{}','{}','{}')"
        self.cur.execute(sql.format(title,rating,regdate))
        self.con.commit()

    def updateRegdate(self,rating,regdate):
        sql = "update webtoon set regdate='{}' where rating >={}"
        self.cur.execute(sql.format(regdate,rating))
        self.con.commit()
    def deleteRating(self,rating):
        sql = "delete from webtoon where rating <={}"
        self.cur.execute(sql.format(rating))
        self.con.commit()



d1=DBManager()
d1.selectAll()
# d1.selectRating(9.95)
# d1.insert("마지막화!","9.95","2020.11.26")
# d1.updateRegdate(9.95,'2020.11.24')
# d1.deleteRating(8)
# d1.selectAll()

#----------------------------------
color = ['red','green','blue']
number = [1,2,3]
fruit = ['apple','banana','orange','melon']
for t in zip(color,fruit):
    print(t)
print("!"*30)
for t in zip(color,number,fruit):
    print(t)