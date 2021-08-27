n = list(map(int, input("Enter All Bid : ").split()))
if(len(n)==1):
    print("not enough bidder")
else:
    n.sort()
    Max = max(n)
    k=n.count(Max)
    if k>1:
        print("error : have more than one highest bid")
    else:
        print("winner bid is",Max,"need to pay",n[len(n)-2])