#包装好的A1类糖果体积为一个存储单位，而包装好的A2类糖果体积正好是A1类的两倍。
#输入中有多组测试数据。每组测试数据的第一行有两个整数n和v，1<=n<=10^5, 1<=v<=10^9，n为可供选购糖果数量，
#v为货车的容量。随后n行为糖果的具体信息，第一行编号为1，第二行编号为2，
#以此类推，最后一行编号为n。每行包含两个整数ti和pi，1<=ti<=2, 1<=pi<=10^4，ti为糖果所属的序列，1为A1、2为A2，pi则是其中的魔幻因子含量。
#输出
#对每组测试数据，先在单独的一行中输出能采购的糖果中的魔幻因子最高含量，之后在单独的行中按编号
#从小到大的顺序输出以空格分隔的糖果编号，若有多组糖果组合均能满足要求，输出编号最小的组。
#若没有糖果能够满足要求，则在第一行中输出0，第二行输出“No”。
#n个糖果数量，车厢总容量为V
while True:
    try:
        n,v=map(int,input().split())
        t=[]
        p=[]
        res = []
#每行输入两个整数，将它分别存入两个list
        for i in range(n):
            ti,pi=map(int,input().split())
            t.append(ti)
            p.append(pi)
        #为了解决超时问题
        if (2*n)<v:
            print(sum(p))
            a = []
            for i in range(1, n + 1):
                a.append(str(i))
            print(" ".join(a))
#f[i][j]用来存放最高含量
#定义并初始化一个二维数组(n+1)*(v+1)
#因为按行存储，所以先定了列，在定义行
        else:
            f=[[0 for i in range(v+1)]for j in range(n+1)]
        #print(t)
            for i in range(1,n+1):
                for j in range(1,v+1):
                    if t[i-1]>j:
                        f[i][j]=f[i-1][j]
                    else:
                        f[i][j]=max(f[i-1][j],(f[i-1][j-t[i-1]]+p[i-1]))
            #print(f)
            if f[n][v]==0:
                print("0"+'\n'+"No")
            else:
                print(f[n][v])
                for i in range(n,0,-1):
                        temp=v
                        if f[i][v] != f[i - 1][v] and f[i][v]==f[i-1][v-t[i-1]]+p[i-1]:
                            res.append(i)
                            v = v-t[i-1]
                        else:
                            continue
                #print(res)
                for i in range(len(res)):
                    res[i]=str(res[i])
                res=res[::-1]
                print(" ".join(res))
    except:
        break
