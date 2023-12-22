import System.IO
import Data.List
import Data.Ord
import Data.Bifunctor

cardTypes = map head $ ["A", "K", "Q", "J", "T"] ++ map show [9, 8..2]
data CardType = CardType {value :: Char} deriving (Eq)

instance Ord CardType where
  compare = comparing (\ct -> elemIndex (value ct) cardTypes)

compareByStrongestCard s1 s2 = head $ dropWhile (== EQ) (zipWith (flip $ comparing CardType) s1 s2)

data Hand = Hand {hand :: String,
                  strength :: Int}
  deriving (Show, Eq)

instance Ord Hand where
  compare h1 h2
    | cmp == EQ = compareByStrongestCard (hand h1) (hand h2)
    | otherwise = cmp
    where cmp = compare (strength h1) (strength h2)

toInt s = read s :: Int

toTuple [l1, l2] = (l1, l2)

countChars s = map (\x -> (head x, length x)) $ group $ sort s

parseHand :: String -> Hand
parseHand s 
  | 5 `elem` values = Hand s 6
  | 4 `elem` values = Hand s 5
  | 3 `elem` values && 2 `elem` values = Hand s 4
  | 3 `elem` values = Hand s 3
  | length (filter (== 2) values) == 2 = Hand s 2
  | 2 `elem` values = Hand s 1
  | otherwise = Hand s 0
  where counts = countChars s
        values = map snd counts

main = do
  content <- readFile "07.input"
  let input = map (toTuple . words) $ lines content
  let handsWithBids = map (Data.Bifunctor.first parseHand) input
  let sortedIndexedHandsWithBids = zip [1..] $ sortBy (comparing fst) handsWithBids
  print . sum $ map (\(i, (_, bid)) -> i * toInt bid) sortedIndexedHandsWithBids
   
