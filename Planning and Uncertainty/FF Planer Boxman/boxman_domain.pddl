(define (domain boxman_domain)
	(:requirements :strips :equality :typing
		       :universal-preconditions
		       :conditional-effects)
	(:types physob loc)
	(:predicates
		(locate ?x - physob ?y - loc)
		(at ?x - loc )
		(right ?x - loc ?y - loc)
		(up ?x - loc ?y - loc)
		(empty ?x -loc)
		)
	(:action move 
		:parameters(?x - loc ?y - loc)
		:precondition(and (empty ?y)(at ?x)(or (right ?x ?y)(right ?y ?x)(up ?x ?y)(up ?y ?x)))
		:effect(and (empty ?x)(at ?y)(not(empty ?y))(not(at ?x)))
		
	)
	(:action moveBoxRight
		:parameters(?box - physob ?x - loc ?y - loc ?z - loc)
		:precondition(and (empty ?z)(at ?x)(locate ?box ?y)(right ?y ?x)(right ?z ?y))
		:effect(and (empty ?x)(at ?y)(locate ?box ?z)(not (at ?x))(not (empty ?z))(not (locate ?box ?y)))
	)
	(:action moveBoxLeft
		:parameters(?box - physob ?x - loc ?y - loc ?z - loc)
		:precondition(and (empty ?z)(at ?x)(locate ?box ?y)(right ?x ?y)(right ?y ?z))
		:effect(and (empty ?x)(at ?y)(locate ?box ?z)(not (at ?x))(not (empty ?z))(not (locate ?box ?y)))
	
	)
	(:action moveBoxUp
		:parameters(?box - physob ?x - loc ?y - loc ?z - loc)
		:precondition(and (empty ?z)(at ?x)(locate ?box ?y)(up ?y ?x)(up ?z ?y))
		:effect(and(empty ?x)(at ?y)(locate ?box ?z)(not (at ?x))(not (empty ?z))(not(locate ?box ?y)))
	)
	(:action moveBoxDown
		:parameters(?box - physob ?x - loc ?y - loc ?z - loc)
		:precondition(and (empty ?z)(at ?x)(locate ?box ?y)(up ?x ?y)(up ?y ?z ))
		:effect(and (empty ?x)(at ?y)(locate ?box ?z)(not (at ?x))(not (empty ?z))(not (locate ?box ?y)))
	)



)
