#!/usr/bin/env kscript

import java.io.File

/**
 * @property color color of the bag, e.g. green
 * @property spec an adjective describing the bag, e.g, shiny
 */
data class Bag(val color: String, val spec: String) {
    companion object {
        fun fromString(bagString: String) = bagString.split(' ')
                .map { it.trim() }
                .let { Bag(it[1], it[0]) }
    }
}

sealed class Constraint {
    data class BagConstraint(val number: Int, val bag: Bag) : Constraint()
    object EmptyConstraint : Constraint()

    companion object {
        val constraintRegex = Regex("(no other bags|(\\d+) ((?:\\w+[ ]?){2}) bag[s]*)[.,]?")

        fun fromString(constraintString: String): Constraint {
            val matchResult = constraintRegex.matchEntire(constraintString.trim())
            requireNotNull(matchResult)
            return if (matchResult.groupValues[1] == "no other bags") {
                EmptyConstraint
            } else {
                matchResult.groupValues
                        .let {
                            BagConstraint(
                                    it[2].toInt(),
                                    Bag.fromString(it.last())
                            )
                        }
            }
        }
    }
}

/**
 * @property constraints Map of required quantity of bags to bag types
 */
data class Rule(val bag: Bag, val constraints: List<Constraint>)

data class Node(val bag: Bag, val parent: Node?) {
    fun parents(): Sequence<Node> {
        var lastParentEncountered = false
        return generateSequence(parent) {
            it.parent
        }
                .takeWhile {
                    var tmp = !lastParentEncountered
                    if (it.parent == null) {
                        lastParentEncountered = true
                    }
                    tmp
                }
    }
}

val myBag = Bag("gold", "shiny")
run {
    val rules = File("07.input")
            .readLines()
            .map { rule ->
                rule.split("bags contain")
                        .also { require(it.size == 2) }
                        .let { it[0] to it[1] }
                        .let { (bagString, constraintsString) ->
                            Rule(
                                    Bag.fromString(bagString),
                                    constraintsString.split(',')
                                            .map(Constraint.Companion::fromString)
                            )
                        }
            }
    val colors = rules.flatMap { rule ->
        listOf(rule.bag.color) + rule.constraints
                .filterIsInstance<Constraint.BagConstraint>()
                .map { it.bag.color }
    }
            .distinct()
    val specs = rules.flatMap { rule ->
        listOf(rule.bag.spec) + rule.constraints
                .filterIsInstance<Constraint.BagConstraint>()
                .map { it.bag.spec }
    }
            .distinct()
    println("Available colors: $colors")
    println("Available specs: $specs")
    println("All rules are different: ${rules.map { it.bag }.let { it.size == it.distinct().size }}")

    fun checkNode(node: Node): List<Node> {
        return rules.find {
            it.bag == node.bag
        }!!
                .constraints
                .filterIsInstance<Constraint.BagConstraint>()
                .map { Node(it.bag, node) }
                .filterNot { node ->
                    // stop recursion for bags that appear second time
                    node.bag in node.parents().map { it.bag }
                }
                .flatMap {
                    if (it.bag == myBag) {
                        listOf(it)
                    } else {
                        checkNode(it)
                    }
                }
    }

    // part 1
    rules.flatMap {
        checkNode(Node(it.bag, null))
    }
            .map { it.parents().last() }
            .distinct()
            .count()
            .also { println(it) }

    fun countBags(node: Node): Int {
        return rules.find {
            it.bag == node.bag
        }!!
                .constraints
                .sumBy { constraint ->
                    when (constraint) {
                        is Constraint.EmptyConstraint -> 0
                        is Constraint.BagConstraint -> constraint.number + constraint.number * countBags(Node(constraint.bag, node))
                    }
                }
    }

    //part 2
    myBag.let {
        Node(it, null)
    }
            .let(::countBags)
            .also { println(it) }
}
