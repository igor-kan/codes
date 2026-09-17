/**
 * Job Sequencing with Deadlines
 * Greedily schedules jobs to maximize profit without missing deadlines.
 */

export interface Job {
  id: string;
  deadline: number;
  profit: number;
}

export function jobSequencing(jobs: Job[]): { scheduledJobs: string[]; totalProfit: number } {
  const sorted = [...jobs].sort((a, b) => b.profit - a.profit);
  const maxDeadline = Math.max(...jobs.map((j) => j.deadline));
  const slots = new Array<string | null>(maxDeadline + 1).fill(null);
  let totalProfit = 0;

  for (const job of sorted) {
    for (let t = job.deadline; t > 0; t--) {
      if (slots[t] === null) {
        slots[t] = job.id;
        totalProfit += job.profit;
        break;
      }
    }
  }

  const scheduledJobs: string[] = [];
  for (let t = 1; t <= maxDeadline; t++) {
    if (slots[t] !== null) scheduledJobs.push(slots[t]!);
  }
  return { scheduledJobs, totalProfit };
}

const jobsList: Job[] = [
  { id: "a", deadline: 2, profit: 100 },
  { id: "b", deadline: 1, profit: 19 },
  { id: "c", deadline: 2, profit: 27 },
  { id: "d", deadline: 1, profit: 25 },
  { id: "e", deadline: 3, profit: 15 },
];
const jsRes = jobSequencing(jobsList);
if (jsRes.totalProfit !== 142) throw new Error("Job sequencing failed");
console.log("Job Sequencing with Deadlines verified successfully.");
