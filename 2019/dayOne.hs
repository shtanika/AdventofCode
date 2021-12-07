getNumbers :: String -> [Int]
getNumbers str = map (read::String -> Int) $ words str

calcFuel :: Int -> Int
calcFuel x = if(div x 3 - 2 > 0) then div x 3 - 2 else 0

recFuel :: Int -> Int 
recFuel 0 = 0
recFuel x = calcFuel x + recFuel(calcFuel x)

main :: IO ()
main= do
    content <- readFile "2019/inputs/1.txt"
    let numbers = getNumbers content
    
    print $ sum [calcFuel x | x <- numbers]
    print $ sum [recFuel x | x <- numbers]
    print $ recFuel 2