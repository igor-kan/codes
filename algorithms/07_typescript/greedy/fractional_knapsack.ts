/**
 * Fractional Knapsack Problem (CLRS 3rd Ed. Chapter 16.2)
 * Greedy algorithm sorting items by value-to-weight ratio in O(n log n).
 */

export interface FractionalItem {
  weight: number;
  value: number;
}

export function fractionalKnapsack(items: FractionalItem[], capacity: number): number {
  const sorted = [...items].sort((a, b) => b.value / b.weight - a.value / a.weight);
  let totalValue = 0;
  let remainingCap = capacity;

  for (const item of sorted) {
    if (item.weight <= remainingCap) {
      totalValue += item.value;
      remainingCap -= item.weight;
    } else {
      totalValue += (item.value / item.weight) * remainingCap;
      break;
    }
  }
  return totalValue;
}

const fItems: FractionalItem[] = [
  { weight: 10, value: 60 },
  { weight: 20, value: 100 },
  { weight: 30, value: 120 },
];
const fVal = fractionalKnapsack(fItems, 50);
if (fVal !== 240) throw new Error("Fractional Knapsack failed");
console.log("CLRS Fractional Knapsack verified successfully.");
