# Schema Diagrams

Schema diagrams serve as graphical representations of ontologies. Due to simplicity being a desirable characteristic of them to facilitate ease of viewing, however, they can be incomplete and ambiguous, lacking the stricter semantics established through the use of axioms. Nonetheless, they provide an easily understandable means of introducing the higher-level concepts of an ontology.

We use [yEd](https://www.yworks.com/products/yed) to construct these schema diagrams. In the remainder of this section, we provide a tutorial on the construction of schema diagrams using yEd and discuss the visual standards to be adhered to during this process. The `AgeRecord` diagram, depicted below, illustrates a simple schema diagram with many syntactic components that are detailed below.

![AgeRecord](schema-diagrams/AgeRecord.png)

## Node Types

For all nodes, the size is not set but allowed to automatically adjust as needed depending on the size of it label.

### Class

A class is illustrated via a "Rounded Rectangle" node with a solid frame ("Line Type" set to the second solid frame option) and orange (#ffcc00) fill color. The label for this node is formatted in PascalCase.

![AgeRecord Node](schema-diagrams/AgeRecordNode.png)

### Module

A module is a single node that indicates a level of hidden complexity. That is, there is a complex model that would actually take the place of the single node but is not fully depicted to emphasize only what is essential to the diagram currently being viewed. This full model would be depicted in its entirety elsewhere. A module is illustrated via a "Rounded Rectangle" node with a dashed frame ("Line Type" set to the second dashed frame option) and blue (#ccffff) fill color. The label for this node is formatted in PascalCase.

![PersonRecord Node](schema-diagrams/PersonRecordNode.png)

The `PeronRecord` module is expanded below as a sub-module of `AgentRecord`.

![AgentRecord](schema-diagrams/AgentRecord.png)

### Controlled Vocabulary

A controlled vocabulary is a set of pre-defined URIs with a specific meaning that is documented externally. It is illustrated via a "Rounded Rectangle" node with a dashed frame ("Line Type" set to the second dashed frame option) and purple (#cc99ff) fill color. The label for this node is formatted in PascalCase.

![AgeCategory.txt Node](schema-diagrams/AgeCategoryNode.png)

### Datatype

A datatype node represents one of the concrete datatypes allowed in OWL. It is illustrated via an "Ellipse" node with a solid frame ("Line Type" set to the second solid frame option) and yellow (#ffff99) fill color. The label for this node is formatted as dictated by OWL. [Protégé](https://protege.stanford.edu) is a useful tool for viewing datatypes in addition to providing other capabilities.

![xsd:double Node](schema-diagrams/xsddoubleNode.png)

## Edge Types

All edges are given "Smooth Bends" (toggle at the very bottom in the "Bends" section when an arrow is clicked).

### Subclass

A subclass relationship is illustrated via an arrow with a white head ("Target Arrow" set to the fourth option) and no label.

![AgeRecord subclassOf PersonRecord](schema-diagrams/AgeRecord-subclass-PersonRecord.png)

### Data Property or Object Property

A data property or object property (distinguished from one another based on the target of an edge) is illustrated via an arrow with a solid tip ("Target Arrow" set to the second option) and a label. The text for edge labels is formatted in camelCase. The "Background" for edge labels is adjusted to be white (#ffffff) or another color to match the background (this is especially common when "Group Nodes" are used).

The `hasAgeValue` relationship acts as a data property in this diagram.

![AgeRecord hasAgeValue xsd:double](schema-diagrams/AgeRecord-hasAgeValue-xsddouble.png)

The `hasAgeCategory` relationship acts as an object property in this diagram.

![AgeRecord hasAgeCategory AgeCategory.txt](schema-diagrams/AgeRecord-hasAgeCategory-AgeCategory.png)
