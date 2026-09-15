// Primary module interface unit (C++20 modules).
export module math;

export int add(int a, int b) { return a + b; }
export int multiply(int a, int b) { return a * b; }

export namespace stats {
inline double mean(double a, double b) { return (a + b) / 2.0; }
}
