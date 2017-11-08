import random
import string

def gen_coupons(n_coupons, length, value):
    coupon_list = []
    for _ in range(n_coupons):
        coupon = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
        coupon_list.append((coupon, value))
    return coupon_list

if __name__ == '__main__':
    import sys
    print(gen_coupons(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
