def taumBday(b, w, bc, wc, z):
    # Write your code here
    if abs(bc - wc) <= z:
        result = b*bc + w*wc
    else:
        total_number_gifts = b + w
        pair_values = (b,wc) if wc < bc else(w, bc)
        result = total_number_gifts*pair_values[1] + z*pair_values[0]
    return result