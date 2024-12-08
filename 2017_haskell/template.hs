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
solvePart1 _ = ""

solvePart2 :: [Line] -> String
solvePart2 _ = ""


main :: IO ()
main = do
  lines <- loadFile "example.txt"
  putStrLn $ "Part 1: " ++ solvePart1 lines
  putStrLn $ "Part 2: " ++ solvePart2 lines
  return ()

