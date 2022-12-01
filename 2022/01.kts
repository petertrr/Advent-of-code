#!/usr/bin/env kscript

import java.io.File

data class Item(
    val calories: Int,
)

data class Inventory(
    val items: MutableList<Item>,
)

run {
    val inventory = Inventory(mutableListOf())
    var item: Item? = null
    File("01.input").readLines().forEach { line ->
        if (line.isBlank()) {
            item?.let { inventory.items.add(item!!) }
            item = Item(0)
        } else {
            item = item?.copy(calories = item!!.calories + line.toInt()) ?: Item(0)
        }
    }
    println("Maximum calories: ${inventory.items.maxByOrNull { it.calories }}")
    println("Maximum calories by top three: ${inventory.items.sortedByDescending { it.calories }.take(3).sumBy { it.calories }}")
}
