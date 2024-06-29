1. Single-Source Shortest Path

Question: Given a graph and a source node, find the shortest path from the source node to all other nodes in the graph.

Solution Sketch: Use Dijkstra’s algorithm to maintain a priority queue that always expands the node with the smallest known distance from the source.

2. Shortest Path in a Weighted Grid

Question: Given a 2D grid where each cell has a weight, find the shortest path from the top-left to the bottom-right corner.

Solution Sketch: Treat each cell as a node and connect adjacent cells with edges weighted by their values. Use Dijkstra’s algorithm starting from the top-left corner.

3. Network Delay Time

Question: Given a network of nodes represented by a weighted directed graph, and a signal that starts from a given node, determine how long it will take for all nodes to receive the signal.

Solution Sketch: Use Dijkstra’s algorithm from the starting node to compute the shortest time it takes for the signal to reach all other nodes. The answer is the maximum distance in the resulting shortest-path tree.

4. Cheapest Flights Within K Stops

Question: Given a list of flights represented as edge weights between nodes (airports), find the cheapest flight from a source to a destination with at most K stops.

Solution Sketch: Use a variation of Dijkstra’s algorithm where the priority queue also tracks the number of stops taken to reach each node. Only consider nodes if the number of stops does not exceed K.

5. Shortest Path with Constraints

Question: Find the shortest path in a graph where each node can only be visited a limited number of times, or where certain nodes must be visited in a specific order.

Solution Sketch: Modify Dijkstra’s algorithm to include additional state information in the priority queue, such as the number of times a node has been visited or the order of nodes visited.

6. Finding the Most Reliable Path

Question: In a network with reliability values assigned to each edge, find the path from a source to a destination that maximizes the probability of successful traversal.

Solution Sketch: Use a variation of Dijkstra’s algorithm that maximizes the product of edge reliabilities instead of summing edge weights.

7. Shortest Path in Dynamic Graphs

Question: Given a graph that changes dynamically (edges can be added or removed), efficiently maintain the shortest paths from a source to all other nodes.

Solution Sketch: Use a dynamic version of Dijkstra’s algorithm that updates the shortest-path tree incrementally when edges are added or removed.

8. Path with Maximum Min-Edge

Question: Find a path from a source to a destination such that the minimum edge weight in the path is maximized.

Solution Sketch: Use a variation of Dijkstra’s algorithm that prioritizes paths based on the minimum edge weight encountered so far, using a max-heap.

9. Multi-Source Shortest Path

Question: Given multiple source nodes, find the shortest paths from any of these sources to all other nodes in the graph.

Solution Sketch: Initialize Dijkstra’s algorithm from all source nodes simultaneously by adding them to the priority queue with a distance of zero.

10. K Shortest Paths

Question: Find the K shortest paths from a source to a destination in a graph.

Solution Sketch: Use a variation of Dijkstra’s algorithm that maintains multiple paths to each node and extends the algorithm to track the K shortest paths.

11. Resource-Constrained Shortest Path

Question: Find the shortest path in a graph with additional constraints, such as a limited budget or time.

Solution Sketch: Extend Dijkstra’s algorithm to include the constraint as part of the state information maintained in the priority queue.

12. Shortest Path with Forbidden Nodes

Question: Find the shortest path from a source to a destination while avoiding a set of forbidden nodes.

Solution Sketch: Modify Dijkstra’s algorithm to skip over forbidden nodes during the search process.

13. Path with Maximum Rewards

Question: Each node has a reward associated with it. Find the path from a source to a destination that maximizes the total reward.

Solution Sketch: Use a variation of Dijkstra’s algorithm that prioritizes paths based on the accumulated reward rather than the shortest distance.

14. Delivery Routes Optimization

Question: Optimize delivery routes in a city where each intersection and road segment has different time costs.

Solution Sketch: Model the city as a graph and use Dijkstra’s algorithm to find the shortest delivery routes.

15. Weighted Bipartite Graph Matching

Question: In a weighted bipartite graph, find the maximum weight matching.

Solution Sketch: Use Dijkstra’s algorithm as a subroutine in the Hungarian algorithm to find the shortest augmenting paths.
