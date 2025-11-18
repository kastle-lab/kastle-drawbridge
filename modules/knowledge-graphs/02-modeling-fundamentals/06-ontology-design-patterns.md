# Ontology Design Patterns

## Definition

`Ontology Design Patterns` (ODPs) are small, self-contained ontologies that aim to address general problems in ontology design. They can also be described as a collection of semantic patterns that provide a generic construct for ontology development. An ODP forms a small component or module of a complete ontology. Additionally, they facilitate the reuse of established design patterns, which can be tailored into a more specific module for a use case, streamlining the ontology building process.

## Background

ODPs were introduced by [Gangemi](https://scholar.google.com/citations?hl=en&user=-iVGcoAAAAAJ), [Blomqvist](https://scholar.google.com/citations?hl=en&user=4ftCkeQAAAAJ), and [Sandkuhl](https://scholar.google.com/citations?hl=en&user=5MxuPr4AAAAJ) in 2005 to simplify the ontology development process. A primary motivator for the inception of ODPs is to provide ontology engineers with small, reusable OWL ontologies that can be integrated into their larger constituents to solve specific modeling challenges. Since then, pattern-based design has become a state-of-the-art (SOTA) standard practice in ontology engineering, enabling modular design and encouraging the reuse of existing patterns. The reason is that ODPs have been shown to positively impact the quality of developed ontologies and to improve interoperability.

In summary, ODPs emerged as a critical tool for standardizing, simplifying, and improving the quality and reusability of ontologies. They provide a structured approach to addressing common modeling challenges in the development of knowledge graphs and other semantic applications.

## Related Papers

### [Patterns In Ontology Engineering: Classification of Ontology Patterns](#1-e-blomqvist-and-k-sandkuhl-patterns-in-ontology-engineering-classification-of-ontology-patterns)

**Authors:** Eva Blomqvist and Kurt Sandkuhl

> The paper's main contribution is the classification of ontology patterns, such as application, design, syntactic, etc. The authors discuss the considerations required to decide how to use these various pattern classifications (i.e., usage, construction, and ontology type).

### [Ontology Design Patterns\*](#2-a-gangemi-and-v-presutti-ontology-design-patterns)

**Authors:** Aldo Gangemi and Valentina Presutti

> The authors make the reader aware of the overlooked aspect of resusbility in ontology design. Notably, in the case of reusing core or reference ontologies that incorporate an enormous amount of knowledge representation, makes them cumbersome to use and understand. Due to this, the authors provide a description, an explanation, and an example use case for Content Ontology Design Patterns (CP). CPs are “…small ontologies that mediate between use cases (problem types) and design solutions that are used as modeling components: ideally, an ontology results from a composition of CPs, with appropriate dependencies between them, plus the necessary design expansion based on specific needs.”

### [Ontology Design Patterns in WebProtégé](#3-k-hammar-ontology-design-patterns-in-webprotégé)

**Authors:** Karl Hammar

> This paper provides and demonstrates a new extension (at the time) to the WebProtege ontology engineering environment for finding, specialising, and integrating ODPs.

### [How to Document Ontology Design Patterns](#4-none-karima-nazifa-n-h-karl-and-n-h-pascal-how-to-document-ontology-design-patterns)

**Authors:** Nazifa Karima, Karl Hammar and Pascal Hitzler

> The authors highlight various obstacles to implementing ODPs and focus specifically on documentation. In their paper, they present data from a survey they conducted, ranking the importance of 10 components of the documentation aspect of ODPs. From this, they highlighted the importance of various documentation components from a user's perspective and demonstrated other issues, such as the non-uniformity or inclusion of diagrams, the highest ranked required documentation component. In summary, the most significant components are: graphical illustrations (diagrams), example instantiations, and competency questions.

### [MODL: A Modular Ontology Design Library\*](#5-c-shimizu-q-hirt-and-p-hitzler-modl-a-modular-ontology-design-library)

**Authors:** Cogan Shimizu, Quinn Hirt, and Pascal Hitzler

> MODL is a collection of well-documented ontology design patterns, drawn from a wide variety of interdisciplinary use-cases. It is presented as a resource where the authors discuss its use and provide some examples of its contents. Additionally, MODL facilitates the searchability and accessibility of their ODPs, promoting reuse.

### [The Landscape of Ontology Reuse Approaches: Studies on the semantic web](#6-v-a-carriero-et-al-the-landscape-of-ontology-reuse-approaches-studies-on-the-semantic-web)

**Authors:** Valentina Anita Carriero, Marilena Daquino, Aldo Gangemi , Andrea Giovanni Nuzzolese , Silvio Peroni , Valentina Presutti , and Francesca Tomasi

> In this paper, the authors argue that at the time of publication, there were no effective solutions to support developers’ decision-making when choosing an ontology reuse (OR) strategy. Therefore, they propose various approaches for deciding when and how to use existing ontologies from authoritative organizations such as ISO and the W3C, as well as endorsed ontologies from such entities, or widely used ontologies outside these authoritative groups. The concepts highlighted for important consideration are ontology selection (OS), accessibility and preservation, integration, and reuse implementation.

### [OPLaX: annotating ontology design patterns at conceptual and instance level](#7-l-asprino-v-carriero-c-colonna-and-v-presutti-oplax-annotating-ontology-design-patterns-at-conceptual-and-instance-level)

**Authors:** Luigi Asprino, Valentina Anita Carriero , Christian Colonna , and Valentina Presutt

> The authors introduce a language for annotating ontology design patterns (ODPs) in ontologies and knowledge graphs at three distinct levels: as implemented in an ontology, the abstract conceptual component that can be implemented by different ODPs, and at the instance of a pattern in a knowledge graph.

### [Modular ontology modeling\*](#8-kirrane-s-ngonga-ngomo-a-c-shimizu-c-hammar-k-hitzler-p-modular-ontology-modeling)

**Authors:** Cogan Shimizu, Karl Hammar, and Pascal Hitzler

> The authors of MOMo identify a few issues which make ontology reuse difficult or challenging. Therefore they introduce a unique methodology that provides a systematic approach for developing robust and reusable ontologies designed to function as a schema for a KG. This approach is designed to address limitations in utilizing monolithic ontologies, as they are often difficult to reuse due to either strong ontological commitments that result in overspecification or weak commitments that cause ambiguity.

### [Neuro-symbolic artificial intelligence: The state of the art](#9-hitzler-p-and-sarker-mk-eds-2022-neuro-symbolic-artificial-intelligence-the-state-of-the-art)

**Editors:** Pascal Hitzler, Md Kamruzzaman Sarker

> This book is an amalgamation of relatively recent research papers that showcase state-of-the-art (SOTA) methods for neurosymbolic systems that combine logic, machine learning, and automated reasoning.

### [Empirical ontology design patterns and shapes from Wikidata](#10-v-a-carriero-p-groth-and-v-presutti-empirical-ontology-design-patterns-and-shapes-from-wikidata)

**Authors:** Valentina Anita Carriero, , Paul Groth, Paul Groth

> This paper introduces a method for extracting empirical ontology design patterns (EODPs) from knowledge graphs (KGs) that lack formal ontologies, such as Wikidata. The method addresses the challenge of reusing Wikidata's ontology, which is defined bottom-up, partially implicit, and constantly evolving. By identifying EODPs as sets of axioms/constraints with associated probability values based on their actual usage in the KG, the research aims to make the implicit ontology emerge and provide guidance for its use and potential improvement. The authors extend previous work by transforming frequent domain-property-range triplets into probabilistic OWL ontology design patterns (using RDF-star) and probabilistic ShEx shapes (a schema language used to formalize shapes), and by defining probabilistic patterns based on a frequentist interpretation.

### [Commonsense Ontology Micropatterns](#11-eells-a-dave-b-hitzler-p-shimizu-c-2024-commonsense-ontology-micropatterns)

**Authors:** Andrew Eells, Brandon Dave, Pascal Hitzler, Cogan Shimizu

> This paper's primary contribution is the creation of a comprehensive collection of 104 commonsense ontology micropatterns, organized into a fully annotated Modular Ontology Design Library (MODL) called CS-MODL. These micropatterns, representing frequently occurring nouns, were curated from common-sense knowledge extracted from Large Language Models (LLMs). The CS-MODL is designed to support the Modular Ontology Modeling (MOMO) methodology, aiming to accelerate ontology development for both human and automated processes. By providing a ready-to-use library of such patterns, the research addresses a major bottleneck in the large-scale deployment of MOMO, which previously faced limited availability of ready-to-use ontology design patterns. This resource is programmatically queryable and can facilitate the construction of internal knowledge frameworks for automated systems.

## Current Usage

### MOMo

---

#### Schema Diagrams

#### ODPs

### Oplax

---

### Patterns + Nesi -> accel LLMs4kgoe

---

### CSMODL

---

> Describe current applied in various systems, domains, or projects. Include human-centered perspectives and discuss future perspectives focused on automation of the process.

- **Momo** — _human aspect / description_
- **Oplax** — _human aspect / description_
- **patterns + nesi → accel LLMs4kgoe** — _describe this combination or workflow_
- **CSMODL** — _explain its role or integration_

### Examples

> Provide one or more examples illustrating how this pattern is used in practice.  
> Include ontology snippets, diagrams, or RDF/Turtle examples as appropriate.

### Example: Modl

**Description:**

> Explain what this example demonstrates.

**Code Example:**

> If any

## References

#### [1] E. Blomqvist and K. Sandkuhl [Patterns In Ontology Engineering: Classification of Ontology Patterns](https://www.scitepress.org/Papers/2005/25188/.)

#### [2] A. Gangemi and V. Presutti, [Ontology Design Patterns](https://www.researchgate.net/profile/Aldo-Gangemi/publication/227215903_Ontology_Design_Patterns/links/00b7d5152eea4d92eb000000/Ontology-Design-Patterns.pdf)

#### [3] K. Hammar, [Ontology Design Patterns in WebProtégé](https://www.diva-portal.org/smash/get/diva2:877199/FULLTEXT01.pdf)

#### [4] Karima Nazifa, N. H. Karl, and N. H. Pascal, [How to Document Ontology Design Patterns](https://ebooks.iospress.nl/publication/48704)

#### [5] C. Shimizu, Q. Hirt, and P. Hitzler, [MODL: A Modular Ontology Design Library](https://arxiv.org/pdf/1904.05405v1)

#### [6] V. A. Carriero et al., [The Landscape of Ontology Reuse Approaches: Studies on the semantic web](https://arxiv.org/pdf/2011.12599)

#### [7] L. Asprino, V. Carriero, C. Colonna, and V. Presutti, [OPLaX: annotating ontology design patterns at conceptual and instance level](https://cris.unibo.it/bitstream/11585/844294/2/paper1.pdf)

#### [8] Kirrane S, Ngonga Ngomo A-C, Shimizu C, Hammar K, Hitzler P. [Modular ontology modeling](https://journals.sagepub.com/doi/full/10.3233/SW-222886)

#### [9] Hitzler, P. and Sarker, M.K. eds., 2022. [Neuro-symbolic artificial intelligence: The state of the art](https://books.google.com/books?hl=en&lr=&id=uFtcEAAAQBAJ&oi=fnd&pg=PR1&dq=%7BNeuro-symbolic+artificial+intelligence:+The+state+of+the+art&ots=s8Lv2HvFZ9&sig=6Y4r3w50HYrAHD2PCpvV6-Ha_DE#v=onepage&q=%7BNeuro-symbolic%20artificial%20intelligence%3A%20The%20state%20of%20the%20art&f=false)

#### [10] V. A. Carriero, P. Groth, and V. Presutti, [Empirical ontology design patterns and shapes from Wikidata](https://journals.sagepub.com/doi/full/10.3233/SW-243613)

#### [11] Eells, A., Dave, B., Hitzler, P., Shimizu, C. (2024). [Commonsense Ontology Micropatterns](https://link.springer.com/chapter/10.1007/978-3-031-71170-1_6)
