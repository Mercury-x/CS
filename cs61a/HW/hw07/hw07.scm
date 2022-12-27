(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? asc-lst)
  (cond 
    ((null? asc-lst)
     #t) ; empty list
    ((null? (cdr asc-lst))
     #t) ; length = 1
    ((<= (car asc-lst) (cadr asc-lst))
     (ascending? (cdr asc-lst)))
    ((> (car asc-lst) (cadr asc-lst))
     #f)))

(define (square n) (* n n))

(define (pow base exp)
  (cond 
    ((= exp 1)         base)
    ((odd? exp)  (* base (pow base (- exp 1))))
    ((even? exp) (square (pow base (/ exp 2))))))
