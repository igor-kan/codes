;;; Selection sort in Common Lisp
(defun selection-sort (arr)
  (let ((a (copy-seq arr))
        (n (length arr)))
    (loop for i from 0 below (1- n) do
      (let ((min-idx i))
        (loop for j from (1+ i) below n do
          (when (< (aref a j) (aref a min-idx))
            (setf min-idx j)))
        (rotatef (aref a i) (aref a min-idx))))
    a))

(defun test-selection-sort ()
  (let ((data #(33 7 91 12 5 5 78 2 44 19))
        (expected #(2 5 5 7 12 19 33 44 78 91)))
    (assert (equalp (selection-sort data) expected))
    (format t "[Common Lisp SelectionSort] Selection sort verified: ~A~%"
            (selection-sort data))))

(test-selection-sort)
