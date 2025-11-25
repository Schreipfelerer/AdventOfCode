use crate::utils::read_input_file;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day01", input_file);

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
    let mut sum = 0;
    for line in input.lines().filter(|line| !line.trim().is_empty()){
        let number: i64 = line.parse().unwrap();
        sum += number/3-2;
    }
    sum
}

fn part2(input: &str) -> i64 {
    let mut sum = 0;
    for line in input.lines().filter(|line| !line.trim().is_empty()){
        let number: i64 = line.parse().unwrap();
        let mut add = number/3-2;
        while add > 0 {
            sum += add;
            add = add/3-2;
        }
    }
    sum
}

