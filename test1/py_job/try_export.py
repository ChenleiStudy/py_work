# -- coding: utf-8 --


list=[1,23,5,6,0,3,5]

for i in list:
    try:
        a=5/i
        print(a)
    except Exception as e :
        print(e)

