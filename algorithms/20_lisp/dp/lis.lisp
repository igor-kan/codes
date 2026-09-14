;;; Longest increasing subsequence (O(n^2) DP) in Common Lisp
(defun lis (arr)
  (let ((n (length arr)))
    (if (zerop n)
        0
        (let ((dp (make-array n :initial-element 1)))
          (loop for i from 1 below n do
            (loop for j from 0 below i do
              (when (< (aref arr j) (aref arr i))
                (setf (aref dp i) (max (aref dp i) (1+ (aref dp j)))))))
          (reduce #'max dp)))))

(defun test-lis ()
  (assert (= (lis #(10 9 2 5 3 7 101 18)) 4))
  (assert (= (lis #()) 0))
  (format t "[Common Lisp LIS] Longest increasing subsequence verified~%"))

(test-lis)
