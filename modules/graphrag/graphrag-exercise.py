"""GraphRAG retrieval exercise: question -> seed entity -> k-hop subgraph -> prompt context.

Runs on CPU with only RDFLib. Uses the Drawbridge animal example KG.

    python graphrag-exercise.py --hops 1
    python graphrag-exercise.py --hops 2
    python graphrag-exercise.py "Who does Butch chase?" --hops 2
"""
import argparse
import re
from pathlib import Path

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import OWL, RDF

TTL = Path(__file__).resolve().parent.parent / "knowledge-graphs" / "Supplementary-material" / "AnimalExample.ttl"
EX = Namespace("http://www.kastledrawbridge.org/animals/")

# Every triple touching a node, in either direction.
NEIGHBORS = "SELECT ?s ?p ?o WHERE { { ?n ?p ?o BIND(?n AS ?s) } UNION { ?s ?p ?n BIND(?n AS ?o) } }"
EXAMPLE = "Which animal chases the cat that chases Jerry?"


def local(term):
    return re.split(r"[/#]", str(term))[-1]


def label(g, node):
    name = g.value(node, EX.hasName)
    return f"{name} ({local(node)})" if name else local(node)


def link_entities(g, question):
    """Lexical entity linking: match words in the question against hasName labels."""
    words = set(re.findall(r"\w+", question.lower()))
    return [s for s, name in g.subject_objects(EX.hasName) if str(name).lower() in words]


def expand(g, seeds, hops):
    """Collect the k-hop neighborhood of the seed entities with SPARQL."""
    triples, frontier, seen = set(), set(seeds), set(seeds)
    for _ in range(hops):
        next_frontier = set()
        for n in frontier:
            for s, p, o in g.query(NEIGHBORS, initBindings={"n": n}):
                if o == OWL.NamedIndividual or p == EX.hasName:
                    continue  # schema noise; names are already shown in labels
                triples.add((s, p, o))
                if p != RDF.type:  # do not walk through class nodes
                    next_frontier.update(x for x in (s, o) if isinstance(x, URIRef))
        frontier = next_frontier - seen
        seen |= frontier
    return sorted(triples)


def verbalize(g, triples):
    return [f"{label(g, s)} {local(p)} {label(g, o)}." for s, p, o in triples]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question", nargs="?", default=EXAMPLE)
    ap.add_argument("--hops", type=int, default=1)
    args = ap.parse_args()

    g = Graph().parse(TTL, format="turtle")
    seeds = link_entities(g, args.question)
    print("Seed entities:", [label(g, s) for s in seeds])

    facts = verbalize(g, expand(g, seeds, args.hops))
    context = "\n".join(f"- {f}" for f in facts)
    print(f"\n--- Prompt ({args.hops}-hop context, {len(facts)} facts) ---")
    print("Answer using only the facts below. If they are not enough, say so.\n")
    print(f"Facts:\n{context}\n\nQuestion: {args.question}")

    if args.question == EXAMPLE:
        # Ground truth: the SPARQL query an LLM would need to write for the example question.
        answer = g.query(
            "SELECT ?name WHERE { ?x :chases ?cat . ?cat a :Cat ; :chases ?m . ?m :hasName 'Jerry' . ?x :hasName ?name }",
            initNs={"": EX},
        )
        print("\nSPARQL ground truth:", [str(r.name) for r in answer])


if __name__ == "__main__":
    main()
