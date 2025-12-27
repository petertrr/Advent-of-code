module Aoc03 where

import System.IO
import Data.Char
import Data.Ord
import Data.List
import Data.List.Split (chunksOf)
import qualified Data.Text as T
import Debug.Trace

maximumWithIndex :: Ord a => [a] -> (a, Int)
-- reverse is needed, because maximumBy uses foldr
maximumWithIndex list = maximumBy (comparing fst) $ reverse (zip list [0..])

getJoltage :: [Int] -> Int
getJoltage nums = n1 * 10 + n2
    where (n1, idx1) = maximumWithIndex $ init nums
          n2 = maximum $ drop (idx1 + 1) nums

aoc2025_03 args = do
  content <- readFile $ head args
  let linesOfFile = lines content
  print . show . getResult $ linesOfFile
    where getResult linesOfFile = sum $ map (getJoltage . inputNumbers) linesOfFile
          inputNumbers = map digitToInt
