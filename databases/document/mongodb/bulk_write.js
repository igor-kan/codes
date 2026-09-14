// Ordered bulk operations for throughput.
const ops = [
  { insertOne: { document: { email: "new@example.com", name: "New" } } },
  { updateOne: { filter: { email: "ada@example.com" }, update: { $inc: { visits: 1 } } } },
  { deleteOne: { filter: { email: "old@example.com" } } },
];

const result = db.users.bulkWrite(ops, { ordered: false });
printjson(result.getWriteErrors());
