package flightSpecExercise


var testCases = []struct {
	description string
	input		string
	length 		int
	location    string
	expected 	bool
}{
	{	
		description: "Amsterdam Flight Spec",
		input:		 "AMS 0 25 S E",
		length: 	 12,
		location:	 "Amsterdam",
		expected:	 true,
	},
	{
		description: "Glasgow Flight Spec",
		input:		 "GLA 1 15 V E",
		location:	 "Glasgow",
		length:	 	 12,
		expected:	 true,
	},
	{
		description: "Spec of incorrect length GLA",
		input:		 "GLA 1 15 VE",
		location:    "Glasgow",
		length:	 	 11,
		expected:	 false,
	},
	{
		description: "Spec Location Incorrect",
		input:		 "GLA 1 15 VE",
		location:    "London",
		length:	 	 11,
		expected:	 false,
	},
	{
		description: "Spec Location correct",
		input:		 "GLA 1 15 VE",
		location:    "Glasgow",
		length:	 	 11,
		expected:	 false,
	},
	
}