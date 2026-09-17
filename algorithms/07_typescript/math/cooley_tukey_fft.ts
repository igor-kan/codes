/**
 * Cooley-Tukey Fast Fourier Transform (CLRS 3rd Ed. Chapter 30.2)
 * Computes Discrete Fourier Transform (DFT) and Inverse DFT in O(n log n).
 */

export interface Complex {
  re: number;
  im: number;
}

function add(a: Complex, b: Complex): Complex {
  return { re: a.re + b.re, im: a.im + b.im };
}

function sub(a: Complex, b: Complex): Complex {
  return { re: a.re - b.re, im: a.im - b.im };
}

function mul(a: Complex, b: Complex): Complex {
  return { re: a.re * b.re - a.im * b.im, im: a.re * b.im + a.im * b.re };
}

export function fft(a: Complex[], invert = false): Complex[] {
  const n = a.length;
  if (n === 1) return [a[0]];

  const a0 = new Array<Complex>(n / 2);
  const a1 = new Array<Complex>(n / 2);
  for (let i = 0; i < n / 2; i++) {
    a0[i] = a[2 * i];
    a1[i] = a[2 * i + 1];
  }

  const y0 = fft(a0, invert);
  const y1 = fft(a1, invert);

  const y = new Array<Complex>(n);
  const angle = ((invert ? -2 : 2) * Math.PI) / n;
  let w: Complex = { re: 1, im: 0 };
  const wn: Complex = { re: Math.cos(angle), im: Math.sin(angle) };

  for (let k = 0; k < n / 2; k++) {
    const term = mul(w, y1[k]);
    y[k] = add(y0[k], term);
    y[k + n / 2] = sub(y0[k], term);
    if (invert) {
      y[k].re /= 2;
      y[k].im /= 2;
      y[k + n / 2].re /= 2;
      y[k + n / 2].im /= 2;
    }
    w = mul(w, wn);
  }
  return y;
}

const sig: Complex[] = [
  { re: 1, im: 0 },
  { re: 2, im: 0 },
  { re: 3, im: 0 },
  { re: 4, im: 0 },
];
const freq = fft(sig);
const rec = fft(freq, true);
if (Math.abs(rec[0].re - 1) > 1e-6 || Math.abs(rec[2].re - 3) > 1e-6) {
  throw new Error("FFT verification failed");
}
console.log("CLRS Cooley-Tukey FFT verified successfully.");
