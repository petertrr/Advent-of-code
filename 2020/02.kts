#!/usr/bin/env kscript

import java.io.File

data class OldPolicy(val letter: Char, val times: IntRange) {
    companion object {
        val regex = Regex("^(\\d+)-(\\d+)\\s")

        fun fromString(policyString: String) =
                regex.find(policyString)
                        ?.let {
                            OldPolicy(
                                policyString.last(),
                                it.groupValues.drop(1).map { it.toInt() }.let { it.first()..it[1] }
                            )
                        }
                        ?: error("Policy string $policyString doesn't match required policy pattern")
    }
}

data class NewPolicy(val letter: Char, val idx1: Int, val idx2: Int) {
    companion object {
        val regex = Regex("^(\\d+)-(\\d+)\\s")

        fun fromString(policyString: String) =
                regex.find(policyString)
                        ?.let {
                            NewPolicy(
                                    policyString.last(),
                                    it.groupValues[1].toInt(),
                                    it.groupValues[2].toInt(),
                            )
                        }
                        ?: error("Policy string $policyString doesn't match required policy pattern")
    }
}

// part 1
run {
    File("02.input").readLines()
            .map { line ->
                line.split(':', limit = 2)
                        .map { it.trim() }
                        .let { (policyString, password) ->
                             OldPolicy.fromString(policyString) to password
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
                            NewPolicy.fromString(policyString) to password
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
