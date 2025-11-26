use std::collections::{HashMap, HashSet};

use crate::utils::read_input_file;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day06", input_file);

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
    let mut orbits = HashMap::new();
    let mut planets = HashSet::new();

    for line in input.lines() {
        let (a, b) = line.split_once(')').unwrap();
        planets.insert(a);
        planets.insert(b);
        orbits.insert(b, a);
    }

    planets.iter().map(|p| get_orbitchain(p, &orbits).iter().count() as i64).sum()
}

fn part2(input: &str) -> i64 {
    let mut orbits = HashMap::new();

    for line in input.lines() {
        let (a, b) = line.split_once(')').unwrap();
        orbits.insert(b, a);
    }

    let you = get_orbitchain("YOU", &orbits);
    let san = get_orbitchain("SAN", &orbits);
    let duplicates = you.iter().copied().filter(|x| san.contains(x)).count();

    (you.len() + san.len() - (duplicates * 2)) as i64
}

fn get_orbitchain<'a>(planet: &str, orbits: &'a HashMap<&'a str, &'a str>) -> Vec<&'a str> {
    match orbits.get(planet) {
        Some(parent) => {
            let mut chain = get_orbitchain(parent, orbits);
            chain.push(parent);
            chain
        }
        None => Vec::new(),
    }
}
