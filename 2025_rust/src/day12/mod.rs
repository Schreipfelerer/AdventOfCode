use itertools::Itertools;

use crate::utils::read_input_file;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day12", input_file);

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
    let mut raw = input.trim_end().split("\n\n").collect_vec();
    let spaces = raw
        .pop()
        .unwrap()
        .split("\n")
        .map(|l| l.split_once(": ").unwrap())
        .map(|i| {
            (
                i.0.split_once("x").unwrap(),
                i.1.split(" ").map(|n| n.parse::<i64>().unwrap()).collect_vec(),
            )
        })
        .collect_vec();
    let shapes = raw
        .iter()
        .map(|f| f.chars().filter(|c| *c == '#').count() as i64)
        .collect_vec();
    
    //naive?
    let mut fitting_spaces = 0;
    for ((x, y), requirements) in spaces{
        let room = x.parse::<i64>().unwrap() * y.parse::<i64>().unwrap();
        let needed = requirements.iter().enumerate().map(|(i, n)| *n*shapes[i]).sum();
        if room >= needed{
            fitting_spaces += 1
        }
    }
    fitting_spaces
}

fn part2(_input: &str) -> i64 {
    80085
}
