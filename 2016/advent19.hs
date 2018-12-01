--solutions from reddit

--first part
main = print (solve 3004953) where solve n = 1 + 2 * (n - 2 ^ (floor $ logBase 2 n))

--second part
steal l = drop 1 l' ++ take 1 l'
    where l' = filter (/= (l !! div (length l) 2)) l

solve n = head $ until ((==1) . length) steal [1..n]

--main = print $ zip [1..] $ map solve [1..100]