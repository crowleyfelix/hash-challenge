package services

import (
	"discounts/internal/infrastructure"
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestServices(t *testing.T) {
	infrastructure.SetUpDB()
	RegisterFailHandler(Fail)
	RunSpecs(t, "Services Suite")
}
