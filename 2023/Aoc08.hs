module Aoc08 where

import System.IO
import Data.List
import Data.Map (Map)
import qualified Data.Map as Map
import Data.List.Split
import Data.Char

trim = f . f
   where f = reverse . dropWhile isSpace

data Node = Node { left :: String, right :: String, title :: String }

lineToNode l
  = let splits = map trim $ splitOn "=" l
        title = head splits
        children = last splits
        childrenNames = map trim $ splitOn "," $ dropWhile (== '(') $ takeWhile (/= ')') children
        in Node (head childrenNames) (last childrenNames) title

buildGraph = Map.fromList . map lineToTuple
  where lineToTuple l = nodeToTuple $ lineToNode l
        nodeToTuple n = (title n, n)

data Instruction = R | L

parseInstruction c | c == 'R' = R | c == 'L' = L

applyInstruction :: (String, Node) -> Instruction -> String
applyInstruction (title, node) instr = case instr of
 R -> right node
 L -> left node

step :: Map String Node -> String -> Instruction -> String
step g t i = applyInstruction (t, (Map.!) g t) i

steps graph start instructions = scanl (\t i -> step graph t i) start (cycle instructions)

takeWhile' :: (a -> Bool) -> [[a]] -> [[a]]
takeWhile' p xss = let
  currentMatch = all (p . head) xss
  in map (takeWhile (const currentMatch)) xss
-- | all (p . head) xss = takeWhile' p $ map tail xss
-- | otherwise = []

aoc2023_08 args = do
  content <- readFile $ head args
  let contentLines = lines content
  let instructions = map parseInstruction $ head contentLines
  let graph = buildGraph $ tail contentLines
-- Part 1
  print . length $ takeWhile (/= "ZZZ") $ steps graph "AAA" instructions
--  Part 2
--  let parallelSteps = transpose $ map (\t -> steps graph t instructions) $ filter (isSuffixOf "A") $ Map.keys graph
--  print . length $ takeWhile (not . all (isSuffixOf "Z")) parallelSteps
--  print . foldr (\a b -> b + 1) 0 $ takeWhile (not . all (isSuffixOf "Z")) parallelSteps
