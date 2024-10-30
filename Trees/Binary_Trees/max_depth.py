import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
import os

# Define Node class for Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Build the graph with positions for nodes
def build_graph(root, graph=None, x=0, y=0, layer=1):
    if root is None:
        return
    graph.add_node(root.val, pos=(x, y))
    if root.left:
        graph.add_edge(root.val, root.left.val)
        build_graph(root.left, graph, x - 1 / layer, y - 1, layer + 1)
    if root.right:
        graph.add_edge(root.val, root.right.val)
        build_graph(root.right, graph, x + 1 / layer, y - 1, layer + 1)

# Depth calculation and recording steps for animation
def calculate_depth(node, depth_steps, depth=1):
    if node is None:
        return 0
    depth_steps.append((node.val, depth))  # Record depth calculation for animation
    left_depth = calculate_depth(node.left, depth_steps, depth + 1)
    right_depth = calculate_depth(node.right, depth_steps, depth + 1)
    max_depth = max(left_depth, right_depth) + 1
    if depth == 1:
        depth_steps.append(("Final", max_depth))  # Append final depth step
    return max_depth

# Animation function
def animate_depth_calculation(G, pos, depth_steps):
    fig, ax = plt.subplots(figsize=(8, 6))

    def update(num):
        ax.clear()
        if depth_steps[num][0] == "Final":
            max_depth = depth_steps[num][1]
            nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', node_size=800, font_size=12, font_color="black")
            ax.set_title(f"Binary Tree Maximum Depth (Height): {max_depth}")
        else:
            current_node, current_depth = depth_steps[num]
            colors = ['red' if node == current_node else 'lightblue' for node in G.nodes()]
            nx.draw(G, pos, ax=ax, with_labels=True, node_color=colors, node_size=800, font_size=12, font_color="black")
            ax.set_title(f"Depth Calculation Step {num + 1}: Node {current_node} at Depth {current_depth}")

    ani = animation.FuncAnimation(fig, update, frames=len(depth_steps), interval=1000, repeat=False)
    
    # Save the animation as GIF
    output_dir = "DSA/Trees/Binary_Trees/img"
    os.makedirs(output_dir, exist_ok=True)
    ani.save(f"{output_dir}/binary_tree_max_depth_calculation.gif", writer='pillow')
    plt.close(fig)

# Tree Setup
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

# Build Graph Structure
G = nx.DiGraph()
build_graph(root, G)
pos = nx.get_node_attributes(G, 'pos')

# Calculate depth steps for each node
depth_steps = []
calculate_depth(root, depth_steps)

# Animate depth calculation
animate_depth_calculation(G, pos, depth_steps)

print("Depth calculation animation saved as GIF.")
