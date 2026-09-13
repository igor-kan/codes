;;; ==============================================================================
;;; File: languages/20_lisp/a_star_pathfinding.lisp
;;; Language: Common Lisp (ANSI Standard, SBCL / CLISP)
;;; Domain: Artificial Intelligence & Graph Theory
;;; Algorithm: A* Heuristic Graph Pathfinding on 2D Grids
;;;
;;; Rationale & Language Fit:
;;;   Common Lisp is the venerable foundation of symbolic artificial intelligence.
;;;   With homoiconicity (code-as-data), dynamic macro metaprogramming, multiple
;;;   dispatch via CLOS, and rich standard data structures (hash tables, vectors,
;;;   lists), Lisp remains unmatched for algorithmic clarity and expressive power.
;;; ==============================================================================

(defstruct node
  (x 0 :type fixnum)
  (y 0 :type fixnum)
  (g-score most-positive-fixnum :type fixnum)
  (f-score most-positive-fixnum :type fixnum)
  (parent nil))

(defun manhattan-distance (x1 y1 x2 y2)
  "Computes admissible Manhattan distance heuristic h(n) = |x1 - x2| + |y1 - y2|."
  (+ (abs (- x1 x2))
     (abs (- y1 y2))))

(defun node-coord-key (x y)
  "Creates a unique cons pair for hash table coordinate indexing."
  (cons x y))

(defun get-valid-neighbors (x y grid width height)
  "Finds 4-directional cardinal neighbors (Up, Down, Left, Right) avoiding obstacles."
  (let ((directions '((0 . 1) (0 . -1) (1 . 0) (-1 . 0)))
        (neighbors '()))
    (dolist (dir directions neighbors)
      (let ((nx (+ x (car dir)))
            (ny (+ y (cdr dir))))
        (when (and (>= nx 0) (< nx width)
                   (>= ny 0) (< ny height)
                   (= (aref grid ny nx) 0)) ; 0 represents walkable cell, 1 is wall
          (push (cons nx ny) neighbors))))))

(defun reconstruct-path (current-node)
  "Traverses parent pointers back from target to origin."
  (let ((path '()))
    (do ((curr current-node (node-parent curr)))
        ((null curr) path)
      (push (cons (node-x curr) (node-y curr)) path))))

(defun a-star-search (grid start-coord goal-coord)
  "Executes A* search algorithm from start (sx, sy) to goal (gx, gy)."
  (let* ((height (array-dimension grid 0))
         (width  (array-dimension grid 1))
         (sx (car start-coord))
         (sy (cdr start-coord))
         (gx (car goal-coord))
         (gy (cdr goal-coord))
         ;; Priority open list storing active nodes
         (open-list '())
         ;; Closed set tracking visited coordinates
         (closed-set (make-hash-table :test #'equal))
         ;; Node cache mapping (x . y) to allocated struct
         (node-map (make-hash-table :test #'equal)))

    (let ((start-node (make-node :x sx :y sy :g-score 0
                                 :f-score (manhattan-distance sx sy gx gy))))
      (setf (gethash (node-coord-key sx sy) node-map) start-node)
      (push start-node open-list))

    (loop while open-list do
      ;; Extract node with minimal f-score
      (setf open-list (sort open-list #'< :key #'node-f-score))
      (let ((current (pop open-list)))
        (let ((cx (node-x current))
              (cy (node-y current)))
          
          ;; Goal termination
          (when (and (= cx gx) (= cy gy))
            (return-from a-star-search (reconstruct-path current)))

          ;; Mark current node as explored
          (setf (gethash (node-coord-key cx cy) closed-set) t)

          ;; Explore 4-connected neighbors
          (dolist (neighbor-coord (get-valid-neighbors cx cy grid width height))
            (let ((nx (car neighbor-coord))
                  (ny (cdr neighbor-coord)))
              (unless (gethash (node-coord-key nx ny) closed-set)
                (let* ((tentative-g (+ (node-g-score current) 1))
                       (neighbor-node (gethash (node-coord-key nx ny) node-map)))
                  (if (null neighbor-node)
                      ;; Discovered fresh neighbor
                      (let ((new-node (make-node :x nx :y ny
                                                 :g-score tentative-g
                                                 :f-score (+ tentative-g (manhattan-distance nx ny gx gy))
                                                 :parent current)))
                        (setf (gethash (node-coord-key nx ny) node-map) new-node)
                        (push new-node open-list))
                      ;; Existing neighbor: check if tentative path is shorter
                      (when (< tentative-g (node-g-score neighbor-node))
                        (setf (node-g-score neighbor-node) tentative-g
                              (node-f-score neighbor-node) (+ tentative-g (manhattan-distance nx ny gx gy))
                              (node-parent neighbor-node) current)
                        (unless (member neighbor-node open-list)
                          (push neighbor-node open-list)))))))))))
    ;; Return NIL if no path exists
    nil))

(defun print-grid-with-path (grid path start-coord goal-coord)
  (let ((height (array-dimension grid 0))
        (width  (array-dimension grid 1))
        (path-table (make-hash-table :test #'equal)))
    (dolist (p path)
      (setf (gethash p path-table) t))
    (dotimes (y height)
      (dotimes (x width)
        (let ((coord (cons x y)))
          (cond
            ((equal coord start-coord) (format t " S "))
            ((equal coord goal-coord)  (format t " G "))
            ((gethash coord path-table) (format t " * "))
            ((= (aref grid y x) 1)     (format t "###"))
            (t                         (format t " . ")))))
      (format t "~%"))))

;; --- Demonstration & Verification ---
(defun run-demo ()
  (format t "=================================================================~%")
  (format t "Common Lisp A* Heuristic Pathfinding Algorithm (2D Grid)~%")
  (format t "=================================================================~%~%")
  
  ;; 10x10 Grid with walls (1: Wall, 0: Open)
  (let ((grid (make-array '(8 12) :initial-contents
                          '((0 0 0 0 0 0 0 0 0 0 0 0)
                            (0 1 1 1 1 1 0 1 1 1 1 0)
                            (0 0 0 0 0 1 0 0 0 0 1 0)
                            (0 1 1 1 0 1 1 1 1 0 1 0)
                            (0 1 0 0 0 0 0 0 1 0 0 0)
                            (0 1 0 1 1 1 1 0 1 1 1 0)
                            (0 0 0 1 0 0 0 0 0 0 1 0)
                            (0 0 0 0 0 1 1 1 1 0 0 0))))
        (start '(0 . 0))
        (goal  '(11 . 7)))
    
    (format t "Finding optimal obstacle-avoidance path from ~A to ~A...~%" start goal)
    (let ((path (a-star-search grid start goal)))
      (if path
          (progn
            (format t "Optimal Path Found! Length: ~D steps~%" (length path))
            (print-grid-with-path grid path start goal)
            (format t "[SUCCESS] Common Lisp A* search found admissible optimal path.~%"))
          (format t "[FAILED] No path found.~%")))))

(run-demo)
