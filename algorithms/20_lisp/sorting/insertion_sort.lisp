;;; Insertion sort in Common Lisp
(defun insertion-sort (arr)
  (let ((a (copy-seq arr))
        (n (length arr)))
    (loop for i from 1 below n do
      (let ((key (aref a i))
            (j (1- i)))
        (loop while (and (>= j 0) (> (aref a j) key)) do
          (setf (aref a (1+ j)) (aref a j))
          (decf j))
        (setf (aref a (1+ j)) key)))
    a))

(defun test-insertion-sort ()
  (let ((data #(33 7 91 12 5 5 78 2 44 19))
        (expected #(2 5 5 7 12 19 33 44 78 91)))
    (assert (equalp (insertion-sort data) expected))
    (format t "[Common Lisp InsertionSort] Insertion sort verified: ~A~%"
            (insertion-sort data))))

(test-insertion-sort)
