#coding = utf8

from collections import OrderedDict
import bisect


ranges = [65,70,75,80,85]
rate =  [20,25,30,35,40]
QuickDeduction = [0,0.25,0.75,1.5,2.5]

def GetSpecialOilIncome(OilPrice,exempt=65):
    if OilPrice <= exempt:
        return 0.0
    i = bisect.bisect_left(ranges, OilPrice)
    SpecialOilIncome = (OilPrice - exempt) * rate[i-1] / 100 - QuickDeduction[i-1]
    return SpecialOilIncome

if __name__ == '__main__':
# 60			        0
# 65			        0
# 68	0.2		        13.6
# 70	0.2		        14
# 73	0.25	0.25	18
# 75	0.25	0.25	18.5
# 78	0.3	    0.75	22.65
# 80	0.3	    0.75	23.25
# 84	0.35	1.5	    27.9
# 85	0.35	1.5	    28.25
# 90	0.4	    2.5	    33.5

    print(GetSpecialOilIncome(60))
    print(GetSpecialOilIncome(65))
    print(GetSpecialOilIncome(68))
    print(GetSpecialOilIncome(70))
    print(GetSpecialOilIncome(73))
    print(GetSpecialOilIncome(75))
    print(GetSpecialOilIncome(78))
    print(GetSpecialOilIncome(80))
    print(GetSpecialOilIncome(84))
    print(GetSpecialOilIncome(85))
    print(GetSpecialOilIncome(90))

    print(GetSpecialOilIncome(106.97,65))
    print(GetSpecialOilIncome(107.2,65))
    print(GetSpecialOilIncome(103.09,65))
    print(GetSpecialOilIncome(99.96,65))
    print(GetSpecialOilIncome(42.55,65))
    print(GetSpecialOilIncome(52.48,65))
    print(GetSpecialOilIncome(70.47,65))
    print(GetSpecialOilIncome(58.92,65))
    print(GetSpecialOilIncome(68.46,65))

