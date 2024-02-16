from collections import defaultdict

def solution(tickets):
    # Create a graph of all the tickets
    graph = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
        
    # for key,value in graph.items():
    #     print(key,value)

    route = []

    def visit(airport):
        # Visit all the destinations from the current airport
        while graph[airport]:
            visit(graph[airport].pop())
        route.append(airport)

    visit('ICN')

    # The route is constructed in reverse, so we reverse it back
    return route[::-1]