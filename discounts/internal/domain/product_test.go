package domain

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

type calculatorMock struct{ should bool }

func (m *calculatorMock) Calculate(price int64) *Discount {
	if !m.should {
		return nil
	}

	perc := float32(0.05)
	return &Discount{
		Percentage:   0.05,
		ValueInCents: int64(float32(price) * perc),
	}
}

var _ = Describe("Product", func() {
	var (
		product Product
	)

	BeforeEach(func() { product = Product{PriceInCents: 100} })

	Describe("applying a discount", func() {
		var (
			discount *Discount
		)

		JustBeforeEach(func() { discount = product.Discount() })

		Context("when no rule is appliable", func() {
			BeforeEach(func() { product.AddCalculators(&calculatorMock{false}) })

			It("should not return a discount", func() {
				Expect(discount).To(BeNil())
			})
		})

		Context("when one rule is appliable", func() {
			BeforeEach(func() { product.AddCalculators(&calculatorMock{false}, &calculatorMock{true}) })

			It("should not return a discount", func() {
				Expect(discount).ToNot(BeNil())
				Expect(discount.Percentage).To(BeEquivalentTo(float32(0.05)))
				Expect(discount.ValueInCents).To(BeEquivalentTo(5))
			})
		})

		Context("when two rules is appliable", func() {
			BeforeEach(func() { product.AddCalculators(&calculatorMock{true}, &calculatorMock{true}) })

			It("should not return a discount", func() {
				Expect(discount).ToNot(BeNil())
				Expect(discount.Percentage).To(BeEquivalentTo(float32(0.1)))
				Expect(discount.ValueInCents).To(BeEquivalentTo(10))
			})
		})

		Context("when max discount exceeded", func() {
			BeforeEach(func() {
				product.AddCalculators(&calculatorMock{true}, &calculatorMock{true}, &calculatorMock{true}, &calculatorMock{true})
			})

			It("should return a max discount", func() {
				Expect(discount).ToNot(BeNil())
				Expect(discount.Percentage).To(BeEquivalentTo(float32(0.1)))
				Expect(discount.ValueInCents).To(BeEquivalentTo(10))
			})
		})
	})
})
