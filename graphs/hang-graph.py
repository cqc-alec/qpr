import graphviz as gv
from fdgraph import c_col, init_attrs, fin_attrs, decision_attrs, choice_attrs

G = gv.Digraph("hang")

G.node("init", label="", **init_attrs)
G.node("fin", **fin_attrs)

G.node("D0", label="", **decision_attrs)
G.node("D1", label="", **decision_attrs)
G.node("C00", **choice_attrs)
G.node("C01", **choice_attrs)
G.node("C10", **choice_attrs)
G.node("C11", **choice_attrs)

G.edge("init", "D0", label="a", color=c_col)
G.edge("init", "D0", label="c", color=c_col)
G.edge("init", "D1", label="b", color=c_col)
G.edge("init", "D1", label="d", color=c_col)

G.edge("D0", "C00", label="a", color=c_col)
G.edge("D0", "C01", label="c", color=c_col)
G.edge("D1", "C10", label="b", color=c_col)
G.edge("D1", "C11", label="d", color=c_col)

G.node("J0", label="AB", shape="rect")
G.node("J1", label="CD", shape="rect")

G.edge("C00", "J0", label="a", color=c_col)
G.edge("C01", "J1", label="c", color=c_col)
G.edge("C10", "J0", label="b", color=c_col)
G.edge("C11", "J1", label="d", color=c_col)

G.node("join", label="", shape="point")

G.edge("J0", "join", label="e", color=c_col)
G.edge("J1", "join", label="e", color=c_col)

G.edge("join", "fin", label="e", color=c_col)

G.render(format="svg")
