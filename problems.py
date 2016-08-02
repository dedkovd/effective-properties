# -*- coding: utf-8 -*- 

from enums import *

defects = {
		EDefect.Regular: 
		{
			"id": EDefect.Regular,
			"name": "Идеальная периодическая структура",
			"folder": "regular",
			"append_matrix": 0,
		},
		EDefect.Fiber_Skip:
		{
			"id": EDefect.Fiber_Skip,
			"name": "Пропуск волокна основы",
			"folder": "d1",
			"append_matrix": 1,
		},
		EDefect.Fiber_Skip_Matrix:
		{
			"id": EDefect.Fiber_Skip_Matrix,
			"name": "Пропуск волокна основы с доуплотнением",
			"folder": "d2",
			"append_matrix": 2,
		},
		EDefect.One_Fiber_Break:
		{
			"id": EDefect.One_Fiber_Break,
			"name": "Разрыв волокна основы",
			"folder": "d3",
			"append_matrix": 1,
		},
		EDefect.One_Fiber_Break_Matrix:
		{
			"id": EDefect.One_Fiber_Break_Matrix,
			"name": "Разрыв волокна основы с доуплотнением",
			"folder": "d4",
			"append_matrix": 2,
		},
		EDefect.Two_Fibers_Break:
		{
			"id": EDefect.Two_Fibers_Break,
			"name": "Разрыв волокон основы и утка",
			"folder": "d5",
			"append_matrix": 1,
		},
		EDefect.Two_Fibers_Break_Matrix:
		{
			"id": EDefect.Two_Fibers_Break_Matrix,
			"name": "Разрыв волокон основы и утка с доуплотнением",
			"folder": "d6",
			"append_matrix": 2,
		},
		EDefect.Pore:
		{
			"id": EDefect.Pore,
			"name": "Внутренняя технологическая пора",
			"folder": "d7",
			"append_matrix": 1,
		},
	}

phases = (
		{
			"id": EPhase.Matrix,
			"name": "Матрица",
			"suffix": "matrix",
		},
		{
			"id": EPhase.Fibers,
			"name": "Волокна",
			"suffix": "fibers",
		}
	)

schemas = {
		ESchema.X1X3_Tension:
		{
			"id": ESchema.X1X3_Tension,
			"name": "Двухстороннее равнокомпонентное растяжение в плоскости слоя",
			"folder": "s0",
		},
		ESchema.X1_Tension:
		{
			"id": ESchema.X1_Tension,
			"name": "Растяжение вдоль волокон основы",
			"folder": "s1",
		},
		ESchema.X1_Tension_X3_Compression:
		{
			"id": ESchema.X1_Tension_X3_Compression,
			"name": "Чистое формоизменение",
			"folder": "s2",
		},
		ESchema.X1X3_Compression:
		{
			"id": ESchema.X1X3_Compression,
			"name": "Двухстороннее равнокомпонентное сжатие в плоскости слоя",
			"folder": "s3",
		},
		ESchema.X1_Compression:
		{
			"id": ESchema.X1_Compression,
			"name": "Сжатие вдоль волокон основы",
			"folder": "s4",
		},
		ESchema.X1X3_Unequal_Compression:
		{
			"id": ESchema.X1X3_Unequal_Compression,
			"name": "Двухстороннее неравнокомпонентное сжатие в плоскости слоя",
			"folder": "s5",
		},
	}

effective_schemas = {
			ESchema.X1_Tension:
			{
				"id": ESchema.X1_Tension,
				"name": "Растяжение вдоль волокон основы",
				"folder": "x1",
                                "index": 1
			},
			ESchema.X3_Tension:
			{
				"id": ESchema.X3_Tension,
				"name": "Растяжение вдоль волокон утка",
				"folder": "x3",
                                "index": 2
			},
			ESchema.X1X3_Tension:
			{
				"id": ESchema.X1X3_Tension,
				"name": "Растяжение вдоль волокон основы и утка",
				"folder": "x1x3",
                                "index": 1
			},
			ESchema.X1_Tension_X3_Compression:
			{
				"id": ESchema.X1_Tension_X3_Compression,
				"name": "Чистое формоизменение",
				"folder": "x1mx3",
                                "index": 2
			}	
		}

problems = (
		{
			"id": EProblem.CC_Without_Contact,
			"name": "Углерод - Углерод без контакта",
			"folder": "p0",
			"schemas": 
			(
				ESchema.X1X3_Tension, 
				ESchema.X1_Tension, 
				ESchema.X1_Tension_X3_Compression,
			),
			"defects":
			(
				EDefect.Regular,
				EDefect.Fiber_Skip,
				EDefect.Fiber_Skip_Matrix,
				EDefect.One_Fiber_Break,
				EDefect.One_Fiber_Break_Matrix,
				EDefect.Two_Fibers_Break,
				EDefect.Two_Fibers_Break_Matrix,
				EDefect.Pore,
			),
		},
		{
			"id": EProblem.CC_With_Contact,
			"name": "Углерод - Углерод с контактом",
			"folder": "p1",
			"schemas": 
			(
				ESchema.X1X3_Tension,
				ESchema.X1_Tension,
				ESchema.X1_Tension_X3_Compression,
			),
			"defects":
			(
				EDefect.Regular,
				EDefect.Fiber_Skip,
				EDefect.Fiber_Skip_Matrix,
				EDefect.One_Fiber_Break,
				EDefect.One_Fiber_Break_Matrix,
				EDefect.Two_Fibers_Break,
				EDefect.Two_Fibers_Break_Matrix,
			),
		},
		{
			"id": EProblem.CS_Without_Contact,
			"name": "Углерод - Сталь без контакта",
			"folder": "p2",
			"schemas": 
			(
				ESchema.X1X3_Compression,
				ESchema.X1_Compression,
				ESchema.X1X3_Unequal_Compression,
			),
			"defects":
			(
				EDefect.Regular,
				EDefect.Fiber_Skip,
				EDefect.Fiber_Skip_Matrix,
				EDefect.One_Fiber_Break,
				EDefect.One_Fiber_Break_Matrix,
				EDefect.Two_Fibers_Break,
				EDefect.Two_Fibers_Break_Matrix,
				EDefect.Pore,
			),
		},
		{
			"id": EProblem.CS_With_Contact,
			"name": "Углерод - Сталь с контактом",
			"folder": "p3",
			"schemas":
			(
				ESchema.X1X3_Compression,
				ESchema.X1_Compression,
				ESchema.X1X3_Unequal_Compression,
			),
			"defects":
			(
				EDefect.Regular,
				EDefect.Fiber_Skip,
				EDefect.Fiber_Skip_Matrix,
				EDefect.One_Fiber_Break,
				EDefect.One_Fiber_Break_Matrix,
				EDefect.Two_Fibers_Break,
				EDefect.Two_Fibers_Break_Matrix,
			),
		},
		{
			"id": EProblem.CC_Without_Contact_Big,
			"name": "Углерод - Углерод без контакта увеличенная площадь",
			"folder": "p4",
			"schemas":
			(
				ESchema.X1X3_Tension,
			),
			"defects":
			(
				EDefect.Regular,
				EDefect.Fiber_Skip,
				EDefect.Fiber_Skip_Matrix,
				EDefect.One_Fiber_Break,
				EDefect.One_Fiber_Break_Matrix,
				EDefect.Two_Fibers_Break,
				EDefect.Two_Fibers_Break_Matrix,
			),
		},
	)
