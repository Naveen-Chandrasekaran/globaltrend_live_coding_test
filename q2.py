import heapq

def dijkstra(graph,start):
    n=len(graph)

    distances={vertex: float('infinity') for vertex in range(n)}
    distances[start]=0

    priority_queue=[(0,start)]

    while priority_queue:
        current_distance,current_vertex=heapq.heappop(priority_queue)

        if(current_distance > distances[current_vertex]):
            continue
        for neighbor,weight in graph[current_vertex].items():
            distance=current_distance+weight

            if distance< distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(priority_queue,(distance,neighbor))
    return distances

graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}
source = 0
shortest_paths=dijkstra(graph,source)

print(shortest_paths)
     
