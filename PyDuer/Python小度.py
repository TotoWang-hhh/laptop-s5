import requests
import random
import datetime

helpword='''
Python小度 帮助
本地帮助
$help 获取帮助
$quit 退出
$get_acc_token 获取access token
$test 测试网络连接
'''

def localCommand(word):
    if word=='$help':
        print(helpword)
    elif word=='$quit':
        exit()
    elif word=='$get_acc_token':
        print(get_acc_token())
    elif word=='$test':
        print(requests.get("https://www.baidu.com"))

def get_acc_token():
    dic={'grant_type':'client_credentials','client_id':'OgyQl5Pc3zN9kFGs4UHqrnxf','client_secret':'cEh2zkvbPuxi4me5jj068VaRGg00Vf06'}
    res=requests.post("https://aip.baidubce.com/oauth/2.0/token",data=dic)
    req=res.json()
    acc_token=req['access_token']
    return acc_token

def chat(word):
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
    res=requests.post("https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token="+get_acc_token(),json=dic)
    req=res.json()
    unit_chat_obj_result = req["result"]
    unit_chat_response_list = unit_chat_obj_result["response_list"]
    # 随机选取一个"意图置信度"[+response_list[].schema.intent_confidence]不为0的技能作为回答
    unit_chat_response_obj = unit_chat_response_list[0]
    unit_chat_response_action_list = unit_chat_response_obj["action_list"]
    unit_chat_response_action_obj = random.choice(unit_chat_response_action_list)
    unit_chat_response_say = unit_chat_response_action_obj["say"]
    return unit_chat_response_say

print(get_acc_token())
print('2020 By 人工智障')
print('调用本地功能请在关键词前面输入$，更多帮助请输入$help')
print('==================================================')

while True:
    curr_time=datetime.datetime.now()
    print('我 '+datetime.datetime.strftime(curr_time,'%Y-%m-%d %H:%M:%S'))
    word=input('')
    print('')
    localCommand(word)
    curr_time=datetime.datetime.now()
    print('小度 '+datetime.datetime.strftime(curr_time,'%Y-%m-%d %H:%M:%S'))
    print(chat(word))
    print('')
