#!/usr/bin/env runhaskell
module Main where
import Data.List (nub, sort)
import Data.Function (on)

type Line = [String]

loadFile :: String -> IO [Line]
loadFile fname = do
  s <- readFile fname
  case traverse parseLine (lines s) of
    Nothing -> fail "some line failed to parse"
    Just people -> pure people


parseLine :: String -> Maybe Line
parseLine = Just . words

solvePart1 :: [Line] -> String
solvePart1 = show . length . filter (((==) `on` length) <*> nub)

solvePart2 :: [Line] -> String
solvePart2 = show  . length . filter (((==) `on` length) <*> nub . map sort)


main :: IO ()
main = do
  lines <- loadFile "input4.txt"
  putStrLn $ "Part 1: " ++ solvePart1 lines
  putStrLn $ "Part 2: " ++ solvePart2 lines
  return ()

