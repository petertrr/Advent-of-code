#!/usr/bin/env kscript

import java.io.File

File("06.input")
        .readText()
        .split("\n\n")
        .map { it.lines() }
        .map { lines ->
            lines.size to
                    lines
                            .map { it.toList() }
                            .flatten()
                            .groupingBy { it }
                            .eachCount()
        }
        .apply {
            map { (_, charsToCount) ->
                charsToCount.size
            }
                    .sum()
                    .also {
                        println("Number of questions *anyone* answered yes to: $it")
                    }
        }
        .run {
            map { (numPeopleInGroup, charsToCount) ->
                charsToCount.count {
                    it.value == numPeopleInGroup
                }
            }
                    .sum()
                    .also {
                        println("Number of questions *everyone* answered yes to: $it")
                    }
        }