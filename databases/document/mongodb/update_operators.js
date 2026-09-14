// Update operators: set, unset, inc, push, pull.
db.users.updateOne(
  { email: "ada@example.com" },
  {
    $set: { lastLogin: new Date() },
    $inc: { loginCount: 1 },
    $push: { tags: { $each: ["compiler"], $slice: -10 } },
    $unset: { legacyId: "" },
  },
);

db.users.updateMany(
  { roles: "admin" },
  { $addToSet: { permissions: "manage-users" } },
);
