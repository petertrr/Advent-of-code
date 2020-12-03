import java.io.File

data class Slope(val right: Int, val down: Int)

class Area(data: List<String>) {
    /**
     * A 2D array representing the slope area. Value is [true] if there is a tree and [false] if area is clear.
     */
    val map = data.mapIndexed { row, line ->
        line.mapIndexed { col, c ->
            when (c) {
                '.' -> false
                '#' -> true
                else -> error("Illegal symbol in input data @ $row:$col: $c")
            }
        }
    }
    private val xMax = map.first().size
    val yMax = map.size

    /**
     * @return value at [x] across (horizontal) and [y] along (vertical) the slope
     */
    fun get(x: Int, y: Int) = map[y][x % xMax]
}

fun treesOnSlope(slope: Slope): Int {
    val area = File("03.input")
            .readLines()
            .let { Area(it) }
    return generateSequence(Pair(0, 0)) {
        it.first + slope.right to it.second + slope.down
    }
            .takeWhile { (_, y) ->
                y < area.yMax
            }
            .count { (x, y) ->
                area.get(x, y)
            }
            .also {
                println("Number of trees encountered: $it")
            }
}

// part 1
treesOnSlope(Slope(3, 1))

// part 2
listOf(
        Slope(1, 1),
        Slope(3, 1),
        Slope(5, 1),
        Slope(7, 1),
        Slope(1, 2)
)
        .map {
            treesOnSlope(it)
        }
        .reduce { acc, i -> acc * i }
        .also {
            println("Product of all counts of trees: $it")
        }