def PremierLeagueScore_Sort(name,points,gd):
    for i in range(len(points)):
        for j in range(i,len(points)):
            if points[i]<points[j]:
                points[i],points[j]=points[j],points[i]
                name[i],name[j]=name[j],name[i]
                gd[i],gd[j]=gd[j],gd[i]
            elif points[i]==points[j] and gd[i]<gd[j]:    
                name[i],name[j]=name[j],name[i]
                gd[i],gd[j]=gd[j],gd[i]
    
inp = input("Enter Input : ").split("/")
points,gd,name=[[]]*len(inp),[[]]*len(inp),[[]]*len(inp)
op,ogd = {},{}
for i in range(len(inp)):
    n,wins,loss,draws,scored,concede = inp[i].split(",")
    name[i] = n
    points[i] = 3*int(wins) + int(draws)
    gd[i] = int(scored) - int(concede)
print("== results ==")
PremierLeagueScore_Sort(name,points,gd)
for x in range(len(points)):
    output = []
    output.append(name[x])
    op['points'] = points[x]
    output.append(op)
    ogd['gd'] = gd[x]
    output.append(ogd)
    print(output)
