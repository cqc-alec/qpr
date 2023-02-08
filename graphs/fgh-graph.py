import graphviz as gv
from fdgraph import q_col, init_attrs, fin_attrs, fn_attrs

G = gv.Digraph("fgh")

G.node("init", label="main", **init_attrs)
G.node("f", label="(f)", **fn_attrs)
G.node("g", label="(g)", **fn_attrs)
G.node("h", label="(h)", **fn_attrs)
G.node("fin", **fin_attrs)
G.edge("init", "f", label="q", color=q_col)
G.edge("init", "f", color=q_col)
G.edge("f", "g", label="q", color=q_col)
G.edge("init", "g", color=q_col)
G.edge("g", "h", label="q", color=q_col)
G.edge("init", "h", color=q_col)
G.edge("h", "fin", color=q_col)
G.edge("f", "fin", color=q_col)
G.edge("g", "fin", color=q_col)
G.edge("h", "fin", color=q_col)

G.render(format="svg")
