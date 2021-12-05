getNumbers :: String -> [Int]
getNumbers str = [(read::String -> Int) x | x <- wordsWhen (==',') str]


wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

getNumber :: [Int] -> Int -> Int
getNumber lst n = lst !! n

getSublist :: [Int] -> Int -> Int -> [Int]
getSublist lst start end = drop start . take end $ lst

find :: Eq t => t -> [t] -> Bool
find _ [] = False
find n (x:xs)
  | x == n = True
  | otherwise = find n xs


checkHalt :: [Int] -> Int -> Bool
{-

checkHalt lst index =
  99 `elem` [x | x <- getSubList lst index (index + 3)]
    || null [x | x <- getSubList lst index (index + 3)]
-}

checkHalt lst index = getNumber lst index == 99

doStep :: [Int] -> Int -> Int
-- doStep xs n = if (a ==1) then xs!! (xs!!(n+1)) + xs !! (xs!!(n+2)) else 
doStep lst n = if (lst !! n == 1)
    then getNumber lst (lst!!(n+1)) + getNumber lst (lst!!(n+2))
    else getNumber lst (lst!!(n+1)) * getNumber lst (lst!!(n+2))

replace :: Int -> a -> [a] -> [a]
replace pos newVal list = take pos list ++ newVal : drop (pos+1) list

-- if 1 or 2
-- then continue program
-- else first number 
--intCode :: [Int] -> Int 
intCode :: [Int] -> Int -> [Int]
intCode lst index = if checkHalt lst index then lst else 
    intCode (replace (getNumber lst (index+3)) (doStep lst index) lst) (index+4) 


intCode2 :: [Int] -> Int -> [Int]
intCode2 lst index = if not(99 `elem` ([x | x <- getSublist lst index (index+3)]) ||
                        null  [x | x <- getSublist lst index (index+3)]) 
    then intCode (replace (lst !! (index+3)) (doStep lst index) lst) (index+4)
    else lst

main :: IO ()
main = do
    content <- readFile "2019/inputs/two.txt"
    let numbers = getNumbers content
    let newNumbers1 = replace 1 12 numbers
    let newNumbers2 = replace 2 2 newNumbers1

    let test1 = [1,9,10,3,2,3,11,0,99,30,40,50]
    let test2 = [1,9,10,70,2,3,11,0,99,30,40,50]
    let test3 = [1,0,0,3,1,1,2,3]
    --print numbers
    --print $ replace 0 2 [1,0,5,0]
    --print $ checkHalt [1,0,2,0, 99] 0

    --print $ replace (getNumber test1 3) (doStep test1 0) test1
    --print $ replace (getNumber test2 7) (doStep test2 4) test2

    --print $ intCode test3 0

    putStrLn "real ver"
    print $ intCode newNumbers2 0
    print $ doStep newNumbers2 0
    print $ newNumbers2 !! 12
    print $ newNumbers2 !! 2
    putStrLn "??? ver"
    print $ intCode2 newNumbers2 0