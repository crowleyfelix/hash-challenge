package mongodb

import (
	"context"
	"reflect"

	"github.com/kamva/mgm/v3"
	. "github.com/onsi/ginkgo"
)

func loadFixtures(fixtures interface{}) {
	for _, m := range toModelSlice(fixtures) {
		ctx := context.TODO()
		coll := mgm.Coll(m)

		r, err := coll.InsertOne(ctx, m)
		if err != nil {
			Fail(err.Error())
		}
		m.SetID(r.InsertedID)
	}
}

func disposeFixtures(fixtures interface{}) {
	for _, m := range toModelSlice(fixtures) {
		coll := mgm.Coll(m)

		err := coll.Delete(m)
		if err != nil {
			Fail(err.Error())
		}
	}
}

func toModelSlice(v interface{}) []mgm.Model {
	switch reflect.TypeOf(v).Kind() {
	case reflect.Slice:
		s := reflect.ValueOf(v)

		ms := make([]mgm.Model, 0)

		for i := 0; i < s.Len(); i++ {
			ms = append(ms, s.Index(i).Addr().Interface().(mgm.Model))
		}

		return ms
	}

	return nil
}
