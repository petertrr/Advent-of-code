#!/usr/bin/env kscript

import java.io.File
import kotlin.math.ceil

data class Seat(val row: Int, val col: Int) {
    val id = row * 8 + col

    companion object {
        fun fromBinary(binary: String): Seat {
            require(binary.length == 10)
            val row = binary.take(7).fold(0..127) { acc, c ->
                when (c) {
                    'F' -> acc.start.rangeTo((acc.start + acc.endInclusive) / 2)
                    'B' -> ceil((acc.start + acc.endInclusive).toFloat() / 2).toInt().rangeTo(acc.endInclusive)
                    else -> error("Incorrect selector $c")
                }
            }
                    .also { require(it.start == it.endInclusive) { "Range $it hasn't converged" } }
                    .start

            val col = binary.takeLast(3).fold(0..7) { acc, c ->
                when (c) {
                    'L' -> acc.start.rangeTo((acc.start + acc.endInclusive) / 2)
                    'R' -> ceil((acc.start + acc.endInclusive).toFloat() / 2).toInt().rangeTo(acc.endInclusive)
                    else -> error("Incorrect selector $c")
                }
            }
                    .also { require(it.start == it.endInclusive) { "Range $it hasn't converged" } }
                    .start

            return Seat(row, col)
        }
    }
}

File("05.input")
        .readLines()
        .map { Seat.fromBinary(it) }
        .sortedBy { it.id }
        .apply {
            println("Maximum seat id is ${last().id}")
        }
        .windowed(3)
        .find {
            it.first().id + 1 != it[1].id || it[1].id + 1 != it.last().id
        }
