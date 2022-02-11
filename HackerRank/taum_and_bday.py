b, w= 384, 887
bc, wc, z= 2778, 6916, 7794

total_gift= b+w
both= (b*bc) + (w*wc)

def buy_one(total_gift, gift_to_buy, gift_price, gift_to_not_buy, rate):
    buy_all= total_gift*gift_price
    if(gift_to_buy==gift_to_not_buy):
        total= (buy_all / total_gift) * gift_to_buy +  (gift_to_not_buy * (gift_price + rate))
    else:
        total= (buy_all/total_gift) * gift_to_buy + ((buy_all/total_gift) * gift_to_not_buy * (gift_price+rate))

    return int(total)

print((buy_one(total_gift, b, bc, w, z), buy_one(total_gift, w, wc, b, z), both))