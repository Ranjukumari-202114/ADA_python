n_vertices = 5
INF= 999


def print_ans(dis):
    print("the shortest distance b/w every pair of vertice:")
    for i in range(n_vertices):
        for j in range(n_vertices): 
            if(dis[i][j] == INF):
                print("% 7s" %" INF",end="")
            else:
                print("%7d\t" %dis[i][j],end=" ")
                print("")

def floyd_warshall(Graph):
    dis=list(map(lambda i:list(lambda j:j,i)),Graph)

    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j])
                print_ans(dis)


if__name__== '_main_':
    Graph=[[0,5,INF,6,INF]
           [2,6,9,INF,2]
           [7,5,2,INF,INF]
           [2,9,INF,7,10]
           [INF,5,INF,INF,7]]
        floyd_warshall(Graph)   