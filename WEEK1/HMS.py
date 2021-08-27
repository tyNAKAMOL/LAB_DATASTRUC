print("*** Converting hh.mm.ss to seconds ***")
h, m, s = list(map(int, input("Enter hh mm ss : ").split()))
if (0<=h<60) and (0<=m<60) and (0<=s<60):
    H = str(h)
    M = str(m)
    S = str(s)
    if h < 10:
        H = '0'+str(h)
    if m < 10:
        M = '0'+str(m)
    if s < 10:
        S = '0'+str(s)
    print(H+":"+M+":"+S+" = "+str("{:,}".format(s+(m*60)+(h*3600)))+ " seconds")
else:
    if h<0 or h>=60:
        print("hh("+str(h)+") is invalid!")
    elif m<0 or m>=60:
        print("mm("+str(m)+") is invalid!")
    elif s<0 or s>=60:
        print("ss("+str(s)+") is invalid!")