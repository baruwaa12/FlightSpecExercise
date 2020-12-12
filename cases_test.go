package flightSpecExercise


var testCases = []struct {
	description string
	input		string
	length 		int
	location    string
	age 		int
	meal    	string
	expected 	bool
	seating 	string
	baggage 	int
	spacing		bool
}{
	{	
		description: "Amsterdam Flight Spec",
		input:		 "AMS 0 25 S E",
		length: 	 12,
		location:	 "Amsterdam",
		age:		 25,
		meal:		 "Standard",
		seating:  	 "Economy",
		expected:	 true,
		baggage:	 0,
		spacing:	 true,
	},
	{
		description: "Glasgow Flight Spec",
		input:		 "GLA 2 15 V E",
		location:	 "Glasgow",
		age:		 15,
		meal: 		 "Vegetarian",
		seating:  	 "Economy",
		length:	 	 12,
		expected:	 true,
		baggage:	 2,
		spacing:	 true,

	},
	{
		description: "Spec of incorrect length GLA",
		input:		 "GLA 3 15 VE",
		location:    "Glasgow",
		age: 		 15,
		meal:		 "Vegetarian",
		seating:  	 "Economy",
		length:	 	 11,
		expected:	 false,
		baggage:	 3,
		spacing:	 true,

	},
	{
		description: "Spec Location Incorrect",
		input:		 "GLA 5 35 N E",
		location:    "London",
		age:		 35,
		meal:		 "None",
		seating:	 "Economy",
		length:	 	 12,
		expected:	 false,
		baggage:	 5,
		spacing:	 true,
		
	},
	{
		description: "Negative age test",
		input:		 "GLA 4 -1 V E",
		location:    "Glasgow",
		age:		 -1,
		meal:		 "Vegetarian",
		seating:  	 "Economy",
		length:	 	 12,
		expected:	 false,
		baggage:	 4,
		spacing:	 true,

	},
	{
		description: "Vegetarian Meal test",
		input:		 "GLA 2 50 V E",
		location:    "Glasgow",
		age:		 50,
		meal:	     "Vegetarian",
		seating:  	 "Economy",
		length:	 	 12,
		expected:	 false,
		baggage:	 2,
		spacing:	 true,


	},
	{
		description: "No meal test",
		input:		 "GLA 1 50 N E",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "None",
		seating:  	 "Economy",
		length:	 	 12,
		expected:	 false,
		baggage:	 1,
		spacing:	 true,

	},
	{
		description: "Standard meal test",
		input:		 "GLA 1 50 S E",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "Standard",
		seating:  	 "Economy",
		length:	 	 12,
		expected:	 false,
		baggage:	 1,
		spacing:	 true,

	},
	{
		description: "Incorrect symbol for meal test",
		input:		 "GLA 1 50 F E",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "This symbol does not represent any meal",
		seating:  	 "Economy",
		length:	 	 12,
		expected:	 false,
		baggage:	 1,
		spacing:	 true,
	},
	{
		description: "Economy symbol for economy class seating test",
		input:		 "GLA 1 50 F E",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "This symbol does not represent any meal ",
		seating:  	 "Economy",
		length:	 	 12,
		expected:	 false,
		baggage: 	 1,
		spacing:	 true,
	},
	{
		description: "First class symbol for first class seating test",
		input:		 "GLA 1 50 F F",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "This symbol does not represent any meal",
		seating:  	 "First Class",
		length:	 	 12,
		expected:	 false,
		baggage:     1,
		spacing:	 true,
	},
	{
		description: "Incorrect symbol for seating class",
		input:		 "GLA 2 50 F D",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "This symbol does not represent any meal",
		seating:  	 "This is not a valid class",
		length:	 	 12,
		expected:	 false,
		baggage: 	 2,
		spacing:	 true,
	},
	{
		description: "One baggage for the customer",
		input:		 "GLA 1 50 F D",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "This symbol does not represent any meal",
		seating:  	 "This is not a valid class",
		length:	 	 12,
		expected:	 false,
		baggage:	 1,
		spacing:	 true,
	},
	{
		description: "No baggage for this customer",
		input:		 "GLA 0 50 F D",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "This symbol does not represent any meal",
		seating:  	 "This is not a valid class",
		length:	 	 12,
		expected:	 false,
		baggage:	 0,
		spacing:	 true,
	},
	{
		description: "No baggage for this customer",
		input:		 "GLA 0 50 F D",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "This symbol does not represent any meal",
		seating:  	 "This is not a valid class",
		length:	 	 12,
		expected:	 false,
		baggage:	 0,
		spacing:	 true,
	},
	
	


}