use crate::utils::read_input_file;
use fancy_regex::Regex;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day02", input_file);

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
    let pattern = Regex::new(r"^(\d+)\1$").unwrap();
    let mut invalid = 0;
    for line in input.trim().split(',').map(|x| x.split_once("-").unwrap()){
        let (from, to) = line;
        for num in from.parse::<i64>().unwrap()..=to.parse::<i64>().unwrap(){
            if pattern.is_match(&num.to_string()).unwrap() {invalid += num}
        }
    }
    invalid
}

fn part2(input: &str) -> i64 {
    let pattern = Regex::new(r"^(\d+)\1+$").unwrap();
    let mut invalid = 0;
    for line in input.trim().split(',').map(|x| x.split_once("-").unwrap()){
        let (from, to) = line;
        for num in from.parse::<i64>().unwrap()..=to.parse::<i64>().unwrap(){
            if pattern.is_match(&num.to_string()).unwrap() {invalid += num}
        }
    }
    invalid
}
