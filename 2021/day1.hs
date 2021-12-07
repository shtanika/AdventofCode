-- PART ONE: CHECK IF CURRENT LINE IS LARGER THAN LAST LINE
-- access file, somehow do list comprehension to compare values?
-- import System.IO 

import System.IO

getNumbers :: String -> [Int]
getNumbers str = map (read::String -> Int) $ words str


-- take out first number
-- compare taken out number to new first number
--  if smaller add 1
--  if less or equal
compareFirstTwo :: [Int] -> Int 
compareFirstTwo (a:b:xs) = isIncrement a b
compareFirstTwo(x:xs) = 0
compareFirstTwo [] = 0
-- compareFirstTwo xs = isIncrement (head xs) (head $ tail xs)

isIncrement :: Int -> Int -> Int
isIncrement a b = if a<b then 1 else 0

countIncrements :: [Int] -> Int
countIncrements [] = 0
countIncrements xs = compareFirstTwo xs + countIncrements(tail xs)


-- PART TWO: CHECK EACH TRIO OF NUMBERS (INCLUSIVE) IF LARGER THAN LAST TRIO
compareFirstThree :: [Int] -> Int 
compareFirstThree (a:b:c:d:xs) = isIncrement (sum [a,b,c]) (sum[b,c,d])
compareFirstThree(x:xs) = 0
compareFirstThree [] = 0

countSumIncrements :: [Int] -> Int 
countSumIncrements [] = 0
countSumIncrements xs = compareFirstThree xs + countSumIncrements (tail xs)

main :: IO ()
main = do
    content <- readFile "2021/inputs/1.txt"
    let bigNumbers = getNumbers content

    -- part 1
    let part1 = "part 1: " ++ show (countIncrements bigNumbers)
    putStrLn part1 
    putStrLn ""

    -- part 2 
    let part2 = "part 2: "++ show (countSumIncrements bigNumbers)
    putStrLn part2




