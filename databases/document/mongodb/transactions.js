// Multi-document ACID transactions across collections.
const session = db.getMongo().startSession();
session.startTransaction({
  readConcern: { level: "snapshot" },
  writeConcern: { w: "majority" },
});

try {
  const accounts = session.getDatabase("bank").accounts;
  accounts.updateOne({ _id: "a" }, { $inc: { balance: -100 } });
  accounts.updateOne({ _id: "b" }, { $inc: { balance: 100 } });
  session.commitTransaction();
} catch (error) {
  session.abortTransaction();
  throw error;
} finally {
  session.endSession();
}
