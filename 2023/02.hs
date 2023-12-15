import System.IO
import Data.Char
import Data.List
import Data.Bifunctor

splitBy delimiter = foldr f [[]] 
         where f c l@(x:xs) | c == delimiter = []:l
                            | otherwise = (c:x):xs

nRed = 12
nGreen = 13
nBlue = 14

trim :: String -> String
trim = f . f
   where f = reverse . dropWhile isSpace

data Color = Red | Green | Blue deriving (Enum, Eq, Show)
asColor s = case s of 
             "red" -> Red
             "green" -> Green
             "blue" -> Blue

parse :: [String] -> (Integer, [[(Integer, Color)]])
parse x
       = let title = head x
             gameNumber = read . last . words $ title :: Integer
             content = last x
             rawRecords = map (splitBy ',' ) $ splitBy ';' content :: [[String]]
             parseRecord r = (headToInt r, asColor . last . words $ r)
              where headToInt r = read . trim . head . words $ r :: Integer
             records = map (map parseRecord) rawRecords
             in (gameNumber, records)

maxByCount :: Color -> [(Integer, Color)] -> [(Integer, Color)] -> (Integer, Color)
maxByCount col r1 r2
 = let count1 = fst <$> find ((==) col . snd) r1
       count2 = fst <$> find (\p -> snd p == col) r2
       in case (count1, count2) of
           (Just c1, Nothing) -> (c1, col)
           (Nothing, Just c2) -> (c2, col)
           (Just c1, Just c2) -> (max c1 c2, col)
           (Nothing, Nothing) -> (0, col)

main :: IO ()
main = do
   content <- readFile "02.input"
   let linesOfFile = lines content
   let splits = map (splitBy ':') linesOfFile
   let games = map parse splits :: [(Integer, [[(Integer, Color)]])]
   let possible = filter (all (all isPossible) . snd) games
        where isPossible r = case snd r of
                                  Red -> fst r <= nRed
                                  Green -> fst r <= nGreen
                                  Blue -> fst r <= nBlue
   print . sum $ map fst possible
   let minimal = map minimalColors games
        where minimalColors :: (Integer, [[(Integer, Color)]]) -> (Integer, [(Integer, Color)])
              minimalColors records
               = let merge :: [(Integer, Color)] -> [(Integer, Color)] -> [(Integer, Color)]
                     merge r g = [maxByCount Red r g, maxByCount Green r g, maxByCount Blue r g]
                     in second (foldr merge (last $ snd records)) records
   print . sum $ map (product . map fst . snd) minimal
