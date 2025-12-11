use crate::utils::read_input_file;
use std::collections::HashMap;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day11", input_file);

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
    let mut paths: HashMap<&str, Vec<&str>> = HashMap::new();
    for (label, outs) in input.lines().map(|l| l.split_once(": ").unwrap()) {
        paths.insert(label, outs.split(" ").collect());
    }
    number_of_paths("you", "out", paths)
}

fn number_of_paths(from: &str, to: &str, paths: HashMap<&str, Vec<&str>>) -> i64 {
    //First Prune from back
    let mut reachable: Vec<&str> = vec![];
    let mut reached = vec![to];
    while !reached.is_empty() {
        let node = reached.pop().unwrap();
        reachable.push(node);
        for prev_node in paths.iter().filter(|(_, v)| v.contains(&node)).map(|(k, _)| k){
            if !reachable.contains(prev_node) && !reached.contains(prev_node) {
                reached.push(prev_node);
            }
        }
    }
    // Calculate how many paths to exit there are
    let mut costs: HashMap<&str, i64> = HashMap::new();
    costs.insert(to, 1);

    let mut changed = true;
    while changed {
        changed = false;
        for k in paths.keys().cloned() {
            if !reachable.contains(&k) || costs.contains_key(&k) {
                continue;
            }
            if paths
                .get(&k)
                .unwrap()
                .iter()
                .all(|n| costs.contains_key(n) || !reachable.contains(n))
            {
                changed = true;
                let cost = paths
                    .get(k)
                    .unwrap()
                    .iter()
                    .filter(|f| reachable.contains(f))
                    .map(|f| costs.get(f).unwrap())
                    .sum::<i64>();
                costs.insert(k, cost);
            }
        }
    }

    *costs.entry(from).or_default()
}

fn part2(input: &str) -> i64 {
    let mut paths: HashMap<&str, Vec<&str>> = HashMap::new();
    for (label, outs) in input.lines().map(|l| l.split_once(": ").unwrap()) {
        paths.insert(label, outs.split(" ").collect());
    }
     
    let srv_dac = number_of_paths("svr", "dac", paths.clone());
    let dac_fft = number_of_paths("dac", "fft", paths.clone());
    let fft_out = number_of_paths("fft", "out", paths.clone());
    let srv_fft = number_of_paths("svr", "fft", paths.clone());
    let fft_dac = number_of_paths("fft", "dac", paths.clone());
    let dac_out = number_of_paths("dac", "out", paths.clone());

    //println!("src-dac-fft-out: {} * {} * {}", srv_dac, dac_fft, fft_out);
    //println!("src-fft-dac-out: {} * {} * {}", srv_fft, fft_dac, dac_out);

    srv_dac * dac_fft * fft_out + srv_fft * fft_dac * dac_out
}
