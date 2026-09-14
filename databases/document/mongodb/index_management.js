// Creating and inspecting indexes.
db.users.createIndex({ email: 1 }, { unique: true });
db.users.createIndex({ name: "text", bio: "text" });
db.users.createIndex({ location: "2dsphere" });
db.orders.createIndex({ customerId: 1, createdAt: -1 });

db.users.getIndexes();
db.users.aggregate([{ $indexStats: {} }]);
