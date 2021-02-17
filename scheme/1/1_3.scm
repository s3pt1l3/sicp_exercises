#lang scheme

(define (square x) (* x x))

(define (square_sum x y) (+ (square x) (square y)))
(define (x a b c)
  (cond ((and (>= (+ a b) (+ b c)) (>= (+ a b) (+ a c))) (square_sum a b)) 
         ((and (>= (+ a c) (+ b c)) (>= (+ a c) (+ a b))) (square_sum a c)) 
         (else (square_sum b c))))
