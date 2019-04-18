#1、网站用户的上线次数统计（活跃用户）
#2、按天统计网站活跃用户
import  redis

db=redis.Redis('192.168.1.113',port=6379,db=1)
#user01
db.setbit("user01",1,1)
db.setbit("user01",30,1)

#user02
db.setbit("user02",2,1)
db.setbit("user02",300,1)

for i in range(3,365,3):
    db.setbit('u001',i,1)

for i in range(4,365,2):
    db.setbit('u002',i,1)

userlist=db.keys("u*")
print(userlist)
Au=[]#活跃用户
nau=[]#不活跃用户
for u in userlist:
    print(db.bitcount(u),u)
    count=db.bitcount(u)
    if count >=100:
        Au.append((u,count))
    else:
        nau.append((u,count))

for i in Au:
    print(str(i[0])+" is alive user"+str(i[1]))

for i in nau:
    print(str(i[0]) + " is not alive user" + str(i[1]))

#
# #2、按天统计网站活跃用户
# 天作为key，用户ID为offset，上线置为1
# 求一段时间内活跃用户数
# SETBIT 20160602 15 1
# SETBIT 20160601 123 1
# SETBIT 20160606 123 1
# 求6月1日到6月10日的活跃用户
# BITOP OR 20160601-10 20160601 20160602 20160603 20160610
# BITCOUNT 20160601-10
# 结果为2