fun Int.digits(): List<Int> {
    return sequence<Int> {
        var n = this@digits
        do {
            yield(n % 10)
            n /= 10
            if (n == 0) break
        } while (n / 10 >= 0)
    }
    .toList()
    .reversed()
}

// Part 1
(264793..803936)
    .asSequence()
    .filter {
        it
            .digits()
            .zipWithNext()
            .let { pairs ->
                pairs.any { it.first == it.second } &&
                    pairs.all { it.first <= it.second }
            }
    }
    .count()
    .also {
        println("The answer to the 1st part is $it")
    }
    
// Part 2
(264793..803936)
    .asSequence()
    .filter {
        it
            .digits()
            .also { require(it.size == 6) { "This is a task requirement" } }
            .let {
                it
                    .zipWithNext()
                    .all { it.first <= it.second } &&
                (it.first() == it[1] && it[1] != it[2] ||
                    it
                        .windowed(4)
                        .any {
                            it[0] != it[1] && it[1] == it[2] && it[2] != it[3]
                        } ||
                    it[it.size - 3] != it[it.size - 2] && it[it.size - 2] == it.last()
                )
            }
    }
    .count()
    .also {
        println("The answer to the 2nd part is $it")
    }