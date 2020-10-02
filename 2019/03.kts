import java.io.File
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min

enum class Direction {
    LEFT, RIGHT, UP, DOWN;
    
    companion object {
        fun from(c: Char): Direction {
            return when (c) {
                'L', 'l' -> LEFT
                'R', 'r' -> RIGHT
                'U', 'u' -> UP
                'D', 'd' -> DOWN
                else -> error("Illegal literal for Direction constructor")
            }
        }
    }
}

data class Point<T>(val x: T, val y: T)
data class Segment<T>(val p1: Point<T>, val p2: Point<T>)

data class Command(val direction: Direction, val steps: Int) {
    fun apply(start: Point<Int>): Point<Int> {
        val (dx, dy) = when (direction) {
            Direction.LEFT -> Point(-steps, 0)
            Direction.RIGHT -> Point(steps, 0)
            Direction.UP -> Point(0, steps)
            Direction.DOWN -> Point(0, -steps)
        }
        return Point(start.x + dx, start.y + dy)
    }
}

fun parseInput(input: List<String>): List<List<Segment<Int>>> = input
    .also { require(it.size == 2) { "There should be only two sets of commands in input" } }
    .map {
        it.trim().split(',')
    }
    .also { println("First path has ${it[0].size} points, second path has ${it[1].size} points") }
    .map { data ->
        data.map {
            Command(Direction.from(it[0]), it.substring(1).toInt())
        }
        .scan(Point(0, 0)) { acc, command ->
            command.apply(acc)
        }
        .zipWithNext()
        .map {
            Segment<Int>(it.first, it.second)
        }
    }

val (data1, data2) = parseInput(
    File("03.input")
        .readLines()
    )
//    listOf("R8,U5,L5,D3",
//           "U7,R6,D4,L4")
    
fun Segment<Int>.intersectionManhattan(another: Segment<Int>): Point<Int>? {
    return if (p1.x == p2.x && another.p1.x == another.p2.x) {
        // both segments are vertical
        null
    } else if (p1.y == p2.y && another.p1.y == another.p2.y) {
        // both segments are horizontal
        null
    } else if (p1.x == p2.x) {
        // this segment is vertical
        require(another.p1.y == another.p2.y) { "Second segment should be horizontal in this case, but is $another" }
        if (min(another.p1.x, another.p2.x) <= p1.x && p1.x <= max(another.p1.x, another.p2.x) &&
            min(p1.y, p2.y) <= another.p1.y && another.p1.y <= max(p1.y, p2.y)) {
            Point(p1.x, another.p1.y)
        } else {
            null
        }
    } else {
        // another segment is vertical
        require(another.p1.x == another.p2.x) { "Second segment should be vertical in this case, but is $another" }
        if (min(p1.x, p2.x) <= another.p1.x && another.p1.x <= max(p1.x, p2.x) &&
            min(another.p1.y, another.p2.y) <= p1.y && p1.y <= max(another.p1.y, another.p2.y)) {
            Point(another.p1.x, p1.y)
        } else {
            null
        }
    }
}

// Part 1
data2
    .flatMap { segment2 ->
        data1
            .mapNotNull { segment1 ->
                segment2.intersectionManhattan(segment1)
            }
    }
    .minByOrNull { p -> abs(p.x) + abs(p.y) }!!
    .apply {
        println("Answer for the first part is: ${abs(x) + abs(y)}")
    }
    
fun Segment<Int>.length() = abs(p2.x - p1.x) + abs(p2.y - p1.y)

// Part 2
data2
    .zip(data2
        .scan(0) { acc, segment2 ->
            acc + segment2.length()
        }
    )
    .drop(1)  // because first point is always (0, 0)
    .map { (segment2, steps2) ->
        data1.zip(data1
                .scan(0) { acc, segment1 ->
                    acc + segment1.length()
                }
            )
            .drop(1)  // because first point is always (0, 0)
            .map { (segment1, steps1) ->
                segment2
                    .intersectionManhattan(segment1)
                    ?.let { p ->
                        steps1 + steps2 + Segment(segment1.p1, p).length() + Segment(segment2.p1, p).length()
                    }
            }
            .filterNotNull()
    }
    .filter { it.isNotEmpty() }
    .flatten()
    .get(1)
    .also {
        println("Answer for the second part is: $it")
    }
