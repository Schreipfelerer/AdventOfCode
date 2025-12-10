use z3::{ast::Int, Config, Context, Optimize, Solver};
use crate::utils::read_input_file;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day10", input_file);

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
    let mut total_presses = 0;
    for (wanted, presses) in input.lines().map(|x| x.split_once("] (").unwrap()) {
        let wanted_state = wanted.chars().skip(1).map(|f| f == '#').collect_vec();
        let options = presses
            .split_once(") {")
            .unwrap()
            .0
            .split(") (")
            .map(|d| {
                d.split(',')
                    .map(|f| f.parse::<usize>().unwrap())
                    .collect_vec()
            })
            .collect_vec();
        let mut current_state = vec![false; wanted_state.len()];

        total_presses += try_presses(&mut current_state, &wanted_state, &options, 0);
    }
    total_presses
}

fn press(state: &mut Vec<bool>, locations: &Vec<usize>) {
    for location in locations {
        state[*location] = !state[*location]
    }
}

fn try_presses(
    state: &mut Vec<bool>,
    wanted_state: &Vec<bool>,
    options: &Vec<Vec<usize>>,
    from_index: usize,
) -> i64 {
    if *state == *wanted_state {
        return 0;
    }
    let mut smallest = i64::MAX;
    for i in from_index..options.len() {
        press(state, &options[i]);
        smallest = smallest.min(try_presses(state, wanted_state, options, i + 1));
        press(state, &options[i]);
    }
    smallest.saturating_add(1)
}

fn part2(input: &str) -> i64 {
    let mut total_presses: i64 = 0;
    for (options_raw, requirements_raw) in input
        .lines()
        .map(|x| x.split_once("] (").unwrap().1.split_once(") {").unwrap())
    {
        let options = options_raw
            .split(") (")
            .map(|d| {
                d.split(',')
                    .map(|f| f.parse::<usize>().unwrap())
                    .collect_vec()
            })
            .collect_vec();
        let wanted_state = requirements_raw
            .trim_end_matches('}')
            .split(',')
            .map(|f| f.parse::<i64>().unwrap())
            .collect_vec();

        let opt = Optimize::new();

    }

    total_presses
}

