"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

Version: 0.1
原Author: 骆昊

改一下：固定每次下注的资产，统计10场，每场坚持多少次下注破产,赢多少场，输多少场

"""
from random import randint

xiazhu = int(input('请下注: '))

for i in range(1,11):
    money = 1000
    time = 0
    time_1 = 0 #赢
    time_2 = 0 #输
    while money > 0:
        #print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = xiazhu #int(input('请下注: '))
            if debt > money : #如果钱不够
                debt = money
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        #print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            #print('玩家胜!')
            money += debt
            time+=1
            time_1+=1
        elif first == 2 or first == 3 or first == 12:
            #print('庄家胜!')
            money -= debt
            time+=1
            time_2+=1
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            #print('玩家摇出了%d点' % current)
            if current == 7:
                #print('庄家胜')
                time+=1
                time_2+=1
                money -= debt
            elif current == first:
                #print('玩家胜')
                time+=1
                time_1+=1
                money += debt
            else:
                needs_go_on = True
    #print('你破产了, 游戏结束!')
    print(time,time_1,time_2)