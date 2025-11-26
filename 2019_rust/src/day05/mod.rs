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
    let mut numbs: Vec<i64> = input
        .trim()
        .split(",")
        .map(|x| x.parse::<i64>().unwrap())
        .collect();
    let mut pc = 0;
    let input_data = 1;
    let mut output_data = -1;

    loop {
        let opcode = numbs[pc];
        let pos1 = opcode / 100 % 10;
        let pos2 = opcode / 1000 % 10;
        match opcode % 100 {
            1 | 2 => {
                let a = numbs[pc + 1];
                let num_a = if pos1 == 1 { a } else { numbs[a as usize] };
                let b = numbs[pc + 2];
                let num_b = if pos2 == 1 { b } else { numbs[b as usize] };
                let out = numbs[pc + 3] as usize;

                numbs[out] = if opcode % 100 == 1 {
                    num_a + num_b
                } else {
                    num_a * num_b
                };

                pc += 4;
            }
            3 | 4 => {
                let a = numbs[pc + 1];
                let num_a = if pos1 == 1 { a } else { numbs[a as usize] };
                if opcode % 100 == 3 {
                    numbs[a as usize] = input_data;
                } else {
                    output_data = num_a;
                }
                pc += 2;
            }
            99 => break,
            _ => unreachable!(),
        }
    }

    output_data
}

fn part2(input: &str) -> i64 {
    let mut numbs: Vec<i64> = input
        .trim()
        .split(",")
        .map(|x| x.parse::<i64>().unwrap())
        .collect();
    let mut pc = 0;
    let input_data = 5;
    let mut output_data = -1;

    loop {
        let opcode = numbs[pc];
        let pos1 = opcode / 100 % 10;
        let pos2 = opcode / 1000 % 10;
        match opcode % 100 {
            1 | 2 => {
                let a = numbs[pc + 1];
                let num_a = if pos1 == 1 { a } else { numbs[a as usize] };
                let b = numbs[pc + 2];
                let num_b = if pos2 == 1 { b } else { numbs[b as usize] };
                let out = numbs[pc + 3] as usize;

                numbs[out] = if opcode % 100 == 1 {
                    num_a + num_b
                } else {
                    num_a * num_b
                };

                pc += 4;
            }
            3 | 4 => {
                let a = numbs[pc + 1];
                let num_a = if pos1 == 1 { a } else { numbs[a as usize] };
                if opcode % 100 == 3 {
                    numbs[a as usize] = input_data;
                } else {
                    output_data = num_a;
                }
                pc += 2;
            }
            5 | 6 => {
                let a = numbs[pc + 1];
                let num_a = if pos1 == 1 { a } else { numbs[a as usize] };
                let b = numbs[pc + 2];
                let num_b = if pos2 == 1 { b } else { numbs[b as usize] };
                pc += 3;
                if (opcode % 100 == 5) == (num_a != 0) {
                    pc = num_b as usize;
                }
            }
            7 | 8 => {
                let a = numbs[pc + 1];
                let num_a = if pos1 == 1 { a } else { numbs[a as usize] };
                let b = numbs[pc + 2];
                let num_b = if pos2 == 1 { b } else { numbs[b as usize] };
                let out = numbs[pc + 3] as usize;

                numbs[out] = if opcode % 100 == 7 && num_a < num_b || opcode % 100 == 8 && num_a == num_b {
                    1
                } else {
                    0
                };
                pc += 4;
            }
            99 => break,
            _ => unreachable!(),
        }
    }

    output_data
}
