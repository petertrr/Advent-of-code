#!/usr/bin/env kscript

import java.io.File
import java.time.LocalDateTime
import java.util.*

val WINDOW_SIZE = 25

/**
 * An attempt on generic algorithm to generate combinations.
 * FixMe: Performance is really bad on large lists with large [r].
 * @param r length of combinations
 * @return a sequence of lists of size [r]
 */
fun <T> List<T>.combinations(r: Int): Sequence<LinkedList<T>> {
    return if (r == 1) {
        asSequence().map {
            LinkedList<T>().apply { add(it) }
        }
    } else {
        sequence {
            for (i in 0 until size - 1) {
                val elementAtI = this@combinations.get(i)
                drop(i + 1)
                        .combinations(r - 1)
                        .onEach {
                            it.add(elementAtI)
                        }
                        .forEach {
                            yield(it)
                        }
            }
        }
    }
}

val numbers = File("09.input")
        .readLines()
        .map { it.toLong() }

val invalidNumber = numbers
        .windowed(WINDOW_SIZE + 1)
        .find { window ->
            window.dropLast(1).combinations(2)
                    .none {
                        it.first() + it[1] == window.last()
                    }
        }!!
        .last()
        .also {
            println("Answer to part 1 is $it")
        }

val group = (2 until numbers.size).asSequence().map { k ->
    numbers.windowed(k).find {
        it.sum() == invalidNumber
    }
}
        .filterNotNull()
        .first()
println("Group in part 2 is $group, smallest + largest = ${group.minOrNull()!! + group.maxOrNull()!!}")
