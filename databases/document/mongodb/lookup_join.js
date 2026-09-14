// $lookup performs a left outer join across collections.
db.orders.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "customerId",
      foreignField: "_id",
      as: "customer",
    },
  },
  { $unwind: "$customer" },
  {
    $project: {
      total: 1,
      "customer.name": 1,
      "customer.email": 1,
    },
  },
]);
