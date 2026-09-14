;;; Common Lisp Quick Sort Implementation
(defun quick-sort (list)
  (when list
    (let ((pivot (first list)))
      (append
        (quick-sort (remove-if-not (lambda (x) (< x pivot)) (rest list)))
        (list pivot)
        (quick-sort (remove-if (lambda (x) (< x pivot)) (rest list)))))))

(defun test-quick-sort ()
  (format t "Testing QuickSort (Common Lisp)~%")
  (let ((data '(33 7 91 12 5 5 78 2 44 19)))
    (let ((sorted (quick-sort data)))
      (assert (equal sorted '(2 5 5 7 12 19 33 44 78 91)))
      (format t "[Common Lisp QuickSort] Functional quicksort verified: ~A~%" sorted)))
  (format t "Empty and singleton lists handled: ~A ~A~%"
          (quick-sort nil) (quick-sort '(42))))

(test-quick-sort)
