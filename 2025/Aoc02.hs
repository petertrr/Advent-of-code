module Aoc02 where

import System.IO
import Data.Char
import Data.List
import Data.List.Split (chunksOf)
import qualified Data.Text as T
import Debug.Trace

allEqual xs = and $ zipWith (==) xs (tail xs)

digits :: Integer -> [Int]
digits = map digitToInt . show

isRepetitionK :: [Int] -> Int -> Bool
isRepetitionK dgts k
    | length dgts `rem` k /= 0 = False
    | otherwise = allEqual (chunksOf k dgts)

isInvalidPart1 :: Integer -> Bool
isInvalidPart1 i
  | odd len = False
  | otherwise = isRepetitionK dgts (len `div` 2)
  where len = length dgts
        dgts = digits i
    
isInvalidPart2 :: Integer -> Bool
isInvalidPart2 i = any (\k -> isRepetitionK dgts k) [1..(len - 1)]
    where len = length dgts
          dgts = digits i

getBorders :: T.Text -> [Integer]
getBorders rngString = map (read . T.unpack) $ T.split (== '-') rngString
    
getRange :: [Integer] -> [Integer]
getRange borders = [head borders..last borders]
    
ranges :: String -> [[Integer]]
ranges lineOfFile = map (getRange . getBorders) (T.split (== ',') . T.pack $ lineOfFile)

isInvalid = isInvalidPart2

aoc2025_02 args = do
  content <- readFile $ head args
  let lineOfFile = head $ lines content
  print . show . getResult $ lineOfFile
  where getResult lineOfFile = sum . concatMap (filter isInvalid) $ ranges lineOfFile
