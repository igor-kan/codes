// Aggregation pipeline: match, group, sort, project.
db.orders.aggregate([
  { $match: { status: "paid" } },
  {
    $group: {
      _id: "$customerId",
      revenue: { $sum: "$total" },
      orders: { $sum: 1 },
      lastOrder: { $max: "$createdAt" },
    },
  },
  { $sort: { revenue: -1 } },
  { $limit: 10 },
  {
    $project: {
      _id: 0,
      customerId: "$_id",
      revenue: { $round: ["$revenue", 2] },
      orders: 1,
      lastOrder: 1,
    },
  },
]);
