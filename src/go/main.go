package main

// #cgo CFLAGS: -I${SRCDIR}/c_includes/
// #cgo LDFLAGS: -L${SRCDIR}/c_build/ -ldice
// #include "shared_header.h"
// #include <stdlib.h>
import "C"

import (
	"fmt"
	"io/ioutil"
	"os"
	"unsafe"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	diceFile := "output.dice"
	toRoll := C.CString("1d20")
	outputFile := C.CString(diceFile)
	os.Remove(diceFile)
	C.roll_and_write(toRoll, outputFile)
	dat, err := ioutil.ReadFile(diceFile)
	check(err)
	fmt.Print(string(dat))
	C.free(unsafe.Pointer(toRoll))
	C.free(unsafe.Pointer(outputFile))
	os.Remove(diceFile)
}
