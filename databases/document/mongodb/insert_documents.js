// Insert one or many documents.
db.users.insertOne({
  email: "ada@example.com",
  name: "Ada Lovelace",
  tags: ["math", "pioneer"],
  createdAt: new Date(),
});

db.users.insertMany([
  { email: "grace@example.com", name: "Grace Hopper", roles: ["admin"] },
  { email: "alan@example.com", name: "Alan Turing", roles: ["editor"] },
]);
