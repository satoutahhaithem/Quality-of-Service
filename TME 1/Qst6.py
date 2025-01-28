import math

s_T = 1  
mT = 100 


def calculate_X(Ta, mT):
    return math.log(Ta / mT) / math.log(2)

def calculate_Idd(Ta, mT, s_T=1):
    X = calculate_X(Ta, mT)
    term_1 = (1 + X ** (6 * s_T)) ** (1 / (6 * s_T))
    term_2 = (1 + (X / 3) ** (6 * s_T)) ** (1 / (6 * s_T))
    Idd = 25 * (term_1 - 3 * term_2 + 2)
    return Idd

Ta_values = [150, 300, 500]  

for Ta in Ta_values:
    if Ta > mT:
        Idd = calculate_Idd(Ta, mT, s_T)
        print(f"For Ta = {Ta} ms, Idd = {Idd:.2f}")
