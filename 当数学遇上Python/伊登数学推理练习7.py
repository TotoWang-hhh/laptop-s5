#要求输入
ps=int(input('请输入单次加分 '))#单次加分
ms=int(input('请输入单次减分 '))#单次减分
st=int(input('请输入成功次数 '))#成功次数
ft=int(input('请输入失败次数 '))#失败次数

#计算
score=0
score+=st*ps
score-=ft*ms
print('最终得分为%s'%score)
