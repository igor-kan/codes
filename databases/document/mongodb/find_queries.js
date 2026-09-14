// Query operators, projection and sorting.
db.users.find(
  { age: { $gte: 18, $lt: 65 }, roles: { $in: ["admin", "editor"] } },
  { name: 1, email: 1, _id: 0 },
).sort({ name: 1 }).limit(20);

db.users.findOne({ "address.city": "London" });

db.orders.find({
  $or: [
    { status: "pending" },
    { total: { $gt: 1000 } },
  ],
});
