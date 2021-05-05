package mongodb

import (
	"discounts/internal/infrastructure"
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestMongoDB(t *testing.T) {
	infrastructure.SetUpDB()
	RegisterFailHandler(Fail)
	RunSpecs(t, "MongoDB Suite")
}
