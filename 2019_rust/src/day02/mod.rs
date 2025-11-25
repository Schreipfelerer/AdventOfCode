use crate::utils::read_input_file;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day02", input_file);

    match part.map(|s| s.as_str()) {
        Some("1") => println!("Part 1: {}", part1(&input, 12, 2)),
        Some("2") => println!("Part 2: {}", part2(&input)),
        _ => {
            // run both if no part specified
            println!("Part 1: {}", part1(&input, 12, 2));
            println!("Part 2: {}", part2(&input));
        }
    }
}

fn part1(input: &str, noun: i64, verb: i64) -> i64 {
    let mut numbs: Vec<i64> = input
        .trim()
        .split(",")
        .map(|x| x.parse::<i64>().unwrap())
        .collect();
    let mut pc = 0;

    numbs[1] = noun;
    numbs[2] = verb;

    loop {
        let opcode = numbs[pc];
        match opcode {
            1 | 2 => {
                let a = numbs[pc + 1] as usize;
                let b = numbs[pc + 2] as usize;
                let out = numbs[pc + 3] as usize;

                numbs[out] = if opcode == 1 {
                    numbs[a] + numbs[b]
                } else {
                    numbs[a] * numbs[b]
                };

                pc += 4;
            }
            99 => break,
            _ => unreachable!(),
        }
    }

    numbs[0]
}

fn part2(input: &str) -> i64 {
    for noun in 0..=99 {
        for verb in 0..=99 {
            if part1(input, noun, verb) == 19690720 {
                return 100 * noun + verb;
            }
        }
    }
    -1
}
