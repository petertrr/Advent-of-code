#!/usr/bin/env kscript

import java.io.File

data class Adapter(val output: Int) {
    fun isValidInput(input: Int) = output > input && output - input <= 3

    fun available(adapters: Iterable<Adapter>) = adapters
            .filter { it.isValidInput(this.output) }
}

data class ChainNode(val value: Adapter, val parent: ChainNode?) {
    fun parents(includeSelf: Boolean = false) = sequence {
        var current: ChainNode? = if (includeSelf) this@ChainNode else this@ChainNode.parent
        while (current != null) {
            yield(current)
            current = current.parent
        }
    }

    fun buildChildren(adapters: Iterable<Adapter>) = value.available(adapters)
            .asSequence()
            .filterNot {
                it in parents(includeSelf = true).map { it.value }
            }
            .map { ChainNode(it, this) }
}

fun buildTreeFromSorted(root: ChainNode,
                        sortedRemainingAdapters: Collection<Adapter>,
                        useAllAdapters: Boolean,
                        allAdapters: Collection<Adapter>,
                        lastAdaper: Adapter
): Sequence<ChainNode> = sortedRemainingAdapters
        .asSequence()
        .filter { it.isValidInput(root.value.output) }
        .map { ChainNode(it, root) }
        .flatMap { node ->
            // because chain has root, that is not included in adapters
            val canConnectLastAdapter = !useAllAdapters || sortedRemainingAdapters.size == 1
//                    it.parents().count() == allAdapters.size
            if (canConnectLastAdapter && lastAdaper.isValidInput(node.value.output)) {
                sequenceOf(node, ChainNode(lastAdaper, node))
            } else if (sortedRemainingAdapters.size > 1) {
                buildTreeFromSorted(
                        node, sortedRemainingAdapters.filterNot { it == node.value },
                        useAllAdapters, allAdapters, lastAdaper
                )
            } else {
                emptySequence()
            }
        }

val adapters = File("10.input")
        .readLines()
        .map {
            Adapter(it.toInt())
        }
val adaptersSorted = adapters
        .sortedBy { it.output }
val myAdapter = adapters
        .maxByOrNull { it.output }!!
        .let { it.output + 3 }
        .let(::Adapter)
val initialOutput = 0
val initialAdapter = Adapter(initialOutput)

// part 1
run {
    buildTreeFromSorted(ChainNode(initialAdapter, null),
            adaptersSorted,
            useAllAdapters = true,
            allAdapters = adapters,
            lastAdaper = myAdapter)
            .filter {
                it.parents().count() == adapters.size + 1
            }
            .map { leaf ->
                leaf.parents(includeSelf = true)
                        .zipWithNext()
                        .map {
                            it.second.value.output - it.first.value.output
                        }
                        .groupingBy { it }
                        .eachCount()
                        .also {
                            println("Length of chain is ${it.values.sum()}")
                        }
            }
            .forEach {
                println(it)
                return@run
            }

//    val startTime = System.nanoTime().also {
//        println("Starting part 2...")
//    }
//    buildTreeFromSorted(ChainNode(initialAdapter, null),
//            adaptersSorted,
//            useAllAdapters = false,
//            allAdapters = adapters,
//            lastAdaper = myAdapter)
//            .filter {
//                it.value == myAdapter
//            }
//            .count()
//            .also {
//                println("Total number of chains: $it")
//            }
//    println("Finished part 2 in ${(System.nanoTime() - startTime) / 1e9} sec")

}

// part 2
class RoutesCounter(val adapters: List<Adapter>) {
    private val adaptersToCounts = mutableMapOf<Adapter, Long>()

    init {
        require(adapters.first().output == 0) { "Incorrect adapter on position 0" }
        adaptersToCounts.put(this.adapters.first(), 1)
        this.adapters.forEach { adapter ->
            countRoutes(adapter).also {
                println("Value for $adapter is $it")
            }
        }
    }

    fun countRoutes(adapter: Adapter): Long {
        return adaptersToCounts.compute(adapter) { _, value ->
            value ?: adapter.possibleInputs()
                    .map { countRoutes(it) }
                    .sum()
        }!!
    }

    private fun Adapter.possibleInputs() = adapters
            .filterNot { it == this || it == adapters.last() }
            .filter {
                isValidInput(it.output)
            }
}

println("Starting part 2...")
RoutesCounter(adaptersSorted.toMutableList().apply {
        add(0, initialAdapter)
        add(myAdapter)
    }
        .toList()
)
        .countRoutes(myAdapter)
        .also {
            println("Number of routes: $it")
        }