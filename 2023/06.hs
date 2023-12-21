import System.IO
import Data.Char
import Data.List

toInt s = read s :: Int

splitBy delimiter = foldr f [[]]
         where f c l@(x:xs) | c == delimiter = []:l
                            | otherwise = (c:x):xs

trim :: String -> String
trim = f . f
   where f = reverse . dropWhile isSpace

solutionsInPair :: (Int, Int) -> Int
solutionsInPair (time, length)
  = let d = sqrt . fromIntegral $ time^2 - 4 * length
        left = (fromIntegral time - d) / 2
        right = (fromIntegral time + d) / 2
        in floor right - ceiling left + 1

main :: IO()
main = do
  content <- readFile "06.input"
  let dataLines = map (\l -> last $ splitBy ':' l) $ lines content
  let part1 = map (\l -> map toInt $ words l) dataLines
  let pairs = zip (head part1) (last part1)
  print . product $ map solutionsInPair pairs
  let part2 = map (toInt . trim . concat . words) dataLines
  print $ solutionsInPair (head part2, last part2)
