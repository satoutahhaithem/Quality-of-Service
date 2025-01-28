def calculate_ie_eff(Ie, Ppl, BurstR, Bpl):
    # Formula to calculate Ie_eff
    Ie_eff = Ie + (95 - Ie) * (Ppl / ((Ppl / BurstR) + Bpl))
    return Ie_eff

# def calculate_Id(T):
#     # Formula to calculate Id (delay impairment)
#     if T > 177.3:
#         Id = 0.024 * T + 0.11 * (T - 177.3)
#     else:
#         Id = 0.024 * T
#     return Id

def calculate_R(Ie_eff, Id, A=0):
    # Formula to calculate the R-factor
    R = 93.2 - Ie_eff - 0.16 - A
    return R

# Constants
Ie = 11  # G.729 codec impairment factor
Bpl = 19  # G.729 burst loss probability
BurstR = 1  # No additional successive losses
T = 150  # Delay in ms

# Packet loss probabilities to test
Ppl_values = [0.01, 0.05, 0.10]  # 1%, 5%, and 10%

# Calculate Id based on delay T
# Id = calculate_Id(T)

# Calculate R-factor for each Ppl value
for Ppl in Ppl_values:
    Ie_eff = calculate_ie_eff(Ie, Ppl, BurstR, Bpl)
    R = calculate_R(Ie_eff, 0.16)
    print ("Ie-eef===>",Ie_eff)
    print(f"R-factor for Ppl={Ppl*100}%: {R}")

