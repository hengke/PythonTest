#coding = utf8
from collections import OrderedDict
import bisect


# ranges = [85,80,75,70,65]
# rate =  [40,35,30,25,25]
# QuickDeduction = [2.5,1.5,0.75,0.25,0]
ranges = [65,70,75,80,85]
rate =  [20,25,30,35,40]
QuickDeduction = [0,0.25,0.75,1.5,2.5]

def GetSpecialOilIncome(OilPrice,exempt=65):
    if OilPrice <= exempt:
        return 0.0
    i = bisect.bisect_left(ranges, OilPrice)
    # j = 0
    SpecialOilIncome = OilPrice * rate[i-1] / 100 - QuickDeduction[i-1]
    # while j < i:
    #     if j+1 < i:
    #         SpecialOilIncome += (ranges[j+1]-ranges[j]) * rate[j] - QuickDeduction[j]
    #     else:
    #         SpecialOilIncome += (OilPrice-ranges[j]) * rate[j] - QuickDeduction[j]
    #         j += 1
    return SpecialOilIncome

# 税率表, 2018.10新个税
tax_ratio = OrderedDict()
tax_ratio[(0, 5000)] = 0
tax_ratio[(5000, 3000)] = 0.03
tax_ratio[(3000, 12000)] = 0.1
tax_ratio[(12000, 25000)] = 0.2
tax_ratio[(25000, 35000)] = 0.25
tax_ratio[(35000, 55000)] = 0.3
tax_ratio[(55000, 80000)] = 0.35
tax_ratio[(80000, float('inf'))] = 0.45

# 计算税
def tax(income, social_benefits=0):
    income -= social_benefits
    total_tax = 0
    for k, v in tax_ratio.items():
        if income > k[1]:
            income -= k[1]
            total_tax += k[1] * v
        elif k[0] < income < k[1]:
            total_tax += income * v
            break
    return total_tax


if __name__ == '__main__':
#     print(tax(12705))
#     print(tax(15000, 2295))
#     print(tax(income=15000, social_benefits=2295))
#     print(tax(social_benefits=2295, income=15000))
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
