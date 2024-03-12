# Validation
1a. Homer's Role
CQ1: What is Homer's family role?
Bridged Dataset:  

SPARQL Query
```sql
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix sp-ont: <https://simpson-family.com/lod/ontology/> 
prefix sp-res: <https://simpson-family.com/lod/resource/> 

SELECT ?string ?Role WHERE {
    ?FamilyMember sp-ont:hasName ?Name .
  	?Name sp-ont:firstAsString ?string .
  	?Name rdf:type sp-ont:First .
	?FamilyMember sp-ont:performsRole ?Role .
  FILTER(
  	?string="Homer"
  )
}
```

Results\
<img width="484" alt="simpsonsSPARQLhomer" src="https://github.com/kastle-lab/kastle-drawbridge/assets/100725412/bb2aace0-d856-4f8e-a68c-5e20d7f642ce">

1b. Simpson's Father Roles
CQ1: Who plays the father role in the Simpsons family?  
Bridged Dataset:  

SPARQL Query
```sql
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix sp-ont: <https://simpson-family.com/lod/ontology/> 
prefix sp-res: <https://simpson-family.com/lod/resource/> 

SELECT ?String ?Role WHERE {
  ?Role rdf:type sp-ont:Father .
  
  ?FamilyMember sp-ont:performsRole ?Role .
  ?FamilyMember sp-ont:hasName ?Name .
  ?Name sp-ont:firstAsString ?String . 
}    limit 10
```

Results\
<img width="484" alt="simpsonsSPARQLfathers" src="https://github.com/kastle-lab/kastle-drawbridge/assets/100725412/676d4829-3ead-461f-8f6b-9303b5940e99">


2. Simpson's Sibling Roles
CQ2:  Who are the siblings within the Simpsons family?
Bridged Dataset:  

SPARQL Query
```sql
PREFIX spt: <http://spitfire-project.eu/ontology/ns/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix sp-ont: <https://simpson-family.com/lod/ontology/> 
prefix sp-res: <https://simpson-family.com/lod/resource/> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 

SELECT ?FirstName ?Role WHERE {
  ?FamilyMember sp-ont:hasName ?Name .

  ?Name sp-ont:firstAsString ?FirstName .

  ?FamilyMember sp-ont:performsRole ?Roles .

  ?Roles a ?Role
  FILTER (?Role = sp-ont:Brother || ?Role = sp-ont:Sister)
} LIMIT 100
```

Results\
<img width="484" alt="simpsonsSPARQLsiblings" src="https://github.com/kastle-lab/kastle-drawbridge/assets/100725412/4df6e152-9b99-4d6f-bbc3-540a9d471dad">


3. Simpson's Family Member Names
3: What are the names of all the members? 
Bridged Dataset:  

SPARQL Query
```sql
PREFIX spt: <http://spitfire-project.eu/ontology/ns/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix sp-ont: <https://simpson-family.com/lod/ontology/> 
prefix sp-res: <https://simpson-family.com/lod/resource/> 
prefix xsd: <http://www.w3.org/2001/XMLSchema#> 

SELECT ?FirstName ?FamilyMember WHERE {
  ?FamilyMember sp-ont:hasName ?Name .
  ?Name sp-ont:firstAsString ?FirstName .

} LIMIT 100
```
Results\
<img width="484" alt="simpsonsSPARQLnames" src="https://github.com/kastle-lab/kastle-drawbridge/assets/100725412/c9650b9a-c6fa-4e99-a2d9-74edce0828eb">

