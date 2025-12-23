module Aoc01 where

import System.IO
import Data.Char
import Data.List

dialStart = DialState 50 0

getRotation :: String -> Int
getRotation line = case line of
    'L' : ds -> negate (read ds)
    'R' : ds -> read ds
    _        -> error ("Invalid instruction: " ++ line)

data DialState = DialState { dial :: Int, timesCrossedZero :: Int }
  deriving Show

aoc2025_01 args = do
  content <- readFile $ head args
  let linesOfFile = lines content
  print . show . getResult $ linesOfFile
  where getResult linesOfFile = 
          let sts = states linesOfFile
          in ( length . filter (\state -> dial state == 0) $ sts, last sts)
        states linesOfFile = scanl updateState dialStart $ map getRotation linesOfFile
        updateState (DialState dial timesCrossedZero) inc = DialState {
          dial = (dial + inc) `mod` 100
          , timesCrossedZero = timesCrossedZero + hasCrossedZero dial inc
        }
        hasCrossedZero current inc = abs p + adj1 + adj2
          where (p, q) = divMod (current + inc) 100
                adj1 = if inc <= 0 && current == 0 then -1 else 0 -- fix going left from zero
                adj2 = if inc <= 0 && q == 0 then 1 else 0        -- fix going left to zero
