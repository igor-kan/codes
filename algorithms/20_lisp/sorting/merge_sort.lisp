;;; Common Lisp Merge Sort Implementation
(defun merge-lists (a b)
  (cond ((null a) b)
        ((null b) a)
        ((<= (car a) (car b)) (cons (car a) (merge-lists (cdr a) b)))
        (t (cons (car b) (merge-lists a (cdr b))))))

(defun merge-sort (list)
  (if (or (null list) (null (cdr list)))
      list
      (let* ((mid (floor (length list) 2)))
        (merge-lists (merge-sort (subseq list 0 mid))
                     (merge-sort (subseq list mid))))))

(defun test-merge-sort ()
  (format t "Testing MergeSort (Common Lisp)~%")
  (let* ((data '(33 7 91 12 5 5 78 2 44 19))
         (sorted (merge-sort data)))
    (assert (equal sorted '(2 5 5 7 12 19 33 44 78 91)))
    (format t "[Common Lisp MergeSort] Recursive merge sort verified: ~A~%" sorted))
  (format t "Empty and singleton lists handled: ~A ~A~%"
          (merge-sort nil) (merge-sort '(42))))

(test-merge-sort)
