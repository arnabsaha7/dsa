import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import networkx as nx

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# BFS Traversal (Level-Order):
def bfs_traversal(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def build_graph(root, graph=None, x=0, y=0, layer=1):
    """Recursive function to create nodes and edges for tree structure"""
    if root is None:
        return
    graph.add_node(root.val, pos=(x, y))
    if root.left:
        graph.add_edge(root.val, root.left.val)
        build_graph(root.left, graph, x - 1 / layer, y - 1, layer + 1)
    if root.right:
        graph.add_edge(root.val, root.right.val)
        build_graph(root.right, graph, x + 1 / layer, y - 1, layer + 1)

def animate_traversal(traversal_path, G, pos, traversal_type):
    fig, ax = plt.subplots(figsize=(6, 6))

    def update(num):
        ax.clear()
        colors = ['orange' if node == traversal_path[num] else 'teal' for node in G.nodes()]
        nx.draw(G, pos, ax=ax, with_labels=True, node_color=colors, node_size=800, font_size=12, font_color="black")
        ax.set_title(f"{traversal_type} Step {num + 1}: Visiting node {traversal_path[num]}")

    ani = animation.FuncAnimation(fig, update, frames=len(traversal_path), interval=1000, repeat=False)
    ani.save(f'DSA/Trees/bfs_traversal/img/{traversal_type.lower()}_traversal.gif', writer='imagemagick')
    plt.close(fig)

# Tree setup
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)

# Build graph structure
G = nx.DiGraph()
build_graph(root, G)
pos = nx.get_node_attributes(G, 'pos')

# Perform BFS traversal and animate
bfs_path = bfs_traversal(root)
animate_traversal(bfs_path, G, pos, "BFS")

print("Animation for BFS traversal saved as a GIF.")