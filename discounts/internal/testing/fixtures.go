package testing

import (
	"encoding/json"
	"io/ioutil"
	"os"

	. "github.com/onsi/ginkgo"
)

func LoadJson(path string, result interface{}) {
	f, err := os.Open(path)
	if err != nil {
		Fail(err.Error())
	}
	defer f.Close()

	var blob []byte
	if blob, err = ioutil.ReadAll(f); err != nil {
		Fail(err.Error())
	}

	if err = json.Unmarshal(blob, result); err != nil {
		Fail(err.Error())
	}
}
