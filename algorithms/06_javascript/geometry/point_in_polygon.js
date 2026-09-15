// Ray-casting point-in-polygon test.
function inside(polygon, px, py) {
  let result = false;
  const n = polygon.length;
  let j = n - 1;
  for (let i = 0; i < n; i += 1) {
    const [xi, yi] = polygon[i];
    const [xj, yj] = polygon[j];
    if ((yi > py) !== (yj > py) && px < ((xj - xi) * (py - yi)) / (yj - yi) + xi) {
      result = !result;
    }
    j = i;
  }
  return result;
}

const square = [[0, 0], [4, 0], [4, 4], [0, 4]];
if (!inside(square, 2, 2) || inside(square, 5, 5)) throw new Error("ray casting failed");
console.log("point in polygon ok");
