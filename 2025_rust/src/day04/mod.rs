use crate::utils::read_input_file;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day04", input_file);

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
    let range: Vec<i64> = input.trim().split("-").map(|x| x.parse().unwrap()).collect();
    let from = range[0];
    let to = range[1];
    let mut num = 0;
    for i in from..=to {
        let digits : Vec<char> = i.to_string().chars().collect();
        if digits.is_sorted() && digits.windows(2).any(|w| w[0] == w[1]){
            num += 1
        }
    }

    num
}

fn part2(input: &str) -> i64 {
    let range: Vec<i64> = input.trim().split("-").map(|x| x.parse().unwrap()).collect();
    let from = range[0];
    let to = range[1];
    let mut num = 0;
    for i in from..=to {
        let mut digits : Vec<char> = i.to_string().chars().collect();
        digits.push('x');
        digits.insert(0, '0');
        if digits.is_sorted() && digits.windows(4).any(|w| w[0] != w[1] && w[1] == w[2] && w[2] != w[3]){
            num += 1
        }
    }

    num
}
