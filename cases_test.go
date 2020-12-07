package flightSpecExercise


var testCases = []struct {
	description string
	input		string
	length 		int
	location    string
	age 		int
	expected 	bool
}{
	{	
		description: "Amsterdam Flight Spec",
		input:		 "AMS 0 25 S E",
		length: 	 12,
		location:	 "Amsterdam",
		age:		 25,
		expected:	 true,
	},
	{
		description: "Glasgow Flight Spec",
		input:		 "GLA 1 15 V E",
		location:	 "Glasgow",
		age:		 15,
		length:	 	 12,
		expected:	 true,
	},
	{
		description: "Spec of incorrect length GLA",
		input:		 "GLA 1 15 VE",
		location:    "Glasgow",
		age: 		 15,
		length:	 	 11,
		expected:	 false,
	},
	{
		description: "Spec Location Incorrect",
		input:		 "GLA 1 35 VE",
		location:    "London",
		age:		 35,
		length:	 	 11,
		expected:	 false,
	},
	{
		description: "Spec Location correct",
		input:		 "GLA 1 -1 VE",
		location:    "Glasgow",
		age:		 -1,
		length:	 	 11,
		expected:	 false,
	},
	
}