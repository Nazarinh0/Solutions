(define (square x) (* x x))

(define (good-enough? guess x)
  (= guess (improve guess x)))

(define (improve guess x)
  (/
   (+ (/ x (square guess)) (* 2 guess))
   3))

(define (cubic-root-iter guess x)
  (if (good-enough? guess x)
      guess
      (cubic-root-iter (improve guess x) x)))

(define (cube-root x)
  (cubic-root-iter 1.0 x))