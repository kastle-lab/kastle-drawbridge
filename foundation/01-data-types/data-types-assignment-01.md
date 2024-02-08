# Datatypes
Python does not require explicit declaration of data types unlike Java or C-based languages.

## Numeric Representation
* integer: representation of whole numbers
* float: similar to a `double` and, as such, can represent decimal values. 

## Non-Numeric Representation
* character: a single letter represented in either upper or lower case. For example: "A" and "b"
* String: a series of letters.  For example: "DrawBridge" and "KASTLE"
* Boolean: representation of 0 and 1 as `True` and `False` (the `T` and `F` casing matters)

## Abstract Data Types (ADT)
* Classes: representation of many characteristics through datatypes as an individual value.  For example, a `Person` is represented by their `name`, `age`.  A `Student` is a specific `Person` that might also extend to represent `ProgramOfStudy` and `YearOfStudy`.

# Assignment
Read and implement [the attached assignment](https://github.com/kastle-lab/kastle-drawbridge/blob/master/foundation/supplementary-material/assignments/cs1160-lab02.pdf) such that your output and calculations match the assignment reading's.

Remember that the numeric datatype affects mathematical calculations. For instance, performing `1/2` rounds down and results in `0`; whereas, `1.0/2.0` evaluates to `0.5`.  What happens if we mix datatypes together (i.e., performing `1/2.0` or `1.0/2`?
