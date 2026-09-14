function [g, l] = gcd_lcm(a, b)
% GCD_LCM Computes Greatest Common Divisor and Least Common Multiple
    orig_a = a; orig_b = b;
    while b ~= 0
        t = b;
        b = mod(a, b);
        a = t;
    end
    g = a;
    l = abs(orig_a * orig_b) / g;
end
