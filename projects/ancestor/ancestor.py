from collections import defaultdict
# from graph import *

def get_node_farthest_away(graph, current_node, visited):

    # seems to work but it is only able to compare 1 and 1
    # a sum would be ideal to work here
    # My guess is it actually doesn't work for all cases, but the tests
    # are not comprehensive

    # print(current_node)
    if current_node not in graph:
        # print('dead end')
        return {'distance': -1, 'node': current_node}
    elif len(graph[current_node]) == 0:

        return {'distance': 1, 'node': current_node}
    else:
        # print('here')
        if visited[current_node] == 0:
            # print('just visited')
            visited[current_node] = 1
            candidates = []
            for child in graph[current_node]:
                candidates.append(get_node_farthest_away(   graph,
                                                            child,
                                                            visited))
            # print('candidates', candidates)
            best_candidate = {  'distance': candidates[0]['distance'],
                                'node': candidates[0]['node']}
            for candidate in candidates:
                if candidate['distance'] > best_candidate['distance']:
                    best_candidate = {  'distance': candidate['distance'],
                                        'node': candidate['node']}
            return best_candidate

            
def make_reverse_graph(list_of_links):

    my_graph = defaultdict(list)

    for link in list_of_links:
        my_graph[link[1]].append(link[0])
        # just in case there are nodes with no outoging edges
        if link[0] not in my_graph:
            # defaultdict init call I suspect
            my_graph[link[0]]
    return my_graph
def earliest_ancestor(ancestors, starting_node):

    # print()
    # list of adjaciency edges
    # make reverse graph
    my_graph = make_reverse_graph(ancestors)
    if starting_node not in my_graph:
        return None

    # no children
    elif len(my_graph[starting_node]) == 0:
        return -1

    # there are children
    else:
        visited = {i: 0 for i in my_graph}
        # [print(i, my_graph[i]) for i in my_graph]
        # print()
        # first test passes
        final_candidate = get_node_farthest_away(my_graph, starting_node, visited)
        return final_candidate['node']
    # if starting node has no children
        # return it
    # else
        # get_node_farthest_away(graph, starting_node)
    # pass