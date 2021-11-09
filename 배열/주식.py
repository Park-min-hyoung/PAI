#121

import sys

prices = [7,1,5,3,6,4]
profit = 0
min_price = sys.maxsize

for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

print(profit)

# 틀렸음
'''1. 저장된 저점(price가 가장 낮은 지점)을 현재 price에서 빼는 아이디어
(기존의 저점보다 현재 price가 작으면 저점은 수정된다)'''

'''https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2
&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CO
DE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1'''
