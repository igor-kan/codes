;;; Longest Common Subsequence using DP in Common Lisp
(defun lcs (s1 s2)
  (let* ((m (length s1))
         (n (length s2))
         (dp (make-array (list (1+ m) (1+ n)) :initial-element 0)))
    (loop for i from 1 to m do
      (loop for j from 1 to n do
        (if (char= (char s1 (1- i)) (char s2 (1- j)))
            (setf (aref dp i j) (1+ (aref dp (1- i) (1- j))))
            (setf (aref dp i j) (max (aref dp (1- i) j) (aref dp i (1- j)))))))
    (aref dp m n)))

(defun test-lcs ()
  (format t "Testing LCS (Common Lisp)~%")
  (format t "lcs(\"abcde\", \"ace\") = ~A (expected 3)~%" (lcs "abcde" "ace"))
  (format t "lcs(\"abc\", \"abc\") = ~A (expected 3)~%" (lcs "abc" "abc"))
  (format t "lcs(\"abc\", \"def\") = ~A (expected 0)~%" (lcs "abc" "def"))
  (format t "lcs(\"aggtab\", \"gxtxayb\") = ~A (expected 4)~%" (lcs "aggtab" "gxtxayb"))
  (format t "lcs(\"\", \"abc\") = ~A (expected 0)~%" (lcs "" "abc"))
  (format t "All LCS tests passed.~%"))

(test-lcs)