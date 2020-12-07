package flightSpecExercise

import (
	"testing"
)

func TestFlightSpec(t * testing.T) {
	for _, test := range testCases {
		if actual := SpecLength(test.input); actual != test.expected {
			t.Fatalf("FAIL [%s]", test.description)
		}
		t.Logf("PASS: %s", test.description)

	}
}

func TestLocationFinder(t * testing.T) {
	for _, test := range testCases {
		if actual := LocationFinder(test.input); actual != test.location {
			t.Fatalf("FAIL [%s]", test.description)
		}
		t.Logf("PASS: %s", test.description)
	}
}

