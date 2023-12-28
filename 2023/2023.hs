import System.Environment
import Aoc07
import Aoc08
import Aoc09
import Aoc11
import Aoc15

main = getArgs >>= parse

parse args = case args of
 "07":as -> aoc2023_07 as
 "08":as -> aoc2023_08 as
 "09":as -> aoc2023_09 as
 "11":as -> aoc2023_11 as
 "15":as -> aoc2023_15 as
