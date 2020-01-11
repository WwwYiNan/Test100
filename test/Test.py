def add(num1, num2):
    return num1 + num2

    # def SaySome(name="王逸楠", words="改变世界"):
    print(name + "-->" + words)


# print(SaySome(words="王逸楠", name="改变世界"))
def test(*params, exp):
    print('参数的长度是：', len(params), exp);
    print('第二个参数是；', params[1]);


# print(test(1, '王逸楠', 3.14, 5, 6, 7,  exp='wang'))

def back():
    return 1, 3.14, 'Www'


# return [1, 3.14, 'Www']


# print(back())

'''
def discount(price, rate):
    final_price = price * rate
    # print('这里试图访问全局变量old_price的值',old_price)
    old_price = 50
    print('修改后old_price的值是1：', old_price)
    return final_price


old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discount(old_price, rate)
print('修改后old_price的值是2：', old_price)
print('打折后的价格是：', new_price)
# print('这里试图打印局部变量final_price的值：',final_price)  #报错——final_price——没有定义
'''  # 全局变量与局部变量

