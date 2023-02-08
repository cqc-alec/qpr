import graphviz as gv
from fdgraph import c_col, q_col, n_col, init_attrs, fin_attrs, fn_attrs

G = gv.Digraph("regalloc")

G.node("init1", label="", **init_attrs)
G.node("fin1", **fin_attrs)
G.node("alloc", label="q_reg_alloc(5)", shape="ellipse")
G.edge("init1", "alloc", color=n_col)
G.node("op1", label="", shape="rect")
G.edge("alloc", "op1", color=c_col)
G.node("f", label="(f)", **fn_attrs)
G.edge("op1", "f", color=c_col)
G.node("op2", label="", shape="rect")
G.edge("f", "op2", color=c_col)
G.edge("op2", "fin1", color=c_col)

G.node("init2", label="", **init_attrs)
G.node("fin2", **fin_attrs)
G.edge("init2", "access", label="i", color=c_col)
G.node("access", label="access", shape="rect")
G.edge("init2", "access", label="R", color=c_col)
G.node("access2", label="access", shape="rect")
G.edge("init2", "access2", label="j", color=c_col)
G.edge("access", "fin2", label="R[i]", color=q_col)
G.edge("access", "access2", label="R", color=c_col)
G.edge("access2", "fin2", label="R[j]", color=q_col)
G.edge("access2", "fin2", label="R", color=c_col)

G.render(format="svg")
