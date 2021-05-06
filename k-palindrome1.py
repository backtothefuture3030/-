def is_palin(s):
    size = len(s) / 2
    for i in range(size):
        if s[i] != s[-(i+1)]: return False
    return True


def chk_palin(s, max_k, k=0):
    if k > max_k:
        return False

    if is_palin(s):
        return True

    size = len(s) / 2
    for i in range(size):
        if s[i] != s[-(i+1)]:
            #
            # remove leftmost
            #
            left_s = s[:i]+s[i+1:]

            #
            # remove rightmost
            #
            if i == 0:
                right_s = s[:-(i+1)]
            else:
                right_s = s[:-(i+1)]+s[-i:]

            return chk_palin(left_s, max_k, k+1) \
                or chk_palin(right_s, max_k, k+1)


print (chk_palin("abxa", 1))
print (chk_palin("abdxa", 1))