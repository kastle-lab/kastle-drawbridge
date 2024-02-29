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

Results

1b. Simpson's Father Roles
CQ1: Who plays the father role in the Simpsons family?  
Bridged Dataset:  

SPARQL Query
```sql
SELECT ?string ?Role WHERE {
  ?Role rdf:type sp-ont:Father .
  
  ?FamilyMember sp-ont:performsRole ?Role .
  
  ?FamilyMember sp-ont:hasName ?Name .
  ?Name rdf:type sp-ont:First . 
}   
```

Results


2. CQ2 Titled
CQ2: Long Form  
Bridged Dataset:  

SPARQL Query
```sql
[Your query here]
```

Results
