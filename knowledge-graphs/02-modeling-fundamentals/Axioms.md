# Welcome to ✨ Axioms ✨
## **What are Axioms and Why do we use them in Ontology?** 🤔
 Axioms are constraints that govern the relationships of things. These constraints allow us to formalize ontologies to ensure standardization, consistency, and buildability of our ontologies. You can think of them as blue prints for how to use and piece ontolgy together. Axioms act as staring points which other statements can logically derive through the rules of inference. It is important to understand the 2 types of logic that you will be exposed to in **KASTLE LAB**: <ins>*Descriptive Logic*</ins> and <ins>*Prediate Logic*</ins>

 - **Description Logic**: 
      - <ins>*Scientific Definition*</ins>: Description logics (DLs) are a family of knowledge representation languages that are widely used in ontological modelling [[1]](#1--krötzsch-m-simancik-f--horrocks-i-2012-a-description-logic-primer-arxiv-preprint-arxiv12014089). These are a family of knowledge representation languages whcih represent knowledge in a domain of interest using formal, logic based sematics [[2]](#2-krötzsch-m-rudolph-s--hitzler-p-2008-description-logic-rules-in-ecai-2008-pp-80-84-ios-press).  
     - <ins>*8th grade defintion*</ins>: Description Logics (DLs) are a type of language used to represent knowledge in a structured way. They help organize information about a topic using logic rules. 
     <!-- DLs use knowledge bases (KBs) to store general facts about categories of things (like animals, books, or cities) and specific facts about individual things and how they relate to each other. DLs come from earlier ideas like semantic networks and frame systems, which were used to model knowledge in a logical way. -->
      
      
<img align="left" src="/pngs/dog.png" width="200" height="300">

  
     Example: Describing Dogs 🐶 and Animals 

     - Identify your categories:
          + Animal = Representation of all animals 
          + Dog = Respresents all dogs 

     - Identify your relationships 
          + hasOwner = A dog can have an owner.
                
     - Identify Assertions:
          + Dog ⊑ Animal = every dog is an animal. 
           + ∃hasOwner.⊤ = Every dog  has atleast one owner.
                
     - Lets put it all in action:
          + Buddy: Dog = "Buddy" is a Dog.
          + hasOwner(Buddy, Alice)= Buddy has an owner:Alice.

<br> 

  - **Predicate logic** : 
    - <ins>*Scientific Defintion*</ins>: Predicate logic also known as <ins>First-Order Logic</ins> is a formal system that extends propositional logic by adding quanitifers and predicates. Statments can be made about objects in a domain and can involve variables that range over these objects. Predicate Logic allows expression such as "For All <ins>*x*</ins> which can be used to describe properties of objects or relations between those objects [[3]](#3enderton-h-b-2001-a-mathematical-introduction-to-logic-elsevier).
    - <ins> *8th Grade Defintion*</ins>: Predicate logic helps us make statements about things or objects. Instead of just saying whether something is true or false, predicate logic lets us talk about different things (like people, numbers, or objects) and their properties or how they are related to each other. 

<img align="left" src="/pngs/student_v2.png" width="200" height="300">

     Example: We want to make a Statement about a set of people using Predicate Logic 👩🏼‍🎓

     - lets identify our Predicate and Domain!
          + Predicate: "Is a student" = S (variable)
          + Domain: All people in a class


     - Lets structure the statment using Predicate Logic!
           ∀x S(x) = Everyone in the class is a student. 

                           OR

            ∃x S(x) = There is atleast one person in the
              class who is a student. 
        

      ** NOTE ** Dont worry about the symbols just yet, We will have a deeper dive into the symbols in this module!)



## **KASTLE's Hottest Axioms** 🥵🥵🥵
<!-- 
reference  why we use this ones! andrea sent the paper that i can reference for this.  -->
In the KASTLE lab we have specific axioms that you will continuously encounter thoughout your onotology development with us! In this section we break down the "*Hottest* 🥵" axioms you will need to know. There are 17 of these axioms but for this module we will only go through the most relavant. 

- All of the axioms are avaiabe in the **KASTLE Lab Axioms Presentation [[4]](#4-understanding-axioms-by-kastlelab)**, since we are not going over all of them it is your repsonsibility to go through and learn the rest, they might not be the most used axioms but they are still relevant and will come up periodically.
     -  You can access that presentation here ➡️ [Understanding Axioms](https://docs.google.com/presentation/d/1EmLxLo8yzo9-O6nKr7Yf6GRZdUXqe_VovG02JbTuh60/edit?usp=sharing) 

### <ins>Know you Symbols!</ins>
Before we dive into the "*Hottest* 🥵" axioms lets take a quick note the symbolic representations you will encounter when working with Axioms. 

!["list of logic symbols"](/pngs/AxiomUnderstanding.png)

In this Figure we demonstrate the symbols and their meaning that you will encounter thoughout this module and throughout your ontology career. 

- It is wise to become familar with these since this is what we use when writing these out in papers and repositories. 
- These are listed in the [Understanding Axioms](https://docs.google.com/presentation/d/1EmLxLo8yzo9-O6nKr7Yf6GRZdUXqe_VovG02JbTuh60/edit?usp=sharing) presentation as well as the Graphical notations and it is suggested that you look over these. 


### <ins>How to read these slides</ins>
!["How to read"](/pngs/how-to-read.png) 
Since we will be referencing the slides within the Understadning Axioms presentation it is imporant to understand how to read these slides in order to get the most out of these examples. In these slides you will be exposed to:

- Manchester Syntax 
- Predicate Logic Syntax
- Natural Language Translation


## Hottest Axioms in the KASTLE lab 🥵🥵🥵🥵

### Axiom 1: Subclass 🥵
In logic a <ins>**Subclass**</ins> is a smaller group within a larger group. Simply put everything in the subclass follows the rules of a bigger group but has additional traits that make it different. Here is a really simple example: 

          Example: Animals 
               + Animal = Main Class (A.K.A your big group fo things)
               + Mammals 🦁, Fish 🐠, Birds 🐦 = The subclasss(s) of Animal

In the figure below we can see the syntax for subclass as well as a broad example + a representative graph as well as a more specific example + representative graph of that example. 

!["subclass"](/pngs/subclass.png)

     Lets break down the slide example!
          + looks like we have the following classes: Cogan, Human, Mammal.
          +Therefore we have:
               - Mammal = Main Class 
               - Human = Subclass of Mammal 
               - Cogan = type of Human

      + Cogan is a Human -- Human is a type of Mammal, therefore, cogan is a type of Mammal. 

      + If we remember our previous animal example we are doing the same thing but with the persective of Mammal as our main class now.

### Axiom 2: Disjointness 🥵
In Logic <ins> **Disjointness** </ins> is when two groups/ subclasses **DO NOT** share  any members. Two sublasses are disjoint if they have *no overlap*.

<img align="left" src="/pngs/disjointness.png" width="200" height="170">


      Example: Animals 
      + Animal = Main Class (A.K.A your big group fo things)
      + Birds 🐦 = Subclass of Animal 
      + Fish 🐠 = Subclass of Animal 

      While fish and bird are both subclasses of animal there is no animal that is both a bird and a fish at the same time. 

<BR>
Now lets look at a KASTLE lab example, Here we have disjointness represented by the graghical notation and an example using: 

- *Anything* ⚪
- *Elephant* 🐘 
- *Newt* 🦎


![Disjoint](/pngs/disjoint.png)

     Lets Break down the example!
      + looks like we have the following classes: 
               - Anything ⚪
               - Elephant 🐘
               - Newt 🦎

      + If anything is type Elephant -- Then Anyhting can not be type newt. No matter what, if Anything is type Elephant then it can never be type Newt and this also works vise versa. 

## Axiom 3 & 4: Global Domain and Scoped Domain 🥵
In Logic you have domains and it comes in two different version: *Global Domain* & *Scoped Domain*.

- **Global Domain**: refers to the complete set of things/ objects that we consider in a particular discussion. Global domain includes *EVERYTHING* that might be involved in our conversation. Everthing that is classfied into subclasses or categories comes from the **Global Domain**. 

      Example: Global Domain
          - All Living Things = Global Domain 🌎
               + Animals 🐖
               + Plants 🌿
               + Fungi 🍄

      Global domain is like taking another step out. We have been working in our examples with Mammals, Birds, & Fish which are subclasses of Aminals which belong to Global Domain: All living things. 

 !["Global"](/pngs/globaldomaon.png)
    
     Lets Break down the example!
            + Global Domain: 
                - Bill
                - Cogan 
                - Parent
     If Bill hasChild Cogan, then Bill will be of type parent. Bill is of type parent becuse of the relationship hasChild.

- **Scoped Domain**: refers to a smaller, more specific part of the global domain, like zooming in on a specific area within *EVERYTHING*. 

      Example: We are looking for the specific domain of mammals within our Global Domain: All Animals. Therefore, Mammals will be our Scoped Domain inside our Global Domain All Animals. 

          - All Animals = Global Domain 🌎
               + Mammals 🦁 = Scoped domain of interest
               + Fish 🐠
               + Birds 🐦

 
!["Scoped Domain"](/pngs/scoped.png)
 
     + lets breakdown the exxample!:
       - we have the follow:
            + Nancy 
            + Student 
            + CEG4350
            + Course

     If Nancy takesCourse CEG4350 and if CEG4350 is of type course, then through this relationship Nancy is of type Student. 

## Axiom 5 & 6: Global Range and Scoped Range 🥵
In Logic you have Ranges and similar to domain there are 2 types: *Global Range* & *Scoped Range*. 

- **Global Range**: refers to the complete set of possible values/outcomes that a logical staement can produce in the entire domain. A global range can provide the full picture. 

!["Global Range"](/pngs/globalrange.png)

    Lets Break down the example(s)!
        + Global Range: 
            - Bill
            - Cogan 
            - Parent
    If Cogan is the childOf Bill, then through the relationship childOf Bill must be of type Parent. 

- **Scoped Range**: has a restriction or specific subset of the Global Domain that we focus on in a particular context or stuation. it aids us in what we are reasoning about. 

      Example: 

         + Global Range: All possible people in a "parentOf" relationship 🤱👶

        + Scoped Range: Only parents who have more that one child. 🤱👶👶


!["Global Range"](/pngs/scopedrange.png)
     
     + Lets break down the exxample!
          - Cogan
          - Bill
          - Child 
          - Parent

     If Cogan is of type Child, Then Cogan is a childOf Bill and then Bill must be of type parent if he has the relationship to Cogan through the childOf relationship. 

## Axiom 9:  Functionality 🥵
   In logic **Functionality** refers to the property of a relation where each input is related to exactly one output. More simplistically a function has <ins>*Exactly One Output*</ins>.

!["functionality"](/pngs/functionality.png)

There are several kinds of functionality including: 
   - *Axiom 10: **Qualified Functionality***
   - *Axiom 11: **Scoped Functionlity***
   - *Axiom 12: **Qualified Scoped Functionality***
   - *Axiom 13: **Inverse Functionality***
   - *Axiom 14: **Inverse Qualified Functionality***
   - *Axiom 15: **Inverse Scoped Functionality***
   - *Axiom 16: **Inverse Qualified Scoped***

 These as well as the remaining axioms not covered in this module are are all expressed in the [Understanding Axioms](https://docs.google.com/presentation/d/1EmLxLo8yzo9-O6nKr7Yf6GRZdUXqe_VovG02JbTuh60/edit?usp=sharing) presentation and is your responsibility to go through and study them. **YOU WILL BE ASSESSED ON THESE IN THE ASSIGNMENT AND BY THE LAB.**

## Assignment
To assess your knowledge over this module you will need to complete the <ins>Axiom Assignment</ins>. This Assignment will go through all of the axioms in the [Understanding Axioms](https://docs.google.com/presentation/d/1EmLxLo8yzo9-O6nKr7Yf6GRZdUXqe_VovG02JbTuh60/edit?usp=sharing) presentation.  Once you have completed the Assignment reachout to the KASTLE members to schedule a time to go through your answers! 😊😊

- To access the assignment click here ➡️ [Axiom Assignment](/knowledge-graphs/02-modeling-fundamentals/Supplementary-material/Assignments/Axiom-assign.md)




## References
### [[1]  Krötzsch, M., Simancik, F., & Horrocks, I. (2012). A description logic primer. arXiv preprint arXiv:1201.4089.](https://arxiv.org/pdf/1201.4089)
<a id="1"></a>

### [[2] Krötzsch, M., Rudolph, S., & Hitzler, P. (2008). Description logic rules. In ECAI 2008 (pp. 80-84). IOS Press.](https://corescholar.libraries.wright.edu/cse/185/)
<a id="2"></a>

### [[3]Enderton, H. B. (2001). A mathematical introduction to logic. Elsevier.](https://bookshelf.jrpotter.com/Bookshelf/Enderton/Logic.pdf)
<a id="3"></a>

### [[4] Understanding Axioms by KASTLELab.](https://docs.google.com/presentation/d/1EmLxLo8yzo9-O6nKr7Yf6GRZdUXqe_VovG02JbTuh60/edit?usp=sharing)
<a id='4'></a>
