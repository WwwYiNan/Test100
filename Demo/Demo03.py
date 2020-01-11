# 温度转换程序 摄氏度 华氏度 相互转换
tempstr = input('请输入带有符号的温度>>>>:')

if tempstr[-1] in ['f', 'F']:
    c = (float(tempstr[:-1]) - 32) / 1.8
    print('转换后的温度是%.2fC' % c)
elif tempstr[-1] in ['c', 'C']:
    f = float(tempstr[:-1]) * 1.8 + 32
    print('转换后的温度是%.2fF' % f)
else:
    print('格式输入错误')
