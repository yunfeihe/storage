#lang sicp

(define (atom? item)
  (and (not (pair? item))

       ))

(define (deriv exp var)
  (cond ((constant? exp var) 0)
        ((same-var? exp var) 1)
        ((sum? exp)
         (make-sum (deriv (add exp) var)
                   (deriv (added exp) var)))
        ((product? exp)
         (make-sum
          (make-product (deriv (m1 exp) var)
                        (m2 exp))
          (make-product (m1 exp)
                        (deriv (m2 exp) var))))
        ))

(define (constant? exp var)
  (and (atom? exp)
       (not (eq? exp var))))

(define (same-var? exp var)
  (and (atom? exp)
       (eq? exp var)))

(define (sum? exp)
  (and (not (atom? exp))
       (eq? (car exp) '+)))

(define (make-sum a b)
  (cond ((and (number? a)
              (number? b)) (+ a b))
        ((and (eq? a 0)
              (atom? b)) b)
        ((and (eq? b 0)
              (atom? a)) a)
        (else (list '+ a b))))

(define add cadr)
(define added caddr)

(define (product? exp)
  (and (not (atom? exp))
       (eq? (car exp) '*)))

(define (make-product a b)
  (cond ((and (number? a)
              (number? b)) (* a b))
        ((and (eq? a 1)
              (atom? b)) b)
        ((and (eq? a 0)
              (atom? b)) nil)
        ((and (eq? b 1)
              (atom? a)) a)
        ((and (eq? b 0)
              (atom? a)) nil)
        (else (list '* a b))))

(define m1 cadr)

(define m2 caddr)

(define foo '(+ (* a (* x x))
                (+ (* b x)
                   c)))

(deriv foo 'a)

