#!/usr/bin/env kscript

import java.io.File

enum class EyeColor(val color: String) {
    AMB("amb"),
    BLU("blu"),
    BRN("brn"),
    GRY("gry"),
    GRN("grn"),
    HZL("hzl"),
    OTH("oth"),
    ;
}

class Passport(map: Map<String, String>) {
    val byr: Int = map.getYear("byr", 1920..2002)
    val iyr: Int = map.getYear("iyr", 2010..2020)
    val eyr: Int = map.getYear("eyr", 2020..2030)
    val hgt: Int = map["hgt"]!!.run {
        when {
            endsWith("cm") -> substringBeforeLast("cm").toInt().also {
                require(it in 150..193) { "Height $this is in invalid range" }
            }
            endsWith("in") -> substringBeforeLast("in").toInt().also {
                require(it in 59..75) { "Height $this is in invalid range" }
            }
            else -> error("Incorrect measure unit in $this")
        }
    }
    val hcl: String = map["hcl"]!!.also {
        require(it.matches(hclRegex)) { "hcl $it doesn't match required pattern $hclRegex" }
    }
    val ecl: String = map["ecl"]!!.also {
        require(it in EyeColor.values().map { it.color }) { "Eye color $it is invalid" }
    }
    val pid: String = map["pid"]!!.also {
        require(it.length == 9) { "PID has to be a 9-digit value" }
    }
    val cid: String? = map["cid"]

    private fun Map<String, String>.getYear(key: String, validRange: IntRange) = getValue(key).toInt().also {
        require(it in validRange) { "Year $it for key $key is invalid: doesn't belong to range $validRange" }
    }

    companion object {
        private val hclRegex = Regex("#[0-9a-f]{6}")
        val requiredKeys = listOf("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
        val optionalKeys = listOf("cid")
    }
}

File("04.input")
        .readText()
        // entries are separated by empty lines
        .split("\n\n")
        .mapNotNull { entry ->
            entry.split(' ', '\n')
                    .map { it.split(':', limit = 2) }
                    .filter { it.size == 2 }
                    .associate { it.first() to it[1] }
        }
        .filter { map ->
            Passport.requiredKeys.all { it in map.keys }
        }
        .also {
            println("Number of passports with correct fields: ${it.size}")
        }
        .map {
            runCatching {
                Passport(it)
            }
        }
        .partition { it.isSuccess }
        .let { (valid, invalid) ->
            println("Number of fully valid passports: ${valid.size}")
            invalid.forEach {
                println("Passport is invalid because: ${it.exceptionOrNull()?.message}")
            }
        }
