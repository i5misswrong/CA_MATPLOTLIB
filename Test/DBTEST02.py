from pymongo import MongoClient
import pprint,datetime

# raudius=['R01','R02','R03']
raudius=[1,2,3]
density=['p01','p02','p03','p04']
case=['case1','case2','case3','case4']

T={'time':100,'surplus':100}
V={'time':100,'v':1}
Q={'time':100,'q':10}
print(raudius[0])
client=MongoClient()
db=client.time01
cur=db.raudius[0].find()
# for c in cur:
#     print(c)
# for p in raudius:
#
#     cur_r_c=db.raudius[0].find()
#     for c in cur_r_c:
#         pprint.pprint(c)