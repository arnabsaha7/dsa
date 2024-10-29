import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import networkx as nx


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# In-Order Traversal (Left -> Root -> Right)
def inorder_traversal(root, result=[]):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
    return result

# Pre-Order Traversal (Root -> Left -> Right)
def preorder_traversal(root, result=[]):
    result = []
    def traverse(node):
        if node:
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return result

# Post-Order Traversal (Left -> Right -> Root)
def postorder_traversal(root, result=[]):
    if root:
        postorder_traversal(root.left, result)
        postorder_traversal(root.right, result)
        result.append(root.val)
    return result

# Build the Graph
def build_graph(root, graph=None, pos=None, x=0, y=0, layer=1):
    if root is None:
        return
    graph.add_node(root.val, pos=(x,y))
    if root.left:
        graph.add_edge(root.val, root.left.val)
        build_graph(root.left, graph, pos, x - 1 / layer, y - 1, layer + 1)
    if root.right:
        graph.add_edge(root.val, root.right.val)
        build_graph(root.right, graph, pos, x + 1 / layer, y - 1, layer + 1)
   
# Animate & Save
def animate_traversal(traversal_path, G, pos, traversal_type):
    fig, ax = plt.subplots(figsize=(6, 6))

    def update(num):
        ax.clear()
        colors = ['red' if node == traversal_path[num] else 'lightblue' for node in G.nodes()]
        nx.draw(G, pos, ax=ax, with_labels=True, node_color=colors, node_size=800, font_size=12, font_color="black")
        ax.set_title(f"{traversal_type} Step {num + 1}: Visiting node {traversal_path[num]}")

    ani = animation.FuncAnimation(fig, update, frames=len(traversal_path), interval=1000, repeat=False)
    ani.save(f'DSA/Trees/dfs_traversal/img/{traversal_type.lower()}_traversal.gif', writer='imagemagick')
    plt.close(fig)


# Tree Setup
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)


# Build Graph Structure
G = nx.DiGraph()
build_graph(root, G)
pos = nx.get_node_attributes(G, 'pos')

# Perform each traversal and animate
preorder_path = preorder_traversal(root, [])
inorder_path = inorder_traversal(root, [])
postorder_path = postorder_traversal(root, [])

# Generate animations for each traversal
animate_traversal(preorder_path, G, pos, "Pre-Order")
animate_traversal(inorder_path, G, pos, "In-Order")
animate_traversal(postorder_path, G, pos, "Post-Order")

print("Animations for Pre-Order, In-Order, and Post-Order traversals saved as GIFs.")