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
solvePart2 x =
  let root = solvePart1 x
   in show $ balance x root (sumTree x root)

balance :: [Line] -> String -> Int -> Int
balance x h b =
  let stuff = getStuff x h
      sums = map (sumTree x) (snd stuff)
   in if tail sums == init sums
        then b - sum sums 
        else balance x (snd stuff !! difInd sums) (sums!!fromEnum (0 == difInd sums)) 

difInd :: [Int] -> Int 
difInd (a:b:c:_) 
 | a == b = 2
 | otherwise = fromEnum $ a == c

sumTree :: [Line] -> String -> Int
sumTree x h =
  let stuff = getStuff x h
   in fst stuff + sum (map (sumTree x) (snd stuff))

getStuff :: [Line] -> String -> (Int, [String])
getStuff x h = (\(_, z1, z2) -> (z1, z2)) $ head $ filter (\y -> h == fst3 y) x

main :: IO ()
main = do
  lines <- loadFile "input7.txt"
  putStrLn $ "Part 1: " ++ solvePart1 lines
  putStrLn $ "Part 2: " ++ solvePart2 lines
  return ()
