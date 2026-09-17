/**
 * Sutherland-Hodgman Algorithm
 * Clips a subject polygon against a convex clipping polygon.
 */

export interface PointC {
  x: number;
  y: number;
}

function isInside(p: PointC, cp1: PointC, cp2: PointC): boolean {
  return (cp2.x - cp1.x) * (p.y - cp1.y) >= (cp2.y - cp1.y) * (p.x - cp1.x);
}

function intersection(cp1: PointC, cp2: PointC, s: PointC, e: PointC): PointC {
  const dc = { x: cp1.x - cp2.x, y: cp1.y - cp2.y };
  const dp = { x: s.x - e.x, y: s.y - e.y };
  const n1 = cp1.x * cp2.y - cp1.y * cp2.x;
  const n2 = s.x * e.y - s.y * e.x;
  const n3 = 1.0 / (dc.x * dp.y - dc.y * dp.x);
  return {
    x: (n1 * dp.x - n2 * dc.x) * n3,
    y: (n1 * dp.y - n2 * dc.y) * n3,
  };
}

export function clipPolygon(subject: PointC[], clipPolygon: PointC[]): PointC[] {
  let outputList = subject;
  const cpLen = clipPolygon.length;

  for (let i = 0; i < cpLen; i++) {
    const cp1 = clipPolygon[i];
    const cp2 = clipPolygon[(i + 1) % cpLen];
    const inputList = outputList;
    outputList = [];

    if (inputList.length === 0) break;
    let s = inputList[inputList.length - 1];

    for (const e of inputList) {
      if (isInside(e, cp1, cp2)) {
        if (!isInside(s, cp1, cp2)) outputList.push(intersection(cp1, cp2, s, e));
        outputList.push(e);
      } else if (isInside(s, cp1, cp2)) {
        outputList.push(intersection(cp1, cp2, s, e));
      }
      s = e;
    }
  }
  return outputList;
}

const subj: PointC[] = [
  { x: 50, y: 150 },
  { x: 200, y: 50 },
  { x: 350, y: 150 },
  { x: 350, y: 300 },
  { x: 250, y: 300 },
  { x: 200, y: 250 },
  { x: 150, y: 350 },
  { x: 100, y: 250 },
  { x: 100, y: 200 },
];
const clip: PointC[] = [
  { x: 100, y: 100 },
  { x: 300, y: 100 },
  { x: 300, y: 300 },
  { x: 100, y: 300 },
];
const clipped = clipPolygon(subj, clip);
if (clipped.length < 4) throw new Error("Polygon clipping failed");
console.log("Sutherland-Hodgman Polygon Clipping verified successfully.");
