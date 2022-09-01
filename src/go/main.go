package main
// #cgo CFLAGS: -I${SRCDIR}/c_includes/
// #cgo LDFLAGS: -L${SRCDIR}/c_build/ -ldice
// #include "shared_header.h"
// #include <stdlib.h>
import "C"
import "fmt"
import "os"
import "unsafe"

func check(e error){
  if e!=nil{
     panic(e)
  }
}

func main(){
    dice_file := "output.dice"
    to_roll := C.CString("1d20")
    output_file := C.CString(dice_file)
    os.Remove(dice_file)
    C.roll_and_write(to_roll, output_file);
    dat, err := os.ReadFile(dice_file)
    check(err)
    fmt.Print(string(dat))
    C.free(unsafe.Pointer(to_roll))
    C.free(unsafe.Pointer(output_file))
    os.Remove(dice_file)
}   
