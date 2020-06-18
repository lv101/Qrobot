'''
#每日一图#  定时群推送
'''
import time
from bing_pic import bing_t

judge = 0

def judge_0():
    global judge
    while not judge:
        try:
            timestr = time.localtime()
            judge_start = eval(time.strftime("%H", timestr))
            # print("judge_0", judge_start)
            if judge_start >= 8:
                judge = bing_t()
                if judge:
                    judge_1()
                else:
                    time.sleep(1)
            else:
                time.sleep(666)
        except:
            time.sleep(1)

def judge_1():
    global judge
    while judge:
        timestr = time.localtime()
        judge_start = eval(time.strftime("%H", timestr))
        # print("judge_1", judge_start)
        if judge_start < 6:
            judge = 0
            judge_0()
        else:
            time.sleep(666)