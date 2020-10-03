#!/usr/bin/env kscript

@file:Include("Intcode.kt")

import java.io.File

val intcode = Intcode.parseInput(
    File("05.input")
        .readLines()
        .first()
)
        
intcode.inputs.add(1)
intcode.runProgram()
println("After running program outputs are: ${intcode.outputs}")
