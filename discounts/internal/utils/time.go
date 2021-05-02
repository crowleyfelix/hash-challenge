package utils

import "time"

var MockedNow *time.Time

func Now() time.Time {
	if MockedNow != nil {
		return *MockedNow
	}

	return time.Now()
}
