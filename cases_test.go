package FlightSpecExercise


var testCases = []struct {
	description string
	input		string
	cost		float32
	location	string
	expected    bool
}{
	{	
		description: "Amsterdam Flight Spec",
		input:		 "AMS 0 25 S E",
		cost:		 160.00,
		location:	 "Amsterdam",
		expected: 	 true,
	},
	{
		description: "Glasgow Flight Spec",
		input:		 "GLA 1 15 V E",
		cost:		 42.50,
		location:	 "Glasgow",
		expected:	 true,
	},
	
}