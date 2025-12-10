use itertools::{Itertools};

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
        let mut current_states: Vec<(Vec<i64>, i64)> = vec![(vec![0; wanted_state.len()], 0)];
        let mut next_states: Vec<(Vec<i64>, i64)> = vec![];
        for counter in 0..wanted_state.len() {
            let relevenat_options = options
                .iter()
                .filter(|o| o.iter().any(|i| *i == counter) && o.iter().all(|i| *i >= counter))
                .collect_vec();
            for (state, p) in &current_states {
                let diff = wanted_state[counter] - state[counter];
                if diff == 0 {
                    next_states.push((state.clone(), *p));
                    continue;
                }
                if relevenat_options.is_empty() {
                    continue;
                }

                for presses in press_possible(
                    diff, 
                    relevenat_options
                        .iter()
                        .map(|o| o.iter().map(|d| wanted_state[*d] - state[*d]).min().unwrap()),
                ) {
                    let mut n_state = state.clone();
                    for (i, pn) in presses.iter().enumerate(){
                        for d in relevenat_options[i]{
                            n_state[*d] += pn;
                        }
                    }
                    if (0..n_state.len()).all(|d| n_state[d] <= wanted_state[d]){
                        next_states.push((n_state, *p+diff));
                    }
                }
            }
            current_states = next_states;
            next_states = vec![];
            println!("advance!");
        }
        total_presses += current_states.iter().min_by_key(|(_, x)| x).unwrap().1;
        println!("solved");
    }
    total_presses
}



fn press_possible<I>(presses: i64, max_presses_iter: I) -> Vec<Vec<i64>>
where
    I: IntoIterator<Item = i64>,
{
    // Collect incoming iterator ONCE to a Vec<i64>
    let max_presses: Vec<i64> = max_presses_iter.into_iter().collect();

    // Too large to fit
    if presses > max_presses.iter().sum() {
        return vec![];
    }

    // Nothing to distribute
    if presses == 0 {
        return vec![vec![0; max_presses.len()]];
    }

    // Last slot only
    if max_presses.len() == 1 {
        return vec![vec![presses]];
    }

    let last_max = max_presses[max_presses.len() - 1];

    let mut result = Vec::new();

    for p in 0..=presses.min(last_max) {
        let sub = press_possible(
            presses - p,
            max_presses[..max_presses.len() - 1].iter().copied(),
        );

        for mut v in sub {
            v.push(p);
            result.push(v);
        }
    }

    result
}

