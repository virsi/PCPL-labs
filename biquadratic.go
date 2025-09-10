package main

import (
	"errors"
	"fmt"
	"os"
)

func inputCoefficients() [3]int {
	coefficients := [3]int{}
	fmt.Println("Введите коэффициенты А, В и С")
	for i:=0; i < 3; i++ {
		fmt.Printf("Коэффициент %c: ", 'A' + i)
		fmt.Scanln(&coefficients[i])
	}
	return coefficients
}

func solveBiquadratic(a, b, c int) ([]int, error) {
	result := []int{}
	if a == 0 {
		if b == 0 {
			if c == 0 {
				err := errors.New("Любое число")
				return nil, err
			} else {
				return nil, nil
			}
		}
	}
	return result, nil
}

func main(){
	args := os.Args[1:]
	if len(args) != 3 {
		coefficients := inputCoefficients()
		fmt.Println(coefficients)
	}

}
