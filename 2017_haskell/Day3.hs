module Main where

type Line = Int

loadFile :: String -> IO [Line]
loadFile fname = do
  s <- readFile fname
  case traverse parseLine (lines s) of
    Nothing -> error "some line failed to parse"
    Just people -> pure people


parseLine :: String -> Maybe Line
parseLine i = Just $ read i

solvePart1 :: [Line] -> String
solvePart1 (x:_) = show $ let s = (getSquare x) in 
                           (quot (s+1) 2)+(abs $ x-(s*s+(quot (s+1) 2)+(quot ((s+2)*(s+2)-s*s) 4) * quot (x - s*s - 1) (quot ((s+2)*(s+2)-s*s) 4)))

-- r^2 < x <= (2+r)^2
getSquare :: Int -> Int
getSquare 1 = 0
getSquare x = (\x -> if odd x then x else x-1) $ floor $ sqrt $ fromIntegral x-1

solvePart2 :: [Line] -> String
solvePart2 (x:_) = show x

main :: IO ()
main = do
  lines <- loadFile "input3.txt"
  putStrLn $ "Part 1: " ++ solvePart1 lines
  putStrLn $ "Part 2: " ++ solvePart2 lines
  return ()
