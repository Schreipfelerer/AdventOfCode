#!/usr/bin/env runhaskell
module Main where

import Data.List (elemIndex)
import Data.Maybe (fromMaybe)

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
solvePart1 (x : _) = show $ loopRedist x []

loopRedist :: Line -> [Line] -> Int
loopRedist x c =
  if x `elem` c
    then 0
    else 1 + loopRedist (redist x) (x : c)

noLoopRedist :: Line -> [Line] -> Int
noLoopRedist x c =
  if x `elem` c
    then loopRedist x []
    else noLoopRedist (redist x) (x : c)

redist :: Line -> Line
redist x =
  let h = maximum x
      i = fromMaybe (-1) $ elemIndex h x
      r = h `mod` length x
   in zipWith (\y yi -> (if yi == i then 0 else y) + h `quot` length x + fromEnum ((yi - i - 1) `mod` length x < r)) x [0..]

solvePart2 :: [Line] -> String
solvePart2 (x : _) = show $ noLoopRedist x []

main :: IO ()
main = do
  lines <- loadFile "input6.txt"
  putStrLn $ "Part 1: " ++ solvePart1 lines
  putStrLn $ "Part 2: " ++ solvePart2 lines
  return ()
