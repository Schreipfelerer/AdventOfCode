#!/usr/bin/env runhaskell
module Main where

type Line = Int

loadFile :: String -> IO [Line]
loadFile fname = do
  s <- readFile fname
  case traverse parseLine (lines s) of
    Nothing -> error "some line failed to parse"
    Just people -> pure people

parseLine :: String -> Maybe Line
parseLine = Just . read

solvePart1 :: [Line] -> String
solvePart1 x = show $ stepsToExit x 0

stepsToExit :: [Line] -> Int -> Int
stepsToExit !x i =
  if i < 0 || i >= length x
    then 0
    else 1 + stepsToExit (take i x ++ (x !! i) + 1 : drop (i + 1) x) (i + x !! i)

solvePart2 :: [Line] -> String
solvePart2 x = show $ stepsToExitJumps x 0

stepsToExitJumps :: [Line] -> Int -> Int
stepsToExitJumps !x i =
  if i < 0 || i >= length x
    then 0
    else let jump = x !! i in 1 + stepsToExitJumps (take i x ++ jump + (if jump >= 3 then -1 else 1) : drop (i + 1) x) (i + jump)

main :: IO ()
main = do
  lines <- loadFile "input5.txt"
  putStrLn $ "Part 1: " ++ solvePart1 lines
  putStrLn $ "Part 2: " ++ solvePart2 lines
  return ()
