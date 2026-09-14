;;; Binary search over a sorted array in Common Lisp
(defun binary-search (arr target)
  (let ((lo 0)
        (hi (1- (length arr))))
    (loop
      (when (> lo hi) (return -1))
      (let* ((mid (floor (+ lo hi) 2))
             (val (aref arr mid)))
        (cond
          ((= val target) (return mid))
          ((< val target) (setf lo (1+ mid)))
          (t (setf hi (1- mid))))))))

(defun test-binary-search ()
  (let ((arr (make-array 7 :initial-contents '(1 3 5 7 9 11 13))))
    (assert (= (binary-search arr 7) 3))
    (assert (= (binary-search arr 8) -1))
    (assert (= (binary-search arr 1) 0))
    (format t "[Common Lisp BinarySearch] Binary search verified~%")))

(test-binary-search)
