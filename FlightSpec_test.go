package FlightSpecExercise

import (
	"testing"
)

func TestFlightSpec(t * testing.T) {
	for _, test := range testCases {
		if actual := FlightSpecCheck(test.input); actual != test.expected {
			t.Fatalf("FAIL [%s]", test.description)
		}
		t.Logf("PASS: %s", test.description)

	}
}

