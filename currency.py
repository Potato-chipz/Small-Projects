def money_japanese_to_rmb(m):
    rmb = 0.0

    rmb = m/21.8
    usd = rmb/7.22

    return rmb

def money_japanese_to_usd(m):
    rmb = 0.0

    rmb = m/21.8 
    usd = rmb/7.22

    return usd

cost_in_j = 3000

print("The cost covert to CNY is: ¥", money_japanese_to_rmb(cost_in_j))
print("The cost covert to USD is: $", money_japanese_to_usd(cost_in_j))
    