package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"unicode"
)

func main() {
	f, err := os.Open("03.input")
	if err != nil {
		log.Fatalln("Error opening file", err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	totalPriority := 0
	for scanner.Scan() {
		line := scanner.Text()
		compartment1 := line[:len(line)/2]
		compartment2 := line[len(line)/2:]
		counts1 := countRunes(compartment1)
		counts2 := countRunes(compartment2)
		commonItems := intersect(counts1, counts2)
		fmt.Println(counts1, counts2, commonItems)
		for k, _ := range commonItems {
			totalPriority += int(priority(k))
		}
	}
	fmt.Println("Total priority: ", totalPriority)

	f.Seek(0, io.SeekStart)
	scanner = bufio.NewScanner(f)
	totalPriority = 0
	for scanner.Scan() {
		window := []string{scanner.Text()}
		scanner.Scan()
		window = append(window, scanner.Text())
		scanner.Scan()
		window = append(window, scanner.Text())

		counts := Map(window, func(s string) map[rune]int {
			return countRunes(s)
		})
		commonItems := intersect(counts[0], intersect(counts[1], counts[2]))
		if len(commonItems) != 1 {
			log.Panicln("More than a single common item type: ", commonItems)
		}
		for k, _ := range commonItems {
			totalPriority += int(priority(k))
		}
	}
	fmt.Println("Total priority: ", totalPriority)
}

func intersect(first map[rune]int, second map[rune]int) map[rune]int {
	commonItems := map[rune]int{}
	for k, v := range first {
		if v2, contains := second[k]; contains {
			if v < v2 {
				commonItems[k] = v
			} else {
				commonItems[k] = v2
			}
		}
	}
	return commonItems
}

func priority(char rune) byte {
	var result byte
	if unicode.IsLower(char) {
		result = byte(char) + 1 - byte('a')
	} else {
		result = byte(char) + 27 - byte('A')
	}
	return result
}

func countRunes(input string) map[rune]int {
	result := map[rune]int{}
	for _, char := range input {
		result[char] += 1
	}
	return result
}

func Map[T any, R any](list []T, transform func(T) R) []R {
	result := make([]R, len(list))
	for i, v := range list {
		result[i] = transform(v)
	}
	return result
}
