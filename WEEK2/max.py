def MAX(lst_):
    if len(lst_)==1:
        return lst_[0]
    else:
        _max = MAX(lst_[1:])
        # print(_max,lst_[0])
        if _max >= lst_[0]:
            return _max
        else :
            return lst_[0]

n = list(map(int,input().split()))
print("max =",MAX(n))