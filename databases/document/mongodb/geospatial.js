// Geospatial queries with 2dsphere indexes.
db.places.createIndex({ location: "2dsphere" });

db.places.find({
  location: {
    $near: {
      $geometry: { type: "Point", coordinates: [-0.1276, 51.5072] },
      $maxDistance: 5000,
    },
  },
});

db.places.aggregate([
  { $geoNear: { near: { type: "Point", coordinates: [2.3522, 48.8566] },
                distanceField: "distance", spherical: true, maxDistance: 10000 } },
  { $limit: 5 },
]);
