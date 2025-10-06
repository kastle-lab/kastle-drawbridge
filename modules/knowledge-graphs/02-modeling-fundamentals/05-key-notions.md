# Key Notions

### Definition

`Key notions` can be thought of as the fundamental ideas that establish the purpose of a Knowledge Graph (KG) [[1]](https://www.sciencedirect.com/science/article/pii/S1570826824000283). Concepts that overlap within the `competency questions` and/or the frequency with which those concepts relate to other ideas within the data, determine the key notions [[2]](https://people.cs.ksu.edu/~hitzler//pub2/2020-mom-tutorial.pdf), [[3]](https://journals.sagepub.com/doi/10.3233/SW-222886). The process for determining the key notions is bidirectional, meaning that as more data is collected or more competency questions are modified, key notions could be added or removed. These core concepts are the foundation and guide for the KG modeling process when designing [ontological](../02-modeling-fundamentals/02-ontology.md) patterns and `modules` [[1]](https://people.cs.ksu.edu/~hitzler//pub2/2020-mom-tutorial.pdf).

### Example

As an example, we will explore the example given in section three of the "Modular Ontology Modeling: A Tutorial" paper [[2]](https://people.cs.ksu.edu/~hitzler//pub2/2020-mom-tutorial.pdf).

Let's assume we want to build a Knowledge Graph that incorporates recipes from the various popular recipe sites across the Web, and we have established the following `competency questions` for our use case:

```
1. How do I make chili with red beans?
2. What are some sweet breakfast items under 100 calories?
3. What minimal meals can I cook in under 30 minutes?
```

From these questions and the analysis of recipes from data sources, we can likely conceive of the following as `key notions`:

```
- RecipeName
- RecipeInstructions
- FoodType
- QuantityOfFood
- TimeInterval
```

These are just a few potential key notions, but choosing the above makes sense as recipes typically have a name, include instructions for prepping and cooking, define the food type, include serving quantities and the number of ingredients, and have cooking times. From here, further analysis of these `key notions` is required when trying to instate these `key notions` and create `modules`.

# Resources

1. [The KWG Ontology](https://www.sciencedirect.com/science/article/pii/S1570826824000283) - Section 3.1.3

2. [Modular Ontology Modeling: A Tutorial](https://people.cs.ksu.edu/~hitzler//pub2/2020-mom-tutorial.pdf) - Section 3, Step 3.

3. [Modular Ontology Modeling](https://journals.sagepub.com/doi/10.3233/SW-222886) - Section 3.6.3
