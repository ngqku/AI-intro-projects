## How to Run
Run like any other python file
Run files individually
* Libraries needed: `numpy`, `matplotlib` and `tensorflow` 

  
## 1. MNIST Digit Recognition (`mnist_solution.py`)
This project involves building a model to recognize handwritten digits from the MNIST dataset.
* **Dataset:** The MNIST database of handwritten digits has a training set of 60,000 examples and a test set of 10,000 examples.

## 2. Nairobi Subcounty Coloring (`nairobi_coloring.py`)
* **Concept:** Applying CSP logic to a local geographic map.
* **Objective:**To color all the sub-counties in Nairobi ensuring that no adjacent sub-counties have the same color using the minimum colors possible
 
## 3. Australia Map Coloring (`australia_map_coloring.py`)
This script solves the classic Australia map coloring problem. 
* **Algorithm:** Constraint Satisfaction Problem (CSP) using backtracking.
* **Goal:** To color each region of Australia (WA, NT, Q, NSW, V, SA, T) such that no two adjacent regions share the same color using only three colors.


## 4.Family Logic Engine(family_logic.pl)
 This small project is a Knowledge-Based system developed in SWI-prolog.
 * **Concept:** it utilizes Predicate Calculus to model and query family relationships.
 * It defines a set of core atomic facts, the system then uses interface rules to dynamically derive relationships like siblings ,cousins and and more
 *  **How to run**
 *  You will need SWI-Prog , use this link to download it (https://www.swi-prolog.org/build/unix.html)
 *  Open your terminal in the project directory and run -- `swipl -s family_logic.pl`
 *  Querying: at the `?-` prompt, you can test the logic
 *  to find siblings: `sibling(X,patrick).`
 *  to reload after edits: `make.`
