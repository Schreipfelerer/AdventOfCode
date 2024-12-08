#!/usr/bin/env runhaskell
module Main where

type Line = [Int]

loadFile :: String -> IO [Line]
loadFile fname = do
  s <- readFile fname
  case traverse parseLine (lines s) of
    Nothing -> error "some line failed to parse"
    Just people -> pure people


parseLine :: String -> Maybe Line
parseLine (i:is) = case parseLine is of 
    Nothing -> Nothing
    Just rest -> Just $ read [i] : rest
parseLine i = Just []

solvePart1 :: [Line] -> String
solvePart1 (x:_) = show $ sum $ zipWith (\y z -> if y == z then y else 0) (last x : init x) x

solvePart2 :: [Line] -> String
solvePart2 (x:_) = show $ sum $ zipWith (\y z -> if y == z then y else 0) (rotateListFor (length x) x) x

rotateListFor :: Int -> [a] -> [a]
rotateListFor 0 x = x
rotateListFor i x = rotateListFor (i-2) (last x : init x)

main :: IO ()
main = do
  lines <- loadFile "input1.txt"
  putStrLn $ "Part 1: " ++ solvePart1 lines
  putStrLn $ "Part 2: " ++ solvePart2 lines
  return ()
