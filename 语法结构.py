# /if 如果有多个条件
# /定义sed变量记录考试分数
sed=int (input('输入分数：'))
## 如果分数大于且等于90，应该显示优
if sed>= 90:
    print ("优")
elif (sed>= 80) and sed <90:
    print("良")
elif (sed>= 70) and sed <80:
    print('中')
elif (sed >= 60) and sed <70:
    print('差')
else:
    print('不及格')
