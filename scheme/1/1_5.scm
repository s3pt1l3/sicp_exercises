#lang scheme

(define (p) (p))
(define (test x y)
  (if (= x 0)
  0
  y))
(test 0 (p))

;If the interpreter uses the applicative order, we will not enter the test procedure because of the infinite recursive call to the procedure p.
;If the interpreter uses normal ordering, we get 0 in the output.
