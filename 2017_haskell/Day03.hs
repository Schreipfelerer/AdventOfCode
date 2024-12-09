#!/usr/bin/env runhaskell

import Data.Bool

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
solvePart1 (1 : _) = "0"
solvePart1 (x : _) =
  show $
    let s = (bool =<< subtract 1) <*> odd $ floor . sqrt $ fromIntegral x - 1
        i = side `quot` 2
        side = s + 1
        lower_s = x - s * s
     in i + abs (lower_s - (i + side * ((lower_s - 1) `quot` side)))

solvePart2 :: [Line] -> String
solvePart2 (x : _) = show x

main :: IO ()
main = do
  lines <- loadFile "input3.txt"
  putStrLn $ "Part 1: " ++ solvePart1 lines
  putStrLn $ "Part 2: " ++ solvePart2 lines
  return ()
