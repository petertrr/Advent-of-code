import System.Environment
import Aoc01

main = getArgs >>= parse

parse args = case args of
 "01":as -> aoc2025_01 as
