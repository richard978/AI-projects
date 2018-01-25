(define (problem boxman5)
	(:domain boxman_domain)
	(:objects Box1 Box2 Box3 - physob  P1 P2 P3 P4 P5 P6 P7 P8 P9 P10 P11 P12 P13 P14 P15 P16 P17 P18 P19 P20 - loc)
	(:init (at P20)(locate Box1 P17)(locate Box2 P11)(locate Box3 P7)
		   (empty P1)(empty P2)(empty P3)(empty P4)(empty P5)(empty P6)(empty P8)(empty P9)(empty P10)
		   (empty P12)(empty P13)(empty P14)(empty P15)(empty P16)(empty P18)(empty P19)
		   (up P1 P3)(up P3 P5)(up P2 P4)(up P4 P6)(up P6 P11)(up P11 P16)(up P16 P18)(up P7 P12)
		   (up P8 P13)(up P13 P17)(up P17 P20)(up P9 P14)(up P10 P15)
		   (right P2 P1)(right P4 P3)(right P6 P5)(right P7 P6)(right P8 P7)(right P9 P8)(right P10 P9)
		   (right P12 P11)(right P13 P12)(right P14 P13)(right P15 P14)(right P19 P18)(right P20 P19)
		  )
    (:goal (and (locate Box1 P18)(locate Box2 P6)(locate Box3 P7))
	)

)