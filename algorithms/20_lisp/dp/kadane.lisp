;;; Kadane's algorithm for maximum subarray sum in Common Lisp
(defun kadane (arr)
  (let ((best (aref arr 0))
        (cur (aref arr 0)))
    (loop for i from 1 below (length arr) do
      (let ((x (aref arr i)))
        (setf cur (max x (+ cur x)))
        (setf best (max best cur))))
    best))

(defun test-kadane ()
  (assert (= (kadane #(-2 1 -3 4 -1 2 1 -5 4)) 6))
  (assert (= (kadane #(-5 -2 -3)) -2))
  (format t "[Common Lisp Kadane] Maximum subarray sum verified~%"))

(test-kadane)
