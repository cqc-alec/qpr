from dataclasses import dataclass
import graphviz as gv
import networkx as nx

edge_types = {"Bit", "u32", "Qubit"}


@dataclass
class Sig:
    in_types: dict[str, str]
    out_types: dict[str, str]


fn_types = {
    "H_gate": Sig({"q": "Qubit"}, {"q": "Qubit"}),
    "CX_gate": Sig({"ctl": "Qubit", "tgt": "Qubit"}, {"ctl": "Qubit", "tgt": "Qubit"}),
}


class QFn:
    def __init__(self, name, sig):
        self.name = name
        self.sig = sig
        self.G = nx.MultiDiGraph()
        self.G.add_node("init", label="")
        self.G.add_node("fin", label="")

    def add_node(self, name, fnid, label=""):
        self.G.add_node(name, fnid=fnid, label=label)

    def add_edge(self, src, src_port, tgt, tgt_port):
        if src == "init":
            raise ValueError("Please use `add_init_edge`")
        if tgt == "fin":
            raise ValueError("Please use `add_final_edge`")
        src_fnid = self.G.nodes[src]["fnid"]
        tgt_fnid = self.G.nodes[tgt]["fnid"]
        src_datatype = fn_types[src_fnid].out_types[src_port]
        tgt_datatype = fn_types[tgt_fnid].in_types[tgt_port]
        if src_datatype != tgt_datatype:
            raise ValueError(f"Type mismatch: {src_datatype} != {tgt_datatype}")
        datatype = src_datatype
        self.G.add_edge(
            src, tgt, src_port=src_port, tgt_port=tgt_port, datatype=datatype
        )

    def add_init_edge(self, src_port, tgt, tgt_port):
        src_datatype = self.sig.in_types[src_port]
        tgt_fnid = self.G.nodes[tgt]["fnid"]
        tgt_datatype = fn_types[tgt_fnid].in_types[tgt_port]
        if src_datatype != tgt_datatype:
            raise ValueError(f"Type mismatch: {src_datatype} != {tgt_datatype}")
        datatype = src_datatype
        self.G.add_edge(
            "init", tgt, src_port=src_port, tgt_port=tgt_port, datatype=datatype
        )

    def add_final_edge(self, src, src_port, tgt_port):
        tgt_datatype = self.sig.out_types[tgt_port]
        src_fnid = self.G.nodes[src]["fnid"]
        src_datatype = fn_types[src_fnid].out_types[src_port]
        if src_datatype != tgt_datatype:
            raise ValueError(f"Type mismatch: {src_datatype} != {tgt_datatype}")
        datatype = src_datatype
        self.G.add_edge(
            src, "fin", src_port=src_port, tgt_port=tgt_port, datatype=datatype
        )

    def save_image(self):
        G = gv.Digraph(self.name)
        for n in self.G.nodes:
            G.node(str(n), label=self.G.nodes[n]["label"])
        for e in self.G.edges:
            G.edge(str(e[0]), str(e[1]))
        G.render(format="svg")


def test():
    f = QFn("bell", Sig({"q0": "Qubit", "q1": "Qubit"}, {"q0": "Qubit", "q1": "Qubit"}))
    f.add_node("H", "H_gate", label="H")
    f.add_node("CX", "CX_gate", label="CX")
    f.add_init_edge("q0", "H", "q")
    f.add_edge("H", "q", "CX", "ctl")
    f.add_init_edge("q1", "CX", "tgt")
    f.add_final_edge("CX", "ctl", "q0")
    f.add_final_edge("CX", "tgt", "q1")
    f.save_image()
