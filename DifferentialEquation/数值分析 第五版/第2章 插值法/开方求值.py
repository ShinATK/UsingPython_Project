import numpy as np
import matplotlib.pyplot as plt

def square_root(a, x0, e_mark):
    x_last = x0
    result_list = [x0]

    # 开方计算主体部分
    while True:
        x_next = 0.5 *(x_last + a/x_last)
        print(x_next)
        x_last = x_next
        result_list.append(x_next)

        # 根据给定精度判断是否停止循环
        if abs(np.sqrt(a) - x_next) > e_mark:
            continue
        else:
            break

    # 绘制图像观察迭代变化趋势
    plt.axhline(y=np.sqrt(a), label='True Value', ls='--', c='red',)
    plt.plot(range(1, len(result_list)+1), result_list, label='Calculaion Result', c='blue')
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'style': 'italic',
            'size': 20
            }
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    plt.xlabel('Calculation Times', font)
    plt.ylabel('Result', fontdict=font)
    plt.legend(prop=font)
    plt.show()

    return x_next

if __name__ == '__main__':
    a = 13  # 开方数值
    x0 = 100  # 迭代初始值
    e_mark = 0.5e-6  # 计算精度

    result = square_root(a, x0, e_mark)