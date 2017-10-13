#coding=utf-8 
'''


''' 
from com.python.utils.image import DrawImage
from com.python.utils.mysqldb import MysqlDb

#测试跨module 方法调用
#print DrawImage.drawGig("先测试一下");

'''
python mysql test

#插入数据
for i in range(0,100):
    flag = MysqlDb.insert("INSERT INTO `tb_python_user` VALUES (UUID(), '张三"+str(i)+"', '3', '4');");
    if flag:
        print "插入成功"
    else:
        print "插入失败"
'''

#查询数据
datas = MysqlDb.find("SELECT * FROM tb_python_user")

for data in datas:
    print data[0],data[1],data[2],data[3]

