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
    let mut dial = 50;
    let mut zeros = 0;
    for line in input.lines(){
        let mult = if line.starts_with("L") {-1} else {1};
        let change: i64 = line[1..].parse().unwrap();
        dial += change * mult;
        dial %= 100;
        if dial == 0 {zeros += 1}
    }
    zeros
}

fn part2(input: &str) -> i64 {
    let mut dial = 50;
    let mut zeros = 0;
    for line in input.lines(){
        let mult = if line.starts_with("L") {-1} else {1};
        let change: i64 = line[1..].parse().unwrap();
        if dial == 0 && mult == -1 {zeros -= 1}
        dial += change * mult;
        if mult == 1 {
            zeros += dial/100;
        }
        else {
            zeros += (dial-100)/-100
        }
        dial = dial.rem_euclid(100);
    }
    zeros
}

