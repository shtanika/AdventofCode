import Text.XHtml.Strict (content)

getNumbers :: String -> [Int]
getNumbers str = [read x :: Int | x <- wordsWhen (==',') str]

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

getCommand :: String -> [String]
getCommand str = [read x :: String | x <- wordsWhen (=='\n') str]

getCommandAndValue :: String -> (String, Int)
getCommandAndValue str = (head $ wordsWhen(==' ')str, read (wordsWhen(==' ')str !! 1) :: Int)


calcPos :: (String, Int) -> (Int, Int)
calcPos ("forward", b) = (b, 0)
calcPos ("up", b) = (0,-b)
calcPos ("down", b) = (0,b)


-- (horizontal, depth)
followInstructions :: [(String, Int)] -> [(Int, Int)] -> [(Int, Int)]
followInstructions [] pos = pos
followInstructions lst pos = calcPos (head lst) : followInstructions (tail lst) pos



--PART 2
calcPos2 :: (String, Int) -> (Int, Int, Int)
calcPos2 ("forward", b) = (b, 0, 0)
calcPos2 ("up", b) = (0, 0, -b)
calcPos2 ("down", b) = (0, 0, b)

combine :: (Int, Int, Int) -> [(Int, Int, Int)] -> [(Int, Int, Int)]
combine (a,b,c) [] = [(a,b,c)]
-- combine (a,b,c) (z,x,y)(:d) = (a+z,b+z*c,c+y) : combine (a+z,b+a*c,c+y) d
combine (a,b,c) ((z,0,0):d) = (a+z,b+z*c,c) : combine (a+z,b+z*c,c) d
combine (a,b,c) ((0,0,y):d) = (a,b,c+y) : combine (a,b,c+y) d


-- (horizontal, depth)
-- pos - (horizontal, depth, aim)
followInstructions2 :: [(String, Int)] -> [(Int, Int, Int)] -> [(Int, Int, Int)]
followInstructions2 [] pos = pos
followInstructions2 lst pos = calcPos2 (head lst) : followInstructions2 (tail lst) pos

mult :: (Int, Int, Int) -> Int 
mult (a,b,c) = a*b

main :: IO ()
main = do
    content <- readFile "day2/input.txt"
    let commands = [getCommandAndValue x | x <- wordsWhen(=='\n') content]
    let steps = followInstructions commands []

    let steps2 = followInstructions2 commands []
    --print steps

    print "PART ONE"
    print $ sum (map fst steps) * sum (map snd steps)

    print "PART TWO"
    --print steps2
    print $ mult $ last $ combine (0,0,0) steps2






