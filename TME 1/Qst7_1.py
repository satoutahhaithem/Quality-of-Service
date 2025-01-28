def calculate_ie_eff(Ie, Ppl, BurstR, Bpl):
    Ie_eff = Ie + (95 - Ie) * (Ppl / ((Ppl / BurstR) + Bpl))
    return Ie_eff


Ie = 11  # Example value for equipment impairment factor
Ppl = 0.01  # Example value for packet loss probability (5%)
BurstR = 1  # Example value for burst ratio
Bpl = 19  # Example value for burst loss probability (10%)

Ie_eff = calculate_ie_eff(Ie, Ppl, BurstR, Bpl)
print("Effective Impairment Factor (Ie_eff):", Ie_eff)
