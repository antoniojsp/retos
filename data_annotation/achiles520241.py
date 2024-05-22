# Each small sweater costs $10, medium is $12 and large is $30.
sweater = {"s":10, "m":12, "l":30}
#   small pair of shorts costs $12, medium is $16 and large is $22.
shorts = {"s":12, "m":16, "l":22}
#  small t-shirt costs $9, medium is $14 and large is $25.
t_shirt = {"s":9, "m":14, "l":25}


# def create_json(region:str, sweater:tuple, shorts:tuple, t_shirt:tuple, quarter):

sales = 600*shorts["s"]+1000*t_shirt["l"]+200*sweater["s"]
sale_after_refund = sales - 200*sweater["s"]
print(sales)
print(sale_after_refund)