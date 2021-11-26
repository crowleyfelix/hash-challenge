package domain

import "time"

type User struct {
	ID          string
	FirstName   string
	LastName    string
	DateOfBirth time.Time
	Location    string
}
