# 取款机取钱的过程，密码123456 ，账户余额为2000
pwd = '123456'
money = '2000'
password = input('输入密码：')
if password == pwd:
    print('密码正确，登录成功')
#输入金额
    get_money =int (input('输入取款金额:') )
    if money < 'get_money':
        print('取款成功')
    else:
        print('余额不足')
else:
        print('密码错误，请再次尝试')