package flightSpecExercise


var testCases = []struct {
	description string
	input		string
	length 		int
	location    string
	age 		int
	meal    	string
	expected 	bool
}{
	{	
		description: "Amsterdam Flight Spec",
		input:		 "AMS 0 25 S E",
		length: 	 12,
		location:	 "Amsterdam",
		age:		 25,
		meal:		 "Standard",
		expected:	 true,
	},
	{
		description: "Glasgow Flight Spec",
		input:		 "GLA 1 15 V E",
		location:	 "Glasgow",
		age:		 15,
		meal: 		 "Vegetarian",
		length:	 	 12,
		expected:	 true,
	},
	{
		description: "Spec of incorrect length GLA",
		input:		 "GLA 1 15 VE",
		location:    "Glasgow",
		age: 		 15,
		meal:		 "Vegetarian",
		length:	 	 11,
		expected:	 false,
	},
	{
		description: "Spec Location Incorrect",
		input:		 "GLA 1 35 NE",
		location:    "London",
		age:		 35,
		meal:		 "None",
		length:	 	 11,
		expected:	 false,
	},
	{
		description: "Negative age test",
		input:		 "GLA 1 -1 V E",
		location:    "Glasgow",
		age:		 -1,
		meal:		 "Vegetarian",
		length:	 	 11,
		expected:	 false,
	},
	{
		description: "Vegetarian Meal test",
		input:		 "GLA 1 50 V E",
		location:    "Glasgow",
		age:		 50,
		meal:	     "Vegetarian",
		length:	 	 11,
		expected:	 false,
	},
	{
		description: "No meal test",
		input:		 "GLA 1 50 N E",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "None",
		length:	 	 12,
		expected:	 false,
	},
	{
		description: "Standard meal test",
		input:		 "GLA 1 50 S E",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "Standard",
		length:	 	 12,
		expected:	 false,
	},
	{
		description: "Incorrect symbol for meal test",
		input:		 "GLA 1 50 F E",
		location:    "Glasgow",
		age:		 50,
		meal: 		 "This symbol does not represent any meal",
		length:	 	 12,
		expected:	 false,
	},

}