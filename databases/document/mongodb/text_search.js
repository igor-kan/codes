// Full-text search with weights and scoring.
db.articles.createIndex({ title: "text", body: "text" }, {
  weights: { title: 10, body: 1 },
});

db.articles.find(
  { $text: { $search: "distributed systems -tutorial" } },
  { score: { $meta: "textScore" } },
).sort({ score: { $meta: "textScore" } });
