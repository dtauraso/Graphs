"""
Simple graph implementation
"""
from collections import defaultdict

from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        pass  # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        pass  # TODO
        if v1 in self.vertices:
            if v2 in self.vertices:
                self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO
        if vertex_id in self.vertices:

            return list(self.vertice[vertex_id])

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        pass  # TODO

        visited = {i: 0 for i in self.vertices}

        my_queue = Queue()
        my_queue.enqueue(starting_vertex)
        while my_queue.size() > 0:

            current_node = my_queue.dequeue()

            if visited[current_node] == 0:
                print(current_node)

                visited[current_node] = 1
                for node in self.vertices[current_node]:
                    my_queue.enqueue(node)

            


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO
        # we want the verticies ordered
        # print('here')
        graph_for_stack = {i: list(self.vertices[i]) for i in self.vertices}
        my_stack = Stack()
        current = {'current': starting_vertex, 'ith_neighbor': 0}
        visited = {i: 0 for i in self.vertices}

        count = 0
        # print(not(my_stack.size() == 0) or current['current'] in graph_for_stack)
        # (current is not none) and (we have a stck or node is in graph)
        while (current is not None) and (not(my_stack.size() == 0) or current['current'] in graph_for_stack):
        
            # if count == 15:
            #     print('loop has reached it\'s limit')
            #     return
            # print(my_stack.stack)
            # print(my_stack.stack, current['current'], graph_for_stack[ current['current'] ], visited[ current['current'] ])

            # the current node is in the graph and it hasn't been visited
            if current['current'] in graph_for_stack and visited[ current['current'] ] == 0:
  
                    visited[ current['current'] ] = 1

                    print(current['current'])

                    # this is why each set of vertices needs to be an array
                    my_stack.push({'current': current['current'], 'ith_neighbor': 0})
                    current = { 'current': graph_for_stack[ current['current'] ][0],
                                'ith_neighbor': 0}
            else:
                # node doesn't exist or we are revisiting a node
                current = my_stack.pop()
                if current is not None:
                    current['ith_neighbor'] += 1

                    # set current to the current's current at the current's ith neighbor
                    if current['ith_neighbor'] < len( graph_for_stack[ current['current'] ] ):
                        current['current'] = graph_for_stack[ current['current'] ][ current['ith_neighbor'] ]
            count += 1



    def dft_recursive_helper(self, current_vertex, visited_verticies):

        if current_vertex not in self.vertices:
            return
        else:
            if visited_verticies[current_vertex] == 0:
                print(current_vertex)
                visited_verticies[current_vertex] = 1
                # it's revisiting neighbos
                for neighbor in self.vertices[current_vertex]:
                    self.dft_recursive_helper(neighbor, visited_verticies)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

        # I'm using a helper function so the graph doesn't need to fundamentally
        # altered for coloring verticies
        visited = {i: 0 for i in self.vertices}
        self.dft_recursive_helper(starting_vertex, visited)
    def get_path(self, destination_vertex, parents):
        tracker = destination_vertex
        search_path = []
        while tracker != destination_vertex:
            search_path = [tracker, *search_path]
            tracker = parents[tracker]
        # print(search_path)
        return search_path
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
        # [print(i, self.vertices[i]) for i in self.vertices]
        visited = {i: 0 for i in self.vertices}

        my_queue = Queue()
        my_queue.enqueue(starting_vertex)
        current_node = -1

        # this is how we remember the path from the start vertex to the
        # destination(reversed linked list)
        parents = {i: 0 for i in self.vertices}

        while current_node != destination_vertex:

            current_node = my_queue.dequeue()

            if visited[current_node] == 0:
                # print(current_node)

                visited[current_node] = 1
                for node in self.vertices[current_node]:
                    my_queue.enqueue(node)
                    parents[node] = current_node
        # [print(i, parents[i]) for i in parents]
        tracker = destination_vertex
        search_path = []
        while tracker > 0:
            search_path = [tracker, *search_path]
            tracker = parents[tracker]
        # print(search_path)
        return search_path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO
        # we want the verticies ordered
        # print('here')
        graph_for_stack = {i: list(self.vertices[i]) for i in self.vertices}
        my_stack = Stack()
        current = {'current': starting_vertex, 'ith_neighbor': 0}
        visited = {i: 0 for i in self.vertices}

        parents = {i: 0 for i in self.vertices}

        count = 0
        # print(not(my_stack.size() == 0) or current['current'] in graph_for_stack)
        # (current is not none) and (we have a stck or node is in graph)
        while (current is not None) and (not(my_stack.size() == 0) or current['current'] in graph_for_stack):
        
            # if count == 15:
            #     print('loop has reached it\'s limit')
            #     return
            # print(my_stack.stack)
            # print(my_stack.stack, current['current'], graph_for_stack[ current['current'] ], visited[ current['current'] ])
            if current['current'] == destination_vertex:
                # print()
                # print(destination_vertex)
                break
            # the current node is in the graph and it hasn't been visited
            if current['current'] in graph_for_stack and visited[ current['current'] ] == 0:
  
                    visited[ current['current'] ] = 1

                    # print(current['current'])

                    # this is why each set of vertices needs to be an array
                    my_stack.push({'current': current['current'], 'ith_neighbor': 0})

                    # so the next node maps to the current node
                    parents[ graph_for_stack[ current['current'] ][0] ] = current['current']

                    current = { 'current': graph_for_stack[ current['current'] ][0],
                                'ith_neighbor': 0}
            else:
                # node doesn't exist or we are revisiting a node
                current = my_stack.pop()
                if current is not None:
                    current['ith_neighbor'] += 1

                    # set current to the current's current at the current's ith neighbor
                    if current['ith_neighbor'] < len( graph_for_stack[ current['current'] ] ):

                        # so the next node maps to the current node
                        parents[ graph_for_stack[ current['current'] ][ current['ith_neighbor'] ] ] = current['current']

                        current['current'] = graph_for_stack[ current['current'] ][ current['ith_neighbor'] ]
            count += 1
        # [print(i, parents[i]) for i in parents]

        already_found_path = set()
        tracker = destination_vertex
        search_path = []
        # there may be cycles involving any nodes along the path
        while tracker > 0 and tracker not in already_found_path:
            # print(tracker)
            search_path = [tracker, *search_path]
            already_found_path.add(tracker)

            tracker = parents[tracker]
        # print(search_path)
        return search_path

        

    def dfs_recursive_helper(self, current_vertex, destination_vertex, visited_verticies, parents):
        # [print(i, parents[i]) for i in parents]
        # print()
        if current_vertex not in self.vertices:
            return
        else:
            if visited_verticies[current_vertex] == 0:
                visited_verticies[current_vertex] = 1

                # print(current_vertex)
                if current_vertex == destination_vertex:
                    return

                for neighbor in self.vertices[current_vertex]:

                    parents[neighbor] = current_vertex
                    self.dfs_recursive_helper(neighbor, destination_vertex, visited_verticies, parents)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO
        visited = {i: 0 for i in self.vertices}
        parents = {i: 0 for i in self.vertices}
        self.dfs_recursive_helper(starting_vertex, destination_vertex, visited, parents)
        # print()
        # print(destination_vertex)
        already_found_path = set()
        tracker = destination_vertex
        search_path = []
        # there may be cycles involving any nodes along the path
        while tracker not in already_found_path:
            search_path = [tracker, *search_path]
            already_found_path.add(tracker)
            tracker = parents[tracker]
        # print(search_path)
        return search_path

        # [print(i, parents[i]) for i in parents]
        # return self.get_path(destination_vertex, parents)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('start looking here')
    graph.dft(1)
    print('done')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
