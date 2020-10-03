package com.github.petertrr

class Intcode(private val register: MutableList<Int>) {
    fun runProgram() {
        var position = 0
        while (true) {
            val opcode = register[position].let(Opcode::from)
            val operation = when (opcode) {
                Opcode.HALT -> break
                Opcode.ADD -> Operation.Add()
                Opcode.MULT -> Operation.Mult()
            }
            position = operation.execute(position, register)
        }
    }
    
    fun setMemoryAt(index: Int, value: Int) {
        register[index] = value
    }
    
    fun memoryAt(index: Int) = register[index]
    
    fun output() = memoryAt(0)
    
    companion object {
        fun parseInput(input: String): Intcode {
            return Intcode(
                input.split(',').map { it.toInt() }.toMutableList()
            )
        }
    }
}

sealed class Operation(private val opcode: Opcode) {
    abstract fun execute(position: Int, register: MutableList<Int>): Int
    
    class Halt : Operation(Opcode.HALT) {
        override fun execute(position: Int, register: MutableList<Int>) = position + 1
    }
    
    class Add: Operation(Opcode.ADD) {
        override fun execute(position: Int, register: MutableList<Int>): Int {
            register[register[position + 3]] = register[register[position + 1]] + register[register[position + 2]]
            return position + 4
        }
    }
    
    class Mult: Operation(Opcode.MULT) {
        override fun execute(position: Int, register: MutableList<Int>): Int {
            register[register[position + 3]] = register[register[position + 1]] * register[register[position + 2]]
            return position + 4
        }
    }
}

enum class Opcode(private val code: Int) {
    ADD(1),
    MULT(2),
    HALT(99)
    ;
    
    companion object {
        fun from(code: Int): Opcode {
            return when (code) {
                1 -> ADD
                2 -> MULT
                99 -> HALT
                else -> error("Unknown opcode $code")
            }
        }
    }
}
