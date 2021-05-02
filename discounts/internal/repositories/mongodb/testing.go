package mongodb

import (
	"context"
	"discounts/internal/testing"

	"github.com/kamva/mgm/v3"
	. "github.com/onsi/ginkgo"
)

func loadFixtures(path string, fixtures interface{}) {
	if err := testing.LoadJson(path, &fixtures); err != nil {
		Fail(err.Error())
	}

	f, ok := fixtures.([]mgm.Model)
	if !ok {
		Fail("Invalid fixtures type")
	}

	coll := mgm.Coll(f[0])
	for i, _ := range f {
		ctx := context.TODO()

		r, err := coll.InsertOne(ctx, f[i])
		if err != nil {
			Fail(err.Error())
		}
		f[i].SetID(r.InsertedID)
	}
}

func disposeFixtures(fixtures interface{}) {
	f, ok := fixtures.([]mgm.Model)
	if !ok {
		Fail("Invalid fixtures type")
	}

	coll := mgm.Coll(f[0])
	for i, _ := range f {
		err := coll.Delete(f[i])
		if err != nil {
			Fail(err.Error())
		}
	}
}
