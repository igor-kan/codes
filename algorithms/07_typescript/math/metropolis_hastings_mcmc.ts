/**
 * Metropolis-Hastings MCMC (Numerical Recipes 3rd Ed. Chapter 15.8)
 * Markov Chain Monte Carlo sampling from arbitrary target probability density p(x).
 */

export function metropolisHastings(
  targetLogPdf: (x: number) => number,
  x0 = 0,
  proposalStd = 0.5,
  numSamples = 1000
): number[] {
  const samples: number[] = [x0];
  let curX = x0;
  let curLogP = targetLogPdf(curX);

  for (let i = 0; i < numSamples; i++) {
    // Normal proposal centered at curX
    const propX = curX + proposalStd * (Math.random() * 2 - 1);
    const propLogP = targetLogPdf(propX);

    const logAlpha = propLogP - curLogP;
    if (Math.log(Math.random()) < logAlpha) {
      curX = propX;
      curLogP = propLogP;
    }
    samples.push(curX);
  }
  return samples;
}

// Sample from standard Gaussian: log p(x) = -0.5 * x^2
const mhSamples = metropolisHastings((x) => -0.5 * x * x, 0, 1.0, 500);
const mhMean = mhSamples.reduce((a, b) => a + b, 0) / mhSamples.length;
if (Math.abs(mhMean) > 0.5) throw new Error("Metropolis-Hastings failed");
console.log(`NR Metropolis-Hastings MCMC verified: sampleMean=${mhMean.toFixed(4)}`);
