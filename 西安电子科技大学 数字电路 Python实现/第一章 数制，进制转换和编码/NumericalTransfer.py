import math
import numpy

# 1.给定数制下数字，转换为指定数制（T）
# 2.增加小数部分转换（）
#   2.1 十进制小数转换为二进制小数（T）
#   2.2 二进制小数转换为十进制小数
# 3.增加按权展开式（）

def Other2Decimal(x, input_R=10):
    # 将输入的数字按照指定数制转换为十进制
    if input_R == 10:
        return x
    elif input_R < 10:
        sum = 0
        i = 0
        length=len(x)
        for each in x:
            i += 1
            sum+=int(each) * input_R**(length-i)
    else:
        H_decimal = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        sum = 0
        i = 0
        length = len(x)
        for each in x:
            i += 1
            if each.isdigit():
                sum += int(each) * input_R**(length - i)
            else:
                sum += H_decimal[each] * input_R**(length - i)
    return sum
def Decimal2Other(x, output_R=2):
    # 将十进制数字转换为指定数制的数字
    if output_R==10:
        return x
    mod_integer = ''
    # 输出为2，8，10进制
    H_decimal = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while x > 0:
        y = x // output_R
        z = x % output_R
        x = y
        if z >= 10:
            mod_integer += str(H_decimal[z])
        else:
            mod_integer += str(z)
    return mod_integer[::-1]

def test(x, output_R=2):
    # 十进制小数转换为二进制小数
    y = x - int(x)
    mod_decimal = '.'
    while y != int(y):
        mod_decimal += str(int(output_R*y))
        y = output_R*y - int(output_R*y)
    return mod_decimal

if __name__ == '__main__':
    while True:
        print('Please input number:')
        x = input()

        # print('Please input input_base(2, 8, 10, 16)')
        # input_base = input()

        # # 测试其他进制转十进制
        # decimal_form = Other2Decimal(x, int(input_base))
        # print(decimal_form)

        print('Please input output_base(2, 8, 10, 16):')
        output_base = input()

        # # 测试十进制转其他进制
        # other_form = Decimal2Other(int(x), int(output_base))
        # print(other_form)

        test_form = test(float(x), int(output_base))
        print(test_form)