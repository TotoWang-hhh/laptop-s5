import requests
import random
import json

def get_acc_token():
    dic={'grant_type':'client_credentials','client_id':'OgyQl5Pc3zN9kFGs4UHqrnxf','client_secret':'cEh2zkvbPuxi4me5jj068VaRGg00Vf06'}
    res=requests.post("https://aip.baidubce.com/oauth/2.0/token",data=dic)
    print(res)
    req=res.json()
    acc_token=req['access_token']
    return acc_token

def chat(word):
    dic={
         'log_id':str(random.random()),
         'request':{
                    'query':word,
                    'user_id':str(random.randint(0,16384))
                   },
         'session_id':'',
         'service_id':'S31885',
         'version':'2.0'}
    res=requests.post("https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token="+get_acc_token(),json=dic)
    print(res)
    req=json.loads(res.content)
    print(req)
    unit_chat_obj_result = req["result"]
    print("unit_chat_obj_result",req)
    unit_chat_response_list = unit_chat_obj_result["response_list"]
    print("unit_chat_response_list",unit_chat_response_list)
    # 随机选取一个"意图置信度"[+response_list[].schema.intent_confidence]不为0的技能作为回答
    unit_chat_response_obj = random.choice(
       [unit_chat_response for unit_chat_response in unit_chat_response_list if
        unit_chat_response["schema"]["intent_confidence"] > 0.0])
    unit_chat_response_action_list = unit_chat_response_obj["action_list"]
    unit_chat_response_action_obj = random.choice(unit_chat_response_action_list)
    unit_chat_response_say = unit_chat_response_action_obj["say"]
    return unit_chat_response_say

print(get_acc_token())
print(chat(input('输入要说的话 ')))
