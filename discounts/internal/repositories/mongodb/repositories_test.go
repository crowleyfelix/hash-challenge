package mongodb

import (
	"discounts/internal/domain"
	"discounts/internal/testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("ProductRepository", func() {
	var (
		repo     = new(ProductRepository)
		fixtures []Product
	)

	BeforeEach(func() {
		if err := testing.LoadJson("fixtures/products.json", &fixtures); err != nil {
			Fail(err.Error())
		}

		loadFixtures(fixtures)
	})

	AfterEach(func() { disposeFixtures(fixtures) })

	Describe("finding a product by id", func() {
		var (
			id      string
			product *domain.Product
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
			BeforeEach(func() { id = fixtures[0].ID.Hex() })

			It("should return product", func() {
				Expect(err).To(BeNil())
				Expect(product.ID).To(Equal(fixtures[0].ID.Hex()))
			})
		})
	})
})

var _ = Describe("UserRepository", func() {
	var (
		repo     = new(UserRepository)
		fixtures []User
	)

	BeforeEach(func() {
		if err := testing.LoadJson("fixtures/users.json", &fixtures); err != nil {
			Fail(err.Error())
		}

		loadFixtures(fixtures)
	})

	AfterEach(func() { disposeFixtures(fixtures) })

	Describe("finding a user by id", func() {
		var (
			id   string
			user *domain.User
			err  error
		)

		JustBeforeEach(func() { user, err = repo.Find(id) })

		Context("when id is invalid", func() {
			BeforeEach(func() { id = "1234" })

			It("should return a error", func() {
				Expect(err).NotTo(BeNil())
				Expect(user).To(BeNil())
			})
		})

		Context("when user is found", func() {
			BeforeEach(func() { id = fixtures[0].ID.Hex() })

			It("should return user", func() {
				Expect(err).To(BeNil())
				Expect(user.ID).To(Equal(fixtures[0].ID.Hex()))
			})
		})
	})
})
