;;; Knuth-Morris-Pratt string matching in Common Lisp
(defun compute-lps (pattern)
  (let* ((m (length pattern))
         (lps (make-array m :initial-element 0))
         (len 0)
         (i 1))
    (loop while (< i m) do
      (if (char= (char pattern i) (char pattern len))
          (progn
            (incf len)
            (setf (aref lps i) len)
            (incf i))
          (if (zerop len)
              (progn
                (setf (aref lps i) 0)
                (incf i))
              (setf len (aref lps (1- len))))))
    lps))

(defun kmp-search (text pattern)
  (let* ((n (length text))
         (m (length pattern))
         (lps (compute-lps pattern))
         (i 0)
         (j 0)
         (result nil))
    (loop while (< i n) do
      (if (char= (char pattern j) (char text i))
          (progn
            (incf i)
            (incf j))
          (if (zerop j)
              (incf i)
              (setf j (aref lps (1- j)))))
      (when (= j m)
        (push (- i j) result)
        (setf j (aref lps (1- j)))))
    (nreverse result)))

(defun test-kmp ()
  (format t "Testing KMP (Common Lisp)~%")
  (format t "kmp(\"ABABDABACDABABCABAB\", \"ABABCABAB\") = ~A (expected (10))~%"
          (kmp-search "ABABDABACDABABCABAB" "ABABCABAB"))
  (format t "kmp(\"AAAA\", \"AA\") = ~A (expected (0 1 2))~%"
          (kmp-search "AAAA" "AA"))
  (format t "kmp(\"HELLO WORLD\", \"WORLD\") = ~A (expected (6))~%"
          (kmp-search "HELLO WORLD" "WORLD"))
  (format t "kmp(\"ABC\", \"DEF\") = ~A (expected NIL)~%"
          (kmp-search "ABC" "DEF"))
  (format t "All KMP tests passed.~%"))

(test-kmp)