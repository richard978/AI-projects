(define (problem boxman4)
	(:domain boxman_domain)
	(:objects Box1 Box2 Box3 - physob  P1 P2 P3 P4 P5 P6 P7 P8 P9 P10 P11 P12 P13 P14 P15 P16 P17 P18 P19 - loc)
	(:init (at P4)(locate Box1 P12)(locate Box3 P15)(locate Box2 P16)
		   (empty P1)(empty P2)(empty P3)(empty P5)(empty P6)(empty P7)(empty P8)(empty P9)(empty P10)(empty P11)(empty P13)
		   (empty P14)(empty P17)(empty P18)(empty P19)
		   (right P2 P1)(right P3 P2)(right P4 P3)(right P5 P4)(right P10 P9)(right P11 P10)(right P12 P11)(right P13 P12)
		   (right P15 P14)(right P16 P15)(right P17 P16)(right P19 P18)
		   (up P1 P6)(up P6 P9)(up P9 P14)(up P14 P18)(up P10 P15)(up P15 P19)(up P3 P7)(up P7 P11)(up P11 P16)
		   (up P12 P17)(up P5 P8)(up P8 P13)
		   
		  )
    (:goal (and(locate Box1 P3)(locate Box2 P7)(locate Box3 P14)))
	)








