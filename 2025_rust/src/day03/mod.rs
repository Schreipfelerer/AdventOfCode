use crate::utils::read_input_file;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day03", input_file);

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
    let mut joltage = 0;
    for line in input.lines(){
        let max1 = line[..line.len()-1].chars().max().unwrap();
        let max2 = line[line.find(max1).unwrap()+1..].chars().max().unwrap();
        joltage += format!("{}{}", max1, max2).parse::<i64>().unwrap()
    }
    joltage
}

fn part2(input: &str) -> i64 {
    let mut joltage = 0;
    for line in input.lines(){
        let mut startindex = 0;
        let mut numbers = String::new();
        for num in (0..12).rev() {
            let max = line[startindex..line.len()-num].chars().max().unwrap();
            startindex += 1+line[startindex..].find(max).unwrap();
            numbers.push(max);
        }
        joltage += numbers.parse::<i64>().unwrap();
    }
    joltage
}

