/**
 * Simulated Annealing (Numerical Recipes 3rd Ed. Chapter 10.9)
 * Global stochastic heuristic using Metropolis acceptance criterion.
 */

export interface City {
  x: number;
  y: number;
}

function tourDistance(tour: number[], cities: City[]): number {
  let dist = 0;
  for (let i = 0; i < tour.length; i++) {
    const c1 = cities[tour[i]];
    const c2 = cities[tour[(i + 1) % tour.length]];
    dist += Math.hypot(c1.x - c2.x, c1.y - c2.y);
  }
  return dist;
}

export function simulatedAnnealingTSP(
  cities: City[],
  initialTemp = 100.0,
  coolingRate = 0.995,
  maxSteps = 5000
): { bestTour: number[]; bestDistance: number } {
  const n = cities.length;
  let currentTour = Array.from({ length: n }, (_, i) => i);
  let currentDist = tourDistance(currentTour, cities);

  let bestTour = [...currentTour];
  let bestDistance = currentDist;
  let T = initialTemp;

  for (let step = 0; step < maxSteps; step++) {
    // 2-opt neighbor: reverse subsegment
    const i = Math.floor(Math.random() * n);
    const j = Math.floor(Math.random() * n);
    if (i === j) continue;

    const nextTour = [...currentTour];
    const [start, end] = i < j ? [i, j] : [j, i];
    const sub = nextTour.slice(start, end + 1).reverse();
    nextTour.splice(start, sub.length, ...sub);

    const nextDist = tourDistance(nextTour, cities);
    const delta = nextDist - currentDist;

    if (delta < 0 || Math.random() < Math.exp(-delta / T)) {
      currentTour = nextTour;
      currentDist = nextDist;
      if (currentDist < bestDistance) {
        bestDistance = currentDist;
        bestTour = [...currentTour];
      }
    }
    T *= coolingRate;
  }
  return { bestTour, bestDistance };
}

const squareCities: City[] = [
  { x: 0, y: 0 },
  { x: 1, y: 0 },
  { x: 1, y: 1 },
  { x: 0, y: 1 },
];
const saRes = simulatedAnnealingTSP(squareCities, 50, 0.99, 2000);
if (Math.abs(saRes.bestDistance - 4) > 1e-4) throw new Error("Simulated Annealing TSP failed");
console.log(`NR Simulated Annealing verified: distance=${saRes.bestDistance}`);
