package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type Shape int

const (
	Rock Shape = iota
	Paper
	Scissors
)

var Shapes = []Shape {
    Rock, Paper, Scissors,
}

var mapping1 = map[string]Shape{
	"A": Rock,
	"B": Paper,
	"C": Scissors,
}

var mapping2 = map[string]Shape{
	"X": Rock,
	"Y": Paper,
	"Z": Scissors,
}

var score = map[Shape]int{
	Rock:     1,
	Paper:    2,
	Scissors: 3,
}

var wins = map[Shape]Shape{
    Rock: Scissors,
    Paper: Rock,
    Scissors: Paper,
}

func main() {
	f, err := os.Open("02.input")
	if err != nil {
		log.Fatalln("Error opening file", err)
	}
	defer f.Close()

	var totalScoreV1 int = 0
	var totalScoreV2 int = 0
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, " ")
		shape1 := mapping1[parts[0]]
		shape2 := mapping2[parts[1]]
        shape2ByStrategy := shapeByStrategy(shape1, parts[1])
		totalScoreV1 += score[shape2] + 3 * result(shape2, shape1)
		totalScoreV2 += score[shape2ByStrategy] + 3 * result(shape2ByStrategy, shape1)
	}
	fmt.Println("Total score (v1): ", totalScoreV1)
	fmt.Println("Total score (v2): ", totalScoreV2)
}

func result(shape1 Shape, shape2 Shape) int {
	var result = 0
	if shape1 == shape2 {
		result = 1
	} else if shape2 == wins[shape1] {
        result = 2
    } else {
        result = 0
    }
	return result
}

func shapeByStrategy(otherShape Shape, strategy string) Shape {
    if strategy == "Y" {
        return otherShape
    } else if strategy == "Z" {
        return willWin(otherShape)
    } else {
        winningShape := willWin(otherShape)
        for _, s := range Shapes {
            if s != otherShape && s != winningShape {
                return s
            }
        }
    }
    log.Panicln("Couldn't find a shape by strategy: ", otherShape, strategy)
    return -1
}

func willWin(otherShape Shape) Shape {
    for k, v := range wins {
        if v == otherShape {
            return k
        }
    }
    log.Panicln("Invalid input ", otherShape)
    return -1
}
