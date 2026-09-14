;;; Counting sort for non-negative integers in Common Lisp
(defun counting-sort (arr)
  (let ((n (length arr)))
    (if (zerop n)
        (make-array 0)
        (let* ((max-val (reduce #'max arr))
               (count (make-array (1+ max-val) :initial-element 0)))
          (loop for x across arr do (incf (aref count x)))
          (loop for i from 1 to max-val do
            (incf (aref count i) (aref count (1- i))))
          (let ((out (make-array n)))
            (loop for i from (1- n) downto 0 do
              (let ((x (aref arr i)))
                (decf (aref count x))
                (setf (aref out (aref count x)) x)))
            out)))))

(defun test-counting-sort ()
  (let ((data #(4 2 2 8 3 3 1))
        (expected #(1 2 2 3 3 4 8)))
    (assert (equalp (counting-sort data) expected))
    (format t "[Common Lisp CountingSort] Counting sort verified: ~A~%"
            (counting-sort data))))

(test-counting-sort)
