module Aoc09 where

import System.IO

nextRow is = zipWith (-) (tail is) is

generateRows is = takeWhile (not . all (== 0)) $ iterate nextRow is

predictForRow forward is = sum . reverse $ map (\xs -> sign * last xs) $ generateRows is
  where sign = if forward then 1 else -1

aoc2023_09 (a:as) = do
  content <- readFile a
  let input = map (map (\w -> read w :: Int) . words) $ lines content
  print . sum $ map (predictForRow True) input
  print . negate . sum $ map (predictForRow False . reverse) input
