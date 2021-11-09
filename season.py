def season(x):
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    fall = [9, 10, 11]
    if x in winter:
        print('Winter')
    elif x in spring:
        print('Spring')
    elif x in summer:
        print('Summer')
    elif x in fall:
        print('Fall')

season(3)