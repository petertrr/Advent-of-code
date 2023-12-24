module Aoc11 where

import System.IO
import Data.List

space = '.'
galaxy = '#'

data Galaxy = Galaxy {x :: Int, y :: Int}

mhDistance :: Galaxy -> Galaxy -> Int
mhDistance g1 g2 = abs (x g1 - x g2) + abs (y g1 - y g2)

parseLine :: Int -> String -> [Galaxy]
parseLine y line = map (\(x, c) -> Galaxy x y) $ filter (\(_, c) -> c == galaxy) $ zip [0..] line

countEmptyLinesBetween :: Int -> Int -> [String] -> Int
countEmptyLinesBetween y1 y2 lines = length $ filter (all (space ==)) $ take (yMax - yMin) $ drop yMin lines
  where yMax = max y1 y2
        yMin = min y1 y2

pairs [x] = []
pairs (x:xs) = map (\x' -> (x, x')) xs ++ pairs xs

aoc2023_11 (a:as) = do
  content <- readFile a
  let unexpanded = lines content
  let galaxies = concatMap (uncurry parseLine) $ zip [0..] unexpanded
  let adjust f g1 g2 arr = countEmptyLinesBetween (f g1) (f g2) arr
  let adjustments = map (\(g1, g2) -> adjust x g1 g2 (transpose unexpanded) + adjust y g1 g2 unexpanded) $ pairs galaxies
  print . sum $ zipWith (+) adjustments $ map (uncurry mhDistance) $ pairs galaxies
  print . sum $ zipWith (+) (map (* 999999) adjustments) $ map (uncurry mhDistance) $ pairs galaxies
