# 定义变量  姓名  年龄  身高
name='周俊'
age=27
height=1.75
sex='男'
#输出打印    注意 身高单位是m
print('我的名字是: %s 年龄是:%d 身高是:%f m '% (name,age,height))
#小数默认显示6位，如果想改变指定位数，%.nf   n 需要换成具体的整数数字 如1f 2f 3f 如下：
print('我的名字是:%s 年龄是:%d 性别:%s 身高是:%.2f m'%(name,age,sex,height))
#另一种格式化    用元组（）表示 并且在元组开头加上'f'或者'F'，变量用字典的形式表示出来{ }
#  注意  输出换行 (\n)
print(f'\n我的名字是:{name},\n年龄是:{age},\n身高是:{height}m,\n性别:{sex}')