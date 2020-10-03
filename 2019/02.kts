#!/usr/bin/env kscript

@file:Include("Intcode.kt")

import java.io.File

fun loadData() = Intcode.parseInput(
    File("02.input").readLines().first()
)

// part 1
run {
    val intcode = loadData()
    intcode.run {
        setMemoryAt(1, 12)
        setMemoryAt(2, 2)
    }
    intcode.runProgram()
    println("Answer to the first part: ${intcode.output()}")
}

// part 2
val desiredOutput = 19690720
val (noun, verb) = run {
    for (noun in 0..100) {
        for (verb in 0..100) {
            val intcode = loadData()
            intcode.run {
                setMemoryAt(1, noun)
                setMemoryAt(2, verb)
            }
            intcode.runProgram()
            if (intcode.output() == desiredOutput) return@run noun to verb
        }
    }
    error("Expected output $desiredOutput has not been achieved for any combination")
}
println("Answer to the second part: ${100 * noun + verb}")
