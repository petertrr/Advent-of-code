#!/usr/bin/env kscript

import java.io.File

data class Range(
    val from: Int,
    val to: Int,
) {
    fun containsFully(other: Range): Boolean {
        return from <= other.from && to >= other.to
    }

    fun overlaps(other: Range): Boolean {
        return from <=other.from && to >= other.from 
    }
}

val assignmentPairs: List<Pair<Range, Range>> = File("04.input").useLines { lines ->
    lines.filter { it.isNotBlank() }.map { line ->
        line.split(",").map {
            it.split("-").map { it.toInt() }.let { Range(it.first(), it.last()) }
        }.let { it.first() to it.last() }
    }.toList()
}

val result1 = assignmentPairs.filter { (a1, a2) ->
    a1.containsFully(a2) || a2.containsFully(a1)
}.count()
println("Part 1: $result1")

val result2 = assignmentPairs.filter { (a1, a2) ->
    a1.overlaps(a2) || a2.overlaps(a1)
}.count()
println("Part 2: $result2")

