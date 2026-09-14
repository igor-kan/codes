;;; Common Lisp Bubble Sort Implementation
(defun bubble-sort (list)
  (let ((arr (copy-seq list))
        (n (length list)))
    (loop for i from 0 below (1- n) do
      (loop for j from 0 below (- n i 1) do
        (when (> (elt arr j) (elt arr (1+ j)))
          (rotatef (elt arr j) (elt arr (1+ j))))))
    arr))
