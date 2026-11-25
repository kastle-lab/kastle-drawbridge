# GraphRAG Learning Path

This learning path is for a graduate research assistant who wants to work on GraphRAG systems, i.e. systems that combine knowledge graphs (KGs) with large language models (LLMs) so that generated answers are grounded in structured, queryable knowledge.

The path has three parts, following [issue #55](https://github.com/kastle-lab/kastle-drawbridge/issues/55):

1. **Symbolic Components**: knowledge representation with RDF, OWL, and SPARQL. These are already covered by the Drawbridge [Knowledge Graphs](../knowledge-graphs/README.md) module, so this path points to those lessons.
2. **Neural Components**: how LLMs generate text, how embeddings support semantic search, and how retrieval-augmented generation (RAG) works.
3. **Neural-symbolic Integration**: using LLMs to populate, query, and reason over KGs, and building prompts that use graph context.

---

## How to Use This Resource

1. **Complete the prerequisites** - The [Foundation](../foundation/README.md) module (Python basics) is assumed.
2. **Follow the sections in order** - Section 3 assumes you can write SPARQL and know what an embedding is.
3. **Read the primary sources** - Each topic lists the paper that introduced the idea. Read the abstract and introduction first; go deeper when a topic matters for your research.
4. **Do the hands-on exercise** - It runs locally on a CPU and only needs `rdflib`. No paid APIs are required.
5. **Ask questions** - Bring them to weekly lab syncs.

---

## Section 1: Symbolic Components

Work through these existing Drawbridge lessons. If you already know a topic, do its assignment as a self-check and move on.

| Topic | Drawbridge lessons |
| --- | --- |
| KGs: building | [Graphs](../knowledge-graphs/01-graphs/01-graphs.md), [Graphs in Turtle](../knowledge-graphs/01-graphs/02-graphs-ttl.md) |
| KGs: querying | [SPARQL](../knowledge-graphs/03-modeling-technologies/04-sparql.md), [SPARQL Tutorial](../knowledge-graphs/03-modeling-technologies/05-sparql-tutorial.md), [Querying Methods](../knowledge-graphs/03-modeling-technologies/06-querying-methods.md) |
| KGs: populating | [Materialization](../knowledge-graphs/03-modeling-technologies/07-materialization.md) |
| KGs: reasoning | [Axioms](../knowledge-graphs/02-modeling-fundamentals/03-Axioms.md) |
| Ontology | [Modeling Fundamentals](../knowledge-graphs/02-modeling-fundamentals/01-modeling-fundamentals.md), [Ontology](../knowledge-graphs/02-modeling-fundamentals/02-ontology.md), [Ontology Design Patterns](../knowledge-graphs/02-modeling-fundamentals/06-ontology-design-patterns.md) |
| RDF | [Graphs in Turtle](../knowledge-graphs/01-graphs/02-graphs-ttl.md) |
| OWL | [Axioms](../knowledge-graphs/02-modeling-fundamentals/03-Axioms.md), [Protégé](../knowledge-graphs/03-modeling-technologies/03-protege.md) |
| SPARQL | [SPARQL](../knowledge-graphs/03-modeling-technologies/04-sparql.md), [SPARQL Tutorial](../knowledge-graphs/03-modeling-technologies/05-sparql-tutorial.md) |
| Schemas | [Schema Diagrams](../knowledge-graphs/03-modeling-technologies/02-schema-diagrams.md), [Key Notions](../knowledge-graphs/02-modeling-fundamentals/05-key-notions.md) |
| Axioms | [Axioms](../knowledge-graphs/02-modeling-fundamentals/03-Axioms.md), [Axiom Assignment](../knowledge-graphs/Supplementary-material/Assignments/Axiom-assign.md) |

Also complete [Competency Questions](../knowledge-graphs/02-modeling-fundamentals/04-Competency-Question.md). Competency questions are the natural-language questions a KG must answer, which makes them the test set of a GraphRAG system.

---

## Section 2: Neural Components

### LLMs: Generation

**Overview**:
An LLM is a Transformer network trained to predict the next token given the tokens before it. At inference time it generates text one token at a time, conditioned on everything in its context window (the prompt). It has no built-in way to check facts, so when the prompt lacks the needed knowledge it can produce fluent but wrong answers (hallucinations). RAG and GraphRAG address this by putting the right knowledge into the prompt.

**What You'll Learn**:

- How the Transformer architecture processes a sequence with attention
- What a context window is and why its size limits how much knowledge you can pass in
- Why grounding the prompt in retrieved knowledge reduces hallucination

**Primary sources**:

- Vaswani et al., 2017. [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
- Jurafsky and Martin. [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) (free textbook draft; see the chapters on Transformers and large language models).

### LLMs: Search Using Embeddings

**Overview**:
An embedding model maps a piece of text to a vector so that texts with similar meaning end up close together (for example, by cosine similarity). Semantic search embeds the question and every candidate passage, then returns the nearest passages. This is the retrieval step of standard (vector) RAG, and in GraphRAG it is often used to find the KG entities a question refers to (entity linking).

**What You'll Learn**:

- What a sentence embedding is and how cosine similarity ranks results
- The difference between lexical (keyword) and semantic (embedding) matching
- Where embeddings fit in a retrieval pipeline

**Primary sources**:

- Reimers and Gurevych, 2019. [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084).
- [Sentence Transformers documentation](https://www.sbert.net/) (open-source library with small models that run on a CPU).

### LLMs: RAG

**Overview**:
Retrieval-augmented generation retrieves documents relevant to a question and adds them to the prompt before the LLM answers. Plain RAG retrieves text chunks independently, so it struggles when the answer requires connecting facts spread across several chunks (multi-hop questions) or summarizing a whole corpus. Those two weaknesses are the main motivation for GraphRAG.

**What You'll Learn**:

- The retrieve-then-generate pipeline
- Common RAG variants and how they are evaluated
- The failure modes of chunk-based retrieval

**Primary sources**:

- Lewis et al., 2020. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401).
- Gao et al., 2023. [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997).

---

## Section 3: Neural-symbolic Integration

Start with the two surveys below to get a map of the field, then work through the topics.

- Pan et al., 2023. [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302).
- Peng et al., 2024. [Graph Retrieval-Augmented Generation: A Survey](https://arxiv.org/abs/2408.08921).

### LLM Population of KGs

**Overview**:
Many GraphRAG systems use an LLM to extract entities and relations from text and build the graph automatically. Microsoft's GraphRAG builds an entity graph, groups it into communities, and pre-writes a summary for each community so it can answer questions about a whole corpus. LightRAG uses a lighter graph index with retrieval at two levels (specific entities and broader themes). HippoRAG extracts triples with open information extraction and stores them as a graph for later retrieval. Note that these graphs are usually schema-light, unlike the ontology-driven KGs built in Section 1; how much the schema matters is an open research question (see Section 4).

**What You'll Learn**:

- How an LLM turns text into triples and where extraction errors come from
- How graph indexes (communities, entity and theme levels) support different question types
- The trade-off between automatically extracted graphs and curated, ontology-based KGs

**Primary sources**:

- Edge et al., 2024. [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130). Code: [microsoft/graphrag](https://github.com/microsoft/graphrag).
- Guo et al., 2024. [LightRAG: Simple and Fast Retrieval-Augmented Generation](https://arxiv.org/abs/2410.05779). Code: [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG).
- Gutiérrez et al., 2024. [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831). Code: [OSU-NLP-Group/HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG).

### LLM Querying over KGs

**Overview**:
When a curated KG already exists, the LLM can query it instead of reading text. The two common patterns are (1) text-to-SPARQL, where the LLM writes a query that a triplestore executes, and (2) subgraph retrieval, where the system finds the entities in the question, pulls their neighborhood from the KG, and passes those triples to the LLM as context. Text-to-SPARQL gives exact answers but fails if the LLM misunderstands the schema; subgraph retrieval is more forgiving but can retrieve too little or too much.

**What You'll Learn**:

- How to give an LLM enough schema information to write correct SPARQL
- How entity linking and k-hop neighborhood retrieval work
- How to turn triples into text an LLM can read (verbalization)

**Primary sources**:

- Pan et al., 2023 and Peng et al., 2024 (surveys above) give an overview of both patterns.
- Jaldi et al., 2025. [Knowledge Conceptualization Impacts RAG Efficacy](https://arxiv.org/abs/2507.09389). KASTLE Lab work on how the structure and complexity of a KG's conceptualization affect an LLM agent querying a triplestore.

### LLM Reasoning over KGs

**Overview**:
Multi-hop questions need the system to follow a chain of relations. Think-on-Graph lets the LLM explore the KG step by step, choosing which relations to follow at each hop. HippoRAG instead runs Personalized PageRank from the question's entities so that relevant multi-hop facts are scored highly in one retrieval step. In both cases the graph structure, not the LLM's memory, supplies the chain of facts, which also makes the answer easier to explain.

**What You'll Learn**:

- Why multi-hop questions are hard for chunk-based RAG
- Iterative (agent-style) versus single-step graph traversal
- How a reasoning path over the KG can serve as an explanation

**Primary sources**:

- Sun et al., 2023. [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://arxiv.org/abs/2307.07697).
- Gutiérrez et al., 2024. HippoRAG (above).

### Prompting with Graph Context

**Overview**:
The retrieved subgraph only helps if the prompt presents it clearly. Good practice: verbalize each triple as a short sentence using human-readable labels, keep the context limited to what the question needs, tell the model to answer only from the given facts and to say when the facts are insufficient, and ask it to cite the facts it used. The `prompts/` folders in the KASTLE research repositories in Section 4 show prompt templates used in lab experiments.

**What You'll Learn**:

- How to verbalize triples and labels
- How to write grounding instructions that reduce hallucination
- How to inspect a prompt to see whether it contains the facts needed to answer

**Hands-on Exercise:**

- [graphrag-exercise.py](graphrag-exercise.py) runs a minimal GraphRAG retrieval pipeline over the Drawbridge [Animal Example](../knowledge-graphs/Supplementary-material/AnimalExample.ttl) KG: it links the question to a seed entity, pulls the k-hop neighborhood with SPARQL, verbalizes the triples, and prints the prompt an LLM would receive. For the example question (the default when no question is given), it also prints the answer from a hand-written SPARQL query as ground truth.
- Setup: `pip install rdflib`, then from this folder run:

```bash
python graphrag-exercise.py --hops 1
python graphrag-exercise.py --hops 2
python graphrag-exercise.py "Who does Butch chase?" --hops 2
```

- Tasks:
  1. Compare the two prompts. Which one contains the full chain of facts needed to answer? Spike appears in both prompts; explain why an LLM given the 1-hop prompt could still answer "Spike" for the wrong reason.
  2. Ask a question about Butch (`Cat2`). What does the retriever return, and what should a grounded LLM say?
  3. The entity linker only matches exact names. Replace it with embedding-based matching using Sentence Transformers and test it with a question that uses a nickname or a misspelling.
  4. Write the SPARQL query for "Who is Jerry's friend?" by hand. Then describe what schema information an LLM would need in its prompt to write the same query (text-to-SPARQL).
  5. Optional: paste a generated prompt into any locally hosted open-weight LLM and check whether its answer matches the SPARQL ground truth.
- _Goal:_ See how the amount of graph context changes whether a question is answerable, and connect the symbolic (SPARQL) and neural (prompt) ways of answering it.

---

## Section 4: KASTLE Lab GraphRAG Research

Once you have finished Sections 1 to 3, read the lab's own GraphRAG work. Each repository contains the data, prompts, scripts, and results of a study.

- [knowledge-conceptualization-graphrag](https://github.com/kastle-lab/knowledge-conceptualization-graphrag): data and code for *Knowledge Conceptualization Impacts RAG Efficacy*, using the Enslaved.org and KnowWhereGraph KGs.
- [structural-lexico-semantic-effects-graphrag](https://github.com/kastle-lab/structural-lexico-semantic-effects-graphrag): evaluation of query-based GraphRAG approaches.
- [kg-suitability-graphrag](https://github.com/kastle-lab/kg-suitability-graphrag): experiments on how schema representations affect selecting a KG from competency questions.
