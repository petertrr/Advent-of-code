#!/usr/bin/env kscript

import java.io.File

sealed class Command(open val line: Int) {
    data class Acc(val value: Int, override val line: Int) : Command(line)
    data class Jmp(val value: Int, override val line: Int) : Command(line)
    data class Nop(val value: Int, override val line: Int) : Command(line)
}

class State(val program: List<Command>) {
    var acc = 0
        private set
    var pointer = 0
        private set
    var isTerminated = false
        private set

    fun execute(): Command {
        return if (pointer == program.size) {
            isTerminated = true
            return Command.Nop(0, pointer)
        } else if (pointer > program.size) {
            error("Attempt to execture command on line $pointer, while program.size=${program.size}")
        } else {
            program[pointer].also {
                apply(it)
            }
        }
    }

    private fun apply(command: Command) {
        when (command) {
            is Command.Acc -> {
                acc += command.value
                pointer += 1
            }
            is Command.Jmp -> pointer += command.value
            is Command.Nop -> pointer += 1
        }
    }
}

val program = File("08.input")
        .readLines()
        .mapIndexed { index, line ->
            line.split(' ', limit = 2).let {
                when (it.first()) {
                    "acc" -> Command.Acc(it[1].toInt(), index)
                    "jmp" -> Command.Jmp(it[1].toInt(), index)
                    "nop" -> Command.Nop(it[1].toInt(), index)
                    else -> error("Unknown command line: <$line>")
                }
            }
        }

fun State.runUntilLoop() {
    val executedCommands = mutableSetOf<Command>()
    while (true) {
        val command = execute()
        if (isTerminated) {
            break
        }
        if (command !in executedCommands) {
            executedCommands.add(command)
        } else {
            break
        }
    }
}

// part 1
run {
    val state = State(program)
    state.runUntilLoop()
    println("Acc before loop start: ${state.acc}")
}

// part 2
run {
    program.mapIndexed { index, command ->
        when (command) {
            is Command.Jmp, is Command.Nop -> index
            else -> null
        }
    }
            .filterNotNull()
            .first { idx ->
                val substitution = program[idx].let {
                    when (it) {
                        is Command.Jmp -> Command.Nop(it.value, it.line)
                        is Command.Nop -> Command.Jmp(it.value, it.line)
                        else -> error("Command $it shouldn't be checked here")
                    }
                }
                val state = State(program
                        .toMutableList()
                        .apply {
                            removeAt(idx)
                            add(idx, substitution)
                        })
                state.runUntilLoop()
                state.isTerminated.also {
                    if (it) {
                        println("When command ${program[idx]} @$idx is substituted with $substitution, program is terminated with state.acc=${state.acc}")
                    }
                }
            }
}
