;;; Euclidean GCD and LCM in Common Lisp
(defun custom-gcd (a b)
  (if (zerop b)
      a
      (custom-gcd b (mod a b))))

(defun custom-lcm (a b)
  (/ (abs (* a b)) (custom-gcd a b)))
