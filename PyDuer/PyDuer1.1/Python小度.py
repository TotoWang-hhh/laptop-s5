import requests
import random
import datetime
import time
from os.path import isfile
import linecache

print('环境正在初始化')

if not isfile("./data/acc_token.dat"):
    fd=open("./data/acc_token.dat",mode='w',encoding='utf-8')
    fd.write('null\n')
    fd.write('0\n')
    fd.write('0')
    fd.close()

class Acc_token():
    def __init__(self):
        self.acc_token='null'
        self.file="./data/acc_token.dat"
    def get(self):
        with open(self.file,'r') as file:
            print(file.read())
        get_time=linecache.getline(self.file,2).strip()
        available_time=linecache.getline(self.file,3).strip()
        print(int(time.time()))
        print(int(get_time))
        print(type(available_time))
        print(available_time)
        print(int(available_time))
        if isfile(self.file) and int(time.time())-int(get_time)<=int(available_time):
            self.acc_token=linecache.getline(self.file,1).strip()
        else:
            self.acc_token=self.fresh()
    def fresh(self):
        dic={'grant_type':'client_credentials','client_id':'OgyQl5Pc3zN9kFGs4UHqrnxf','client_secret':'cEh2zkvbPuxi4me5jj068VaRGg00Vf06'}
        res=requests.post("https://aip.baidubce.com/oauth/2.0/token",data=dic)
        req=res.json()
        acc_token=req['access_token']
        with open(self.file,'w+',encoding='utf-8') as file:
            file.write(acc_token+'\n')
            file.write(str(int(time.time()))+'\n')
            file.write(str(req['expires_in']))
        f=open(self.file,'r',encoding='utf-8')
        print(f.read())
        f.close()
        self.acc_token=acc_token

acc_token=Acc_token()

def chat(word):
    acc_token.get()
    skill_ids=['1036063','1036064','1036060','1036062','1036059','1036061']
    dic={
         'log_id':str(random.random()),
         'request':{
                    'query':word,
                    'user_id':str(random.randint(0,16384))
                   },
         'session':'',
         'skill_ids':skill_ids,
         'service_id':'S31885',
         'version':'2.0'}
    res=requests.post("https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token="+acc_token.acc_token,json=dic)
    req=res.json()
    unit_chat_obj_result = req["result"]
    unit_chat_response_list = unit_chat_obj_result["response_list"]
    # 随机选取一个"意图置信度"[+response_list[].schema.intent_confidence]不为0的技能作为回答
    unit_chat_response_obj = random.choice(
       [unit_chat_response for unit_chat_response in unit_chat_response_list if
        unit_chat_response["schema"]["intent_confidence"] > 0.0])
    unit_chat_response_action_list = unit_chat_response_obj["action_list"]
    unit_chat_response_action_obj = random.choice(unit_chat_response_action_list)
    unit_chat_response_say = unit_chat_response_action_obj["say"]
    return unit_chat_response_say

print(acc_token.get())
print('==================================================')

while True:
    curr_time=datetime.datetime.now()
    print('我 '+datetime.datetime.strftime(curr_time,'%Y-%m-%d %H:%M:%S'))
    word=input('')
    print('')
    curr_time=datetime.datetime.now()
    print('小度 '+datetime.datetime.strftime(curr_time,'%Y-%m-%d %H:%M:%S'))
    print(chat(word))
    print('')



