#!/usr/bin/env kscript

@file:Include("Intcode.kt")

import java.io.File

// examples
fun handleExample(example: String, input: Int, check: (outputs: List<Int>) -> Unit) {
    val intcode = Intcode.parseInput(example)
    intcode.inputs.add(input)
    intcode.runProgram()
    check(intcode.outputs)
}

"3,9,8,9,10,9,4,9,99,-1,8".run {
    handleExample(this, 8) { require(it.single() == 1) }
    handleExample(this, 6) { require(it.single() == 0) }
    handleExample(this, 9) { require(it.single() == 0) }
    handleExample(this, 0) { require(it.single() == 0) }
    handleExample(this, -1) { require(it.single() == 0) }
}

handleExample("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 1) {
    require(it.single() == 1)
}
handleExample("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 0) {
    require(it.single() == 0)
}

"101,-1,7,7,4,7,1105,11,0,99".run {
    handleExample(this, 1) { require(it == (10 downTo 0).toList()) }
}

val complexExample = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
handleExample(complexExample, 7) { require(it.single() == 999) }
handleExample(complexExample, 8) { require(it.single() == 1000) }
handleExample(complexExample, 9) { require(it.single() == 1001) }

fun loadData() = Intcode.parseInput(
    File("05.input")
        .readLines()
        .first()
)

// part 1
/*run {
    val intcode = loadData()
    intcode.inputs.add(1)
    intcode.runProgram()
    println("After running program outputs are: ${intcode.outputs}")
}*/

// part 2
/*run {
    val intcode = loadData()
    intcode.inputs.add(5)
    intcode.runProgram()
    println("After running program outputs are: ${intcode.outputs}")
}*/
