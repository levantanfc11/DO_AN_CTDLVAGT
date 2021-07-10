#!/usr/bin/env python
# coding: utf-8

# In[5]:


import networkx as nx
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15,9))
G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'), ('B', 'D'), ('B', 'C'),('C', 'D')])
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = "red", node_size = 2500)
nx.draw_networkx_labels(G, pos, font_size=30)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True, min_target_margin = 30)
plt.show()


# In[ ]:




