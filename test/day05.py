# -*- coding:utf-8 -*-
#!/usr/bin/python

'''
写一个餐厅菜单显示程序，根据不同的菜系分成顶级菜单：湘菜、粤菜等;
根据肉食、蔬菜、特色菜分为二级菜单，根据每个选项里面的各个菜式分为三级菜单，
可以根据你输入的菜系、菜类、菜式可以选择进入各子菜单，查看菜式，也可以选择退出菜单。
'''

while True:

    print("菜系：\n1、湘菜；\n2、粤菜\n3、退出")
    choice = input("选择菜系：")
    if choice == '1':
        print("菜类：\n1、肉食；\n2、蔬菜\n3、特色菜\n4、退出")
        choice = input("选择菜类：")
        if choice == '1':
            print("菜式：\n1、菜式A；\n2、菜式B\n3、菜式C\n4、退出")
            choice = input("选择菜类：")
            if choice == '4':
                break
        if choice == '2':
            pass
        if choice == '3':
            pass
        if choice == '4':
            break
    if choice == '2':
        pass
    if choice == '3':
        break