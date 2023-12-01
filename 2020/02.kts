#!/usr/bin/env kscript

import java.io.File

sealed class Policy {
    abstract val regex: Regex
    abstract fun isValid(password: String): Boolean

    data class OldPolicy(val letter: Char, val times: IntRange) : Policy() {
        override val regex = Regex("^(\\d+)-(\\d+)\\s")

        override fun isValid(password: String) = password.count { it == letter } in times
    }

    data class NewPolicy(val letter: Char, val idx1: Int, val idx2: Int) : Policy() {
        override val regex = Regex("^(\\d+)-(\\d+)\\s")

        override fun isValid(password: String) = (password[idx1 - 1] == letter) xor (password[idx2 - 1] == letter)
    }
}

fun <T: Policy> T.createPolicy(policyString: String): T {
    return regex.find(policyString)
            ?.let {
                when (this) {
                    is Policy.OldPolicy ->
                        Policy.OldPolicy(
                                policyString.last(),
                                it.groupValues.drop(1).map { it.toInt() }.let { it.first()..it[1] }
                        )
                    is Policy.NewPolicy ->
                        Policy.NewPolicy(
                                policyString.last(),
                                it.groupValues[1].toInt(),
                                it.groupValues[2].toInt(),
                        )
                }
            }
            ?: error("Policy string $policyString doesn't match required policy pattern ${regex.pattern}")
}

fun <T: Policy> solve() {
    File("02.input")
            .readLines()
            .map { line ->
                line.split(':', limit = 2)
                        .map { it.trim() }
                        .let { (policyString, password) ->
                            Policy.OldPolicy.fromString(policyString) to password
                        }
            }
            .count { (policy, password) ->
                password.count { it == policy.letter } in policy.times
            }
            .also {
                println("Passwords that comply with policy count: $it")
            }
}

// part 1
run {
    File("02.input").readLines()
            .map { line ->
                line.split(':', limit = 2)
                        .map { it.trim() }
                        .let { (policyString, password) ->
                            Policy.OldPolicy.fromString(policyString) to password
                        }
            }
            .count { (policy, password) ->
                password.count { it == policy.letter } in policy.times
            }
            .also {
                println("Passwords that comply with policy count: $it")
            }
}

// part 2
run {
    File("02.input").readLines()
            .map { line ->
                line.split(':', limit = 2)
                        .map { it.trim() }
                        .let { (policyString, password) ->
                            Policy.NewPolicy.fromString(policyString) to password
                        }
            }
            .count { (policy, password) ->
                (password[policy.idx1 - 1] == policy.letter) xor
                        (password[policy.idx2 - 1] == policy.letter)
            }
            .also {
                println("Passwords that comply with the new policy count: $it")
            }
}
