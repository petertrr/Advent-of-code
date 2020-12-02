#!/usr/bin/env kscript

import java.io.File

// part 1
run {
    val numbers = File("01.input").readLines()
            .map { it.toInt() }

    numbers.elementPairs()
            .firstOrNull {
                it.first + it.second == 2020
            }
            ?.let { (i, j) ->
                println("numbers $i and $j sum up to 2020, their product is ${i * j}")
            }
}

// part 2
run {
    val numbers = File("01.input").readLines()
            .map { it.toInt() }

    numbers.elementTriples()
            .firstOrNull { (i, j, k) ->
                i + j + k == 2020
            }
            ?.let { (i, j, k) ->
                println("numbers $i, $j and $k sum up to 2020, their product is ${i * j * k}")
            }
}

fun <T> List<T>.elementPairs() = sequence {
    for (i in 0 until size - 1) {
        for (j in i + 1 until size - 1) {
            yield(get(i) to get(j))
        }
    }
}

fun <T> List<T>.elementTriples() = sequence {
    for (i in 0 until size - 1) {
        for (j in i + 1 until size - 1) {
            for (k in j + 1 until size - 1) {
                yield(Triple(get(i), get(j), get(k)))
            }
        }
    }
}
