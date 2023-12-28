module Aoc15 where

import System.IO
import Data.List.Split
import Data.Char

hash :: String -> Int
hash = foldl step 0
  where step acc c = (acc + ord c) * 17 `rem` 256

aoc2023_15 (a:_) = do
  line <- readFile a
  let instructions = splitOn "," $ head . lines $ line
  print . sum $ map hash instructions
