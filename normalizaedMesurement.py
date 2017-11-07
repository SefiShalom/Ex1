#Normalized Probability:
p = [0.2,0.2,0.2,0.2,0.2]
world = ['green', 'red', 'red', 'green', 'green']
Z = ['red','green']
pHit = 0.6
pMiss = 0.25

def sense(p, Z):
    q=[]
    for i in range(len(p)):
            hit = (Z == world[i])
            q.append(p[i] * (hit * pHit + (1-hit)* pMiss))
    s=sum(q)
    for i in range(len(p)):
        q[i]=q[i]/s
    return q




for i in range(6):
    p= sense(p, Z[0])
print("After 6 senses of ",Z[0],":")
print (p)
for i in range(1):
    p= sense(p, Z[1])
print (p)