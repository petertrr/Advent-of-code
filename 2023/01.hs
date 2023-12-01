import System.IO
import Data.Char
import Data.List

digitsAsWords = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

main :: IO ()
main = do
    content <- readFile "01.input"
    let linesOfFile = lines content
    putStrLn . show . result $ linesOfFile
      where result = \lines -> sum $ map processLine lines
            processLine line = 10 * firstDigit digitsAsWords line + lastDigit digitsAsWords line
            firstDigit words line = head $ filter (\x -> x >= 0) (map (\x -> getLeadingDigitIfAny words x) (tails line))
            lastDigit words line = firstDigit (map reverse words) (reverse line)
-- Implementation for Part 1
--            getLeadingDigitIfAny = \s -> if isDigit . head $ s then digitToInt . head $ s else -1
-- Implementation for Part 2
            getLeadingDigitIfAny words s = if isDigit . head $ s then digitToInt . head $ s else getLeadingDigitFromWord words s
            getLeadingDigitFromWord words s = case (maybeFirstDigitFromWord words s) of
              Just (ss) -> ss
              Nothing -> -1
              where maybeFirstDigitFromWord words s = case (wordAtStartOf s) of
                      (x:xs) -> elemIndex x words
                      [] -> Nothing
                      where wordAtStartOf s = filter (\w -> isPrefixOf w s) words

