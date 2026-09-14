;;; Disjoint Set Union (Union-Find) in Common Lisp
(defclass dsu ()
  ((parent :initarg :parent :accessor dsu-parent)
   (rank :initarg :rank :accessor dsu-rank)))

(defun make-dsu (n)
  (make-instance 'dsu
                 :parent (make-array n :initial-contents (loop for i from 0 below n collect i))
                 :rank (make-array n :initial-element 0)))

(defun dsu-find (dsu x)
  (let ((p (aref (dsu-parent dsu) x)))
    (if (/= p x)
        (setf (aref (dsu-parent dsu) x) (dsu-find dsu p))
        p)))

(defun dsu-union (dsu x y)
  (let ((rx (dsu-find dsu x))
        (ry (dsu-find dsu y)))
    (unless (= rx ry)
      (let ((rxr (aref (dsu-rank dsu) rx))
            (ryr (aref (dsu-rank dsu) ry)))
        (cond
          ((< rxr ryr) (setf (aref (dsu-parent dsu) rx) ry))
          ((> rxr ryr) (setf (aref (dsu-parent dsu) ry) rx))
          (t (setf (aref (dsu-parent dsu) ry) rx)
             (incf (aref (dsu-rank dsu) rx))))))))

(defun dsu-connected (dsu x y)
  (= (dsu-find dsu x) (dsu-find dsu y)))

(defun test-dsu ()
  (let ((dsu (make-dsu 5)))
    (dsu-union dsu 0 1)
    (dsu-union dsu 1 2)
    (dsu-union dsu 3 4)
    (assert (dsu-connected dsu 0 2))
    (assert (not (dsu-connected dsu 0 3)))
    (format t "[Common Lisp DSU] Disjoint set union verified~%")))

(test-dsu)
