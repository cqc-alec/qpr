import graphviz as gv
from fdgraph import c_col, init_attrs, fin_attrs, decision_attrs, choice_attrs

G = gv.Digraph("race")

G.node("init", label="", **init_attrs)
G.node("fin", **fin_attrs)

G.node("J0", label="A", shape="rect")
G.node("J1", label="B", shape="rect")

G.edge("init", "J0", label="a", color=c_col)
G.edge("init", "J1", label="b", color=c_col)

G.node("join", label="", shape="point")

G.edge("J0", "join", label="c", color=c_col)
G.edge("J1", "join", label="c", color=c_col)

G.edge("join", "fin", label="c", color=c_col)

G.render(format="svg")
