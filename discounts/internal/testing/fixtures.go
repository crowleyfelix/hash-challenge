package testing

import (
	"encoding/json"
	"io/ioutil"
	"os"
)

func LoadJson(path string, result interface{}) error {
	f, err := os.Open(path)
	if err != nil {
		return err
	}
	defer f.Close()

	var blob []byte
	if blob, err = ioutil.ReadAll(f); err != nil {
		return err
	}

	if err = json.Unmarshal(blob, result); err != nil {
		return err
	}

	return err
}
