;;; Breadth-First Search in Common Lisp
(defun bfs (graph start)
  (let ((visited (make-hash-table :test 'equal))
        (queue (list start))
        (order nil))
    (setf (gethash start visited) t)
    (loop while queue do
      (let ((node (pop queue)))
        (push node order)
        (dolist (neighbor (gethash node graph))
          (unless (gethash neighbor visited)
            (setf (gethash neighbor visited) t)
            (setf queue (append queue (list neighbor)))))))
    (nreverse order)))
