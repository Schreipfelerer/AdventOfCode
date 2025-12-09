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
    let lines: Vec<Vec<char>> = input.lines().map(|x| x.chars().collect()).collect();
    let mut movable = 0;

    for y in 0..lines.len() {
        for x in 0..lines[y].len() {
            if lines[y][x] != '@' {
                continue;
            }

            let mut nearby = 0;
            for y_offset in -1..=1 {
                for x_offset in -1..=1 {
                    if y_offset == 0 && x_offset == 0 {
                        continue;
                    }
                    let nx = x as isize + x_offset;
                    let ny = y as isize + y_offset;
                    if ny == -1 || ny == lines.len() as isize {
                        continue;
                    }
                    if nx == -1 || nx == lines[ny as usize].len() as isize {
                        continue;
                    }
                    if lines[ny as usize][nx as usize] == '@' {
                        nearby += 1
                    }
                }
            }
            if nearby < 4 {
                movable += 1
            }
        }
    }

    movable
}

fn part2(input: &str) -> i64 {
    let mut lines: Vec<Vec<char>> = input.lines().map(|x| x.chars().collect()).collect();
    let mut movable = 0;

    let mut is_changed = true;
    while is_changed {
        is_changed = false;
        for y in 0..lines.len() {
            for x in 0..lines[y].len() {
                if lines[y][x] != '@' {
                    continue;
                }

                let mut nearby = 0;
                for y_offset in -1..=1 {
                    for x_offset in -1..=1 {
                        if y_offset == 0 && x_offset == 0 {
                            continue;
                        }
                        let nx = x as isize + x_offset;
                        let ny = y as isize + y_offset;
                        if ny == -1 || ny == lines.len() as isize {
                            continue;
                        }
                        if nx == -1 || nx == lines[ny as usize].len() as isize {
                            continue;
                        }
                        if lines[ny as usize][nx as usize] == '@' {
                            nearby += 1
                        }
                    }
                }
                if nearby < 4 {
                    movable += 1;
                    lines[y][x] = '.';
                    is_changed = true;
                }
            }
        }
    }

    movable
}
