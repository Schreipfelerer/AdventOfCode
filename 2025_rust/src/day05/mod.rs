use std::{ops::RangeInclusive};

use crate::utils::read_input_file;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day05", input_file);

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
    let (ranges_str, checks) = input.split_once("\n\n").unwrap();
    let ranges: Vec<RangeInclusive<i64>> = ranges_str
        .lines()
        .map(|range| {
            let (from, to) = range.split_once("-").unwrap();
            from.parse::<i64>().unwrap()..=to.parse().unwrap()
        })
        .collect();

    checks
        .lines()
        .filter(|x| {
            ranges
                .iter()
                .any(|range| range.contains(&(x.parse::<i64>().unwrap())))
        })
        .count() as i64
}

fn part2(input: &str) -> i64 {
    let (ranges_str, _) = input.split_once("\n\n").unwrap();
    let mut ranges: Vec<RangeInclusive<i64>> = ranges_str
        .lines()
        .map(|range| {
            let (from, to) = range.split_once("-").unwrap();
            from.parse::<i64>().unwrap()..=to.parse().unwrap()
        }).collect();

    ranges.sort_by_key(|r| *r.start());

    let mut lower_bound = i64::MIN;
    let mut included = 0;

    for r in ranges{
        if *r.start() > lower_bound {
            included += *r.end() - *r.start() + 1;
            lower_bound = *r.end();
        }
        else if *r.end() > lower_bound {
            included += *r.end() - lower_bound;
            lower_bound = *r.end();
        }

    }

    included
}
