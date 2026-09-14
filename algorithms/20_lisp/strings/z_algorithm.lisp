;;; Z-algorithm in Common Lisp
(defun z-algorithm (s)
  (let* ((n (length s))
         (z (make-array n :initial-element 0))
         (l 0)
         (r 0))
    (unless (zerop n) (setf (aref z 0) n))
    (loop for i from 1 below n do
      (when (<= i r)
        (setf (aref z i) (min (- r i -1) (aref z (- i l)))))
      (loop while (and (< (+ i (aref z i)) n)
                       (char= (char s (aref z i)) (char s (+ i (aref z i)))))
            do (incf (aref z i)))
      (when (> (1- (+ i (aref z i))) r)
        (setf l i)
        (setf r (1- (+ i (aref z i))))))
    z))

(defun test-z-algorithm ()
  (assert (equalp (z-algorithm "abacaba") #(7 0 1 0 3 0 1)))
  (format t "[Common Lisp ZAlgorithm] Z-algorithm verified~%"))

(test-z-algorithm)
