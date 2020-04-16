#conding:utf-8
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：张康驰
日期：2020.04.16‘
"""

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

import random

def name_to_number(name):
    
    '''将游戏对象对应到不同的整数'''
        
    if name == '石头' :
        player_choice_number=0
    if name == '史波克' :
        player_choice_number=1
    if name == '纸' :
        player_choice_number=2
    if name == '蜥蜴' :
        player_choice_number=3        
    if name == '剪刀' :
        player_choice_number=4
    return player_choice_number                                                  
    
    # 使用if语句将各游戏对象对应到不同的整数   

def number_to_name(number):
   
    '''将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对'''    
    
    if number==0:
        comp_choice='石头'
    if number==1:
        comp_choice='史波克'    
    if number==2:
        comp_choice='纸'            
    if number==3:
        comp_choice='蜥蜴'            
    if number==4:
        comp_choice='剪刀'
    return comp_choice
                     
    # 使用if语句将不同的整数对应到游戏的不同对象
    
def rpsls(player_choice_number,comp_number):
    
    '''用户玩家任意给出一个选择，根据RPSLS游戏规则，判断对应的结果'''
          
    if player_choice_number == 0 and (comp_number == 3 or comp_number == 4):
        result='您赢了！'
    elif player_choice_number == 1 and (comp_number == 0 or comp_number == 4):
        result='您赢了！'
    elif player_choice_number == 2 and (comp_number == 0 or comp_number == 1):
        result='您赢了！'
    elif player_choice_number == 3 and (comp_number == 1 or comp_number == 2):
        result='您赢了！'    
    elif player_choice_number == 4 and (comp_number == 2 or comp_number == 3):
        result='您赢了！'                
    elif player_choice_number == comp_number:
        result='您和计算机出的一样呢！'
    else:
        result='机器赢了'
    return result
    #用if/elif/else语句判断胜负结果
def result():  

    '''输入您的选择和产生电脑的选择，调用上面的函数输出选择的结果和胜负结果并进行循环。'''
    print("欢迎使用RPSLS游戏")
    print("--------") 
    player_choice = input('请输入您的选择:')             
    comp_number=random.randint(0,4)
    while player_choice == '剪刀' or player_choice == '石头' or player_choice == '纸' or player_choice == '蜥蜴' or player_choice == '史波克'  :
        player_choice_number=name_to_number(player_choice)
        print('您的选择为:'+player_choice)
        print('计算机的选择为:'+number_to_name(comp_number))
        print(rpsls(player_choice_number,comp_number))
        print()
        result()
    #输入您的选择和电脑的，判断输入正确时，输出胜负结果，并调用函数自身进行循环
    else:
        print('Error: No Correct Name')
        print()
        result()
    return    
    #输入错误时，进行提示，并调用函数自身进行循环
result()
pass

    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
    
    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    # 在屏幕上显示计算机选择的随机对象
    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
