use crate::utils::read_input_file;
use itertools::Itertools;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day09", input_file);

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
    let rectangles: Vec<(isize, isize)> = input
        .lines()
        .map(|x| {
            let (from, to) = x.split_once(",").unwrap();
            (from.parse().unwrap(), to.parse().unwrap())
        })
        .collect();
    let mut biggest = 0;
    for x1 in 0..rectangles.len() {
        for x2 in x1 + 1..rectangles.len() {
            let rec1 = rectangles[x1];
            let rec2 = rectangles[x2];
            biggest = biggest.max((rec1.0.abs_diff(rec2.0) + 1) * (rec1.1.abs_diff(rec2.1) + 1));
        }
    }
    biggest as i64
}

fn part2(input: &str) -> i64 {
    let rectangles: Vec<(isize, isize)> = input
        .lines()
        .map(|x| {
            let (from, to) = x.split_once(",").unwrap();
            (from.parse().unwrap(), to.parse().unwrap())
        })
        .collect();

    let lines = rectangles.iter().circular_tuple_windows::<(_, _)>();
    let mut biggest = 0;
    for x1 in 0..rectangles.len() {
        for x2 in x1 + 1..rectangles.len() {
            let c1 = rectangles[x1];
            let c2 = rectangles[x2];
            let mut is_intersecing = false;
            for (p1, p2) in lines.clone() { // Check if any lines intersect
                if p1.0 == p2.0 && p1.0 > c1.0.min(c2.0) && p1.0 < c1.0.max(c2.0){ // Same x
                    if p1.1.min(p2.1) < c1.1.max(c2.1) && p1.1.max(p2.1) > c1.1.min(c2.1){ // inside
                        is_intersecing = true;
                        break;
                    }
                }
                else if p1.1 == p2.1 && p1.1 > c1.1.min(c2.1) && p1.1 < c1.1.max(c2.1){ // Same y
                    if p1.0.min(p2.0) < c1.0.max(c2.0) && p1.0.max(p2.0) > c1.0.min(c2.0){ // inside
                        is_intersecing = true;
                        break;
                    }
                }
            }
            if is_intersecing{continue;}
            // WARNING this assumes that any rectangles that are completly outside the area is
            // smaller than the biggest on the inside
            biggest = biggest.max((c1.0.abs_diff(c2.0) + 1) * (c1.1.abs_diff(c2.1) + 1));
        }
    }
    biggest as i64
}
