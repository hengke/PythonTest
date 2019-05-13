#coding = utf8
from collections import OrderedDict


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
    print(tax(12705))
    print(tax(15000, 2295))
    print(tax(income=15000, social_benefits=2295))
    print(tax(social_benefits=2295, income=15000))
