// Change streams react to realtime mutations.
const pipeline = [
  { $match: { "ns.coll": "orders", operationType: { $in: ["insert", "update"] } } },
  { $project: { "fullDocument.customerId": 1, "fullDocument.total": 1 } },
];

const changeStream = db.orders.watch(pipeline, {
  fullDocument: "updateLookup",
  maxAwaitTimeMS: 1000,
});

changeStream.on("change", (change) => {
  print("order changed", JSON.stringify(change.fullDocument));
});
