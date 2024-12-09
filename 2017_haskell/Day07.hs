#!/usr/bin/env runhaskell
module Main where

import Data.Tuple.Extra (fst3)

type Line = (String, Int, [String])

loadFile :: String -> IO [Line]
loadFile fname = do
  s <- readFile fname
  case traverse parseLine (lines s) of
    Nothing -> error "some line failed to parse"
    Just people -> pure people

parseLine :: String -> Maybe Line
parseLine i =
  let w = words i
   in Just (head w, read (tail $ init (w !! 1)), drop 3 (map (filter (',' /=)) w))

solvePart1 :: [Line] -> String
solvePart1 x =
  let w = foldl (\ws (_, _, y) -> ws ++ y) [] x
   in fst3 $ head $ filter (\(n, _, l) -> n `notElem` w && not (null l)) x

solvePart2 :: [Line] -> String
solvePart2 _ = ""

main :: IO ()
main = do
  lines <- loadFile "input7.txt"
  putStrLn $ "Part 1: " ++ solvePart1 lines
  putStrLn $ "Part 2: " ++ solvePart2 lines
  return ()
