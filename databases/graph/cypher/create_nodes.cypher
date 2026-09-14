// Create nodes with labels and properties.
CREATE (ada:Person {name: "Ada Lovelace", born: 1815})
CREATE (alan:Person {name: "Alan Turing", born: 1912})
CREATE (cs:Field {name: "Computer Science"});

// Multi-label nodes and list properties.
CREATE (grace:Person:Engineer {
  name: "Grace Hopper",
  born: 1906,
  languages: ["COBOL", "FLOW-MATIC"]
});
