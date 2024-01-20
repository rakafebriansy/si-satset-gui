def DataInput(region):
    list_nodedge = ''
    with open(f'{region}.txt', "r") as txt:
        while True:
            nodedge = txt.readline()
            list_nodedge+=nodedge
            if '\n' not in nodedge:
                break
    list_node = list_nodedge.split('\n')[0].split(',')
    list_edgeBEFORE, list_edgeAFTER = list_nodedge.split('\n')[1].split(','), {}
    for edge in list_edgeBEFORE:
        node_a = int(edge.split('.')[0])
        node_b = int(edge.split('.')[1])
        weight = int(edge.split('.')[2])
        if node_a not in list_edgeAFTER:
            list_edgeAFTER[node_a] = {}
        list_edgeAFTER[node_a][node_b] = weight
        if node_b not in list_edgeAFTER:
            list_edgeAFTER[node_b] = {}
        list_edgeAFTER[node_b][node_a] = weight
    return list_edgeAFTER, list_node

def Graphs(list_edge,start,end,graph=[]):
    graph = graph + [start]
    if start == end:
        return [graph]
    if start not in list_edge:
        return []
    list_graph = []
    for node in list_edge[start]:
        if node not in graph:
            newGraph = Graphs(list_edge,node,end,graph)
            for newNode in newGraph:
                list_graph.append(newNode)
    return list_graph

def TotalWeight(list_edge,start,end):
    table = Graphs(list_edge,start,end)
    for i in table:
        total_weight = 0
        for j in range(len(i)-1):
            total_weight += list_edge[i[j]][i[j+1]]
        i.insert(0,total_weight)    
    return sorted(table)

def MinimumWeight(sorted_table):
    for i in sorted_table:
        i.remove(i[0])
    return sorted_table