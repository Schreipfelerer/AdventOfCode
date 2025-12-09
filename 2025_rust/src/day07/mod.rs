use std::collections::{HashMap, HashSet};

use crate::utils::read_input_file;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day07", input_file);

    match part.map(|s| s.as_str()) {
        Some("1") => println!("Part 1: {}", part1(&input)),
        Some("2") => println!("Part 2: {}", part2(&input)),
        _ => {
            // run both if no part specified
            println!("Part 1: {}", part1(&input));
            println!("Part 2: {}", part2(&input));
        }
    }
}

fn part1(input: &str) -> i64 {
    let mut lines = input.lines();
    let start = lines.next().unwrap().chars().position(|x| x == 'S').unwrap();
    let mut splits = 0;
    let mut beams: HashSet<usize> = HashSet::new();
    beams.insert(start);
    for line in lines{
        let chars: Vec<char> = line.chars().collect();
        let mut new_beams: HashSet<usize> = HashSet::new(); 
        for beam in &beams{
            if chars[*beam] == '^'{
                new_beams.insert(beam - 1);
                new_beams.insert(beam + 1);
                splits += 1
            }
            else {
                new_beams.insert(*beam);
            }
        }
        beams = new_beams;
    }
    splits
}

fn part2(input: &str) -> i64 {
    let mut lines = input.lines();
    let start = lines.next().unwrap().chars().position(|x| x == 'S').unwrap();
    let mut beams: HashMap<usize, i64> = HashMap::new();
    beams.insert(start, 1);
    for line in lines{
        let chars: Vec<char> = line.chars().collect();
        let mut new_beams: HashMap<usize, i64> = HashMap::new(); 
        for (beam, number) in beams{
            if chars[beam] == '^'{
                *new_beams.entry(beam - 1).or_default() += number;
                *new_beams.entry(beam + 1).or_default() += number;
            }
            else {
                *new_beams.entry(beam).or_default() += number;
            }
        }
        beams = new_beams;
    }
    beams.values().sum()
}
