num=int(input('请输入日期的和 '))
days=int(input('请输入外出的天数 '))
time=1#尝试次数（外出日期）
getAns=False#获得答案
temp=0#天数和

while not getAns:
    for i in range(1,days+1):
        temp+=i+time
        print('调试信息：temp=%s'%temp)
    if time==num:
        getAns=True
        print('答案为'+str(time))
        break
    else:
        time+=1
        print('尝试'+str(time))
    temp=0
