package mongodb

import (
	"discounts/internal/models"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("ProductRepository", func() {
	var (
		repo     = new(ProductRepository)
		fixtures []Product
	)

	BeforeEach(func() { loadFixtures("fixtures/products.json", fixtures) })

	AfterEach(func() { disposeFixtures(fixtures) })

	Describe("finding a product by id", func() {
		var (
			id      string
			product *models.Product
			err     error
		)

		JustBeforeEach(func() { product, err = repo.Find(id) })

		Context("when id is invalid", func() {
			BeforeEach(func() { id = "1234" })

			It("should return a error", func() {
				Expect(err).NotTo(BeNil())
				Expect(product).To(BeNil())
			})
		})

		Context("when product is found", func() {
			BeforeEach(func() { id = fixtures[0].ID.String() })

			It("should return product", func() {
				println(fixtures[0].ID.String())
				Expect(err).To(BeNil())
				Expect(product).NotTo(BeNil())
			})
		})
	})
})
