package mymap

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestHashMap(t *testing.T) {
	var h HashMap[int]
	h.Add("wook", 100)

	val, ok := h.Get("wook")
	assert.True(t, ok)
	assert.Equal(t, 100, val)

	h.Add("golang", 200)

	val, ok = h.Get("golang")
	assert.True(t, ok)
	assert.Equal(t, 200, val)

	val, ok = h.Get("wook")
	assert.True(t, ok)
	assert.Equal(t, 100, val)

	h.Add("aw", 300)
	val, ok = h.Get("aw")
	assert.True(t, ok)
	assert.Equal(t, 300, val)
}

func  TestGoBasicMap(t *testing.T) {
	m := make(map[string]int)
	// var m map[string]int
	m["wook"] = 100
	
}