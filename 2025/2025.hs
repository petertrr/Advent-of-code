import System.Environment
import Aoc01
import Aoc02

main = getArgs >>= parse

parse args = case args of
 "01":as -> aoc2025_01 as
 "02":as -> aoc2025_02 as
