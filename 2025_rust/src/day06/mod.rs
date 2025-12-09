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
    let mut problems: Vec<Vec<&str>> = input
        .lines()
        .map(|x| x.split_whitespace().collect())
        .collect();
    let operants = problems.pop().unwrap();
    let mut grand_total = 0;
    for problem in 0..operants.len() {
        let reduction = if operants[problem] == "+" {
            i64::strict_add
        } else {
            i64::strict_mul
        };

        grand_total += problems
            .iter()
            .map(|x| x[problem].parse().unwrap())
            .reduce(reduction)
            .unwrap();
    }
    grand_total
}

fn part2(input: &str) -> i64 {
    let mut total = 0;
    let mut lines: Vec<Vec<char>> = input.lines().map(|x| x.chars().collect()).collect();
    let operants = lines.pop().unwrap();
    let mut numbers: Vec<i64> = Vec::new();
    for index in (0..lines[0].len()).rev() {
        let top_down_number: String = lines.iter().map(|x| x[index]).collect();
        let trimmed = top_down_number.trim();
        if trimmed.is_empty() {
            numbers = Vec::new();
            continue;
        }
        numbers.push(trimmed.parse().unwrap());
        if operants[index] != ' ' {
            let operant = if operants[index] == '+' {
                i64::strict_add
            } else {
                i64::strict_mul
            };
            total += numbers.iter().copied().reduce(operant).unwrap();
        }
    }
    total
}
