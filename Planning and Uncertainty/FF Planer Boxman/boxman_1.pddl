(define (problem boxman1)
	(:domain boxman_domain)
	(:objects Box1 Box2 Box3 Box4 - physob  P1 P2 P3 P4 P5 P6 P7 P8 P9 P10 P11 P12 - loc)
	(:init (at P10)(locate Box1 P3)(locate Box2 P5)(locate Box3 P9)(locate Box4 P11)
		   (empty P1)(empty P2)(empty P4)(empty P6)(empty P7)(empty P8)(empty P12)
		   (up P1 P2)(up P2 P3)(up P3 P9)(up P4 P10)(up P10 P11)(up P11 P12)	
		   (right P4 P3)(right P5 P4)(right P6 P5)(right P8 P7)(right P9 P8)(right P10 P9)
		   
		  )
    (:goal (and (locate Box1 P1)(locate Box2 P6)(locate Box3 P7)(locate Box4 P12))
	)

)
