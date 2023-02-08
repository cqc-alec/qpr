import graphviz as gv

c_col = "black"
q_col = "blue"
n_col = "grey"

init_attrs = {"shape": "diamond", "style": "filled", "fillcolor": "orange"}
fin_attrs = {
    "label": "",
    "shape": "diamond",
    "style": "filled",
    "fillcolor": "orangered",
}
decision_attrs = {"shape": "hexagon", "color": "green", "penwidth": "3"}
choice_attrs = {"label": "", "shape": "point", "height": "0.2", "color": "green"}
fn_attrs = {"shape": "ellipse", "fontcolor": "darkorange4"}

G = gv.Digraph("write2")

G.node("init", label="main", **init_attrs)
G.node("fin", **fin_attrs)
G.node("q0_alloc", label="", shape="circle")
G.node("q1_alloc", label="", shape="circle")
G.node("Rx_q0", label="Rx(1/4)", shape="rect")
G.node("Rx_q1", label="Rx(1/2)", shape="rect")
G.edge("q0_alloc", "Rx_q0", color=q_col)
G.edge("q1_alloc", "Rx_q1", color=q_col)
G.node("M_q0", label="M", shape="rect")
G.node("M_q1", label="M", shape="rect")
G.edge("Rx_q0", "M_q0", color=q_col)
G.edge("Rx_q1", "M_q1", color=q_col)
G.node("q0_free", label="", shape="circle")
G.node("q1_free", label="", shape="circle")
G.edge("M_q0", "q0_free", color=q_col)
G.edge("M_q1", "q1_free", color=q_col)
G.node("write0", label="(w)", **fn_attrs)
G.node("write1", label="(w)", **fn_attrs)
G.edge("M_q0", "write0", color=c_col)
G.edge("M_q1", "write1", color=c_col)
G.edge("init", "write0", color=n_col)
G.edge("init", "write1", color=n_col)
G.edge("write0", "fin", color=n_col)
G.edge("write1", "fin", color=n_col)

G.render(format="svg")
