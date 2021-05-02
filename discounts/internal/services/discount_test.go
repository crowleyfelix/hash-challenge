package services

import (
	"context"
	"discounts/internal/repositories/mongodb"
	"discounts/internal/testing"
	"discounts/internal/utils"
	"discounts/proto"
	"time"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("ProductRepository", func() {
	var (
		svc      proto.DiscountCalculatorServer
		products []mongodb.Product
		users    []mongodb.User
	)

	BeforeEach(func() {
		svc = NewDiscountCalculator()

		if err := testing.LoadJson("fixtures/products.json", &products); err != nil {
			Fail(err.Error())
		}

		if err := testing.LoadJson("fixtures/users.json", &users); err != nil {
			Fail(err.Error())
		}
	})

	JustBeforeEach(func() {
		mongodb.LoadFixtures(products)
		mongodb.LoadFixtures(users)
	})

	AfterEach(func() {
		mongodb.DisposeFixtures(products)
		mongodb.DisposeFixtures(users)
	})

	Describe("calculating a discount", func() {
		var (
			req  *proto.CalculateRequest
			resp *proto.CalculateResponse
			err  error
		)

		JustBeforeEach(func() { resp, err = svc.Calculate(context.TODO(), req) })

		Context("when product does not exist", func() {
			BeforeEach(func() { req = &proto.CalculateRequest{ProductId: "1234", UserId: users[0].ID.Hex()} })

			It("should return a error", func() {
				Expect(err).NotTo(BeNil())
				Expect(resp).To(BeNil())
			})
		})

		Context("when user does not exist", func() {
			BeforeEach(func() { req = &proto.CalculateRequest{ProductId: products[0].ID.Hex(), UserId: "1234"} })

			It("should return product", func() {
				Expect(err).NotTo(BeNil())
				Expect(resp).To(BeNil())
			})
		})

		Context("when user and product exists", func() {
			var (
				product *mongodb.Product
				user    *mongodb.User
			)

			BeforeEach(func() {
				product = &products[0]
				user = &users[0]

				req = &proto.CalculateRequest{ProductId: product.ID.Hex(), UserId: user.ID.Hex()}
			})

			Context("and no rule is appliable", func() {
				BeforeEach(func() {
					m, _ := time.Parse(time.RFC3339, "2021-01-01T00:00:00+00:00")
					utils.MockedNow = &m

					bd, _ := time.Parse(time.RFC3339, "1990-10-26T00:00:00+00:00")
					product.PriceInCents = 5000
					user.DateOfBirth = bd
				})

				AfterEach(func() { utils.MockedNow = nil })

				It("should not return a discount", func() {
					Expect(err).To(BeNil())
					Expect(resp.Product.Discount).To(BeNil())
				})
			})

			Context("and is black friday", func() {
				BeforeEach(func() {
					m, _ := time.Parse(time.RFC3339, "2021-11-25T00:00:00+00:00")
					utils.MockedNow = &m

					bd, _ := time.Parse(time.RFC3339, "1990-10-26T00:00:00+00:00")
					product.PriceInCents = 5000
					user.DateOfBirth = bd
				})

				AfterEach(func() { utils.MockedNow = nil })

				It("should return blackfriday discount", func() {
					Expect(err).To(BeNil())
					Expect(resp.Product.Discount).ToNot(BeNil())
					Expect(resp.Product.Discount.Percentage).To(Equal(float32(0.1)))
				})
			})

			Context("and is user birthday", func() {
				BeforeEach(func() {
					m, _ := time.Parse(time.RFC3339, "2021-10-26T00:00:00+00:00")
					utils.MockedNow = &m

					bd, _ := time.Parse(time.RFC3339, "1990-10-26T00:00:00+00:00")
					product.PriceInCents = 5000
					user.DateOfBirth = bd
				})

				AfterEach(func() { utils.MockedNow = nil })

				It("should return birthday discount", func() {
					Expect(err).To(BeNil())
					Expect(resp.Product.Discount).ToNot(BeNil())
					Expect(resp.Product.Discount.Percentage).To(Equal(float32(0.05)))
				})
			})

			Context("and discounts exceeds limit", func() {
				BeforeEach(func() {
					m, _ := time.Parse(time.RFC3339, "2021-11-25T00:00:00+00:00")
					utils.MockedNow = &m

					bd, _ := time.Parse(time.RFC3339, "1990-11-25T00:00:00+00:00")
					product.PriceInCents = 5000
					user.DateOfBirth = bd
				})

				AfterEach(func() { utils.MockedNow = nil })

				It("should return limit discount", func() {
					Expect(err).To(BeNil())
					Expect(resp.Product.Discount).ToNot(BeNil())
					Expect(resp.Product.Discount.Percentage).To(Equal(float32(0.1)))
				})
			})
		})

	})
})
