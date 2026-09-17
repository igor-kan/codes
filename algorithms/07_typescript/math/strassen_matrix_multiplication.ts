/**
 * Strassen's Sub-Cubic Matrix Multiplication (CLRS 3rd Ed. Chapter 4.2)
 * Divide-and-conquer multiplication of square matrices running in O(n^(log2 7)) approx O(n^2.81).
 */

function addM(A: number[][], B: number[][]): number[][] {
  return A.map((row, i) => row.map((val, j) => val + B[i][j]));
}

function subM(A: number[][], B: number[][]): number[][] {
  return A.map((row, i) => row.map((val, j) => val - B[i][j]));
}

export function strassenMultiply(A: number[][], B: number[][]): number[][] {
  const n = A.length;
  if (n <= 2) {
    // Base case: standard matrix multiplication
    const C = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) {
      for (let k = 0; k < n; k++) {
        for (let j = 0; j < n; j++) {
          C[i][j] += A[i][k] * B[k][j];
        }
      }
    }
    return C;
  }

  const half = Math.floor(n / 2);
  const a11: number[][] = [], a12: number[][] = [], a21: number[][] = [], a22: number[][] = [];
  const b11: number[][] = [], b12: number[][] = [], b21: number[][] = [], b22: number[][] = [];

  for (let i = 0; i < half; i++) {
    a11.push(A[i].slice(0, half));
    a12.push(A[i].slice(half));
    a21.push(A[i + half].slice(0, half));
    a22.push(A[i + half].slice(half));

    b11.push(B[i].slice(0, half));
    b12.push(B[i].slice(half));
    b21.push(B[i + half].slice(0, half));
    b22.push(B[i + half].slice(half));
  }

  const p1 = strassenMultiply(a11, subM(b12, b22));
  const p2 = strassenMultiply(addM(a11, a12), b22);
  const p3 = strassenMultiply(addM(a21, a22), b11);
  const p4 = strassenMultiply(a22, subM(b21, b11));
  const p5 = strassenMultiply(addM(a11, a22), addM(b11, b22));
  const p6 = strassenMultiply(subM(a12, a22), addM(b21, b22));
  const p7 = strassenMultiply(subM(a11, a21), addM(b11, b12));

  const c11 = subM(addM(addM(p5, p4), p6), p2);
  const c12 = addM(p1, p2);
  const c21 = addM(p3, p4);
  const c22 = subM(subM(addM(p5, p1), p3), p7);

  const C = Array.from({ length: n }, () => new Array(n).fill(0));
  for (let i = 0; i < half; i++) {
    for (let j = 0; j < half; j++) {
      C[i][j] = c11[i][j];
      C[i][j + half] = c12[i][j];
      C[i + half][j] = c21[i][j];
      C[i + half][j + half] = c22[i][j];
    }
  }
  return C;
}

const mA = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 1, 2, 3],
  [4, 5, 6, 7],
];
const mB = [
  [7, 6, 5, 4],
  [3, 2, 1, 0],
  [1, 2, 3, 4],
  [5, 6, 7, 8],
];
const mC = strassenMultiply(mA, mB);
if (mC[0][0] !== 36 || mC[1][1] !== 104) throw new Error("Strassen multiplication failed");
console.log("CLRS Strassen Matrix Multiplication verified successfully.");
