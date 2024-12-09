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
parseLine i = Just $ map read (words i)

solvePart1 :: [Line] -> String
solvePart1 x = show $ sum $ map (\x -> maximum x - minimum x) x

solvePart2 :: [Line] -> String
solvePart2 x = show $ sum $ map (\xs -> sum [quot x y | x <- xs, y <- xs, rem x y == 0, x /= y]) x

main :: IO ()
main = do
  lines <- loadFile "input2.txt"
  putStrLn $ "Part 1: " ++ solvePart1 lines
  putStrLn $ "Part 2: " ++ solvePart2 lines
  return ()
