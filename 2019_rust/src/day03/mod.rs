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
    let mut points = input.lines().map(to_points);
    let a = points.next().unwrap();
    let b = points.next().unwrap();
    let mut distance = i64::MAX;
    for pair1 in a.windows(2) {
        let (x1, y1) = pair1[0];
        let (x2, y2) = pair1[1];
        for pair2 in b.windows(2) {
            let (x3, y3) = pair2[0];
            let (x4, y4) = pair2[1];
            if (x1 == x2)
                && (y3 == y4)
                && (x3.min(x4) <= x1 && x1 <= x3.max(x4))
                && (y1.min(y2) <= y3 && y3 <= y1.max(y2))
            {
                distance = std::cmp::min(distance, x1.abs() + y3.abs());
            }
            if (y1 == y2)
                && (x3 == x4)
                && (y3.min(y4) <= y1 && y1 <= y3.max(y4))
                && (x1.min(x2) <= x3 && x3 <= x1.max(x2))
            {
                distance = std::cmp::min(distance, y1.abs() + x3.abs());
            }
        }
    }
    distance
}

fn part2(input: &str) -> i64 {
    let mut points = input.lines().map(to_points_steps);
    let a = points.next().unwrap();
    let b = points.next().unwrap();
    let mut distance = i64::MAX;
    for pair1 in a.windows(2) {
        let (x1, y1, steps1) = pair1[0];
        let (x2, y2, _) = pair1[1];
        for pair2 in b.windows(2) {
            let (x3, y3, steps2) = pair2[0];
            let (x4, y4, _) = pair2[1];
            if (x1 == x2)
                && (y3 == y4)
                && (x3.min(x4) <= x1 && x1 <= x3.max(x4))
                && (y1.min(y2) <= y3 && y3 <= y1.max(y2))
            {
                distance = std::cmp::min(distance, steps1 + steps2 + x1.abs_diff(x3) as i64 + y1.abs_diff(y3) as i64);
            }
            if (y1 == y2)
                && (x3 == x4)
                && (y3.min(y4) <= y1 && y1 <= y3.max(y4))
                && (x1.min(x2) <= x3 && x3 <= x1.max(x2))
            {
                distance = std::cmp::min(distance, steps1 + steps2 + x1.abs_diff(x3) as i64 + y1.abs_diff(y3) as i64);
            }
        }
    }
    distance
}

fn to_points(input: &str) -> Vec<(i64, i64)> {
    let mut x = 0;
    let mut y = 0;
    let mut points = Vec::new();
    for inst in input.split(",") {
        let num: i64 = inst[1..].parse().unwrap();
        match inst.chars().next().unwrap() {
            'R' => x += num,
            'L' => x -= num,
            'D' => y -= num,
            'U' => y += num,
            _ => unreachable!(),
        }
        points.push((x, y));
    }
    points
}


fn to_points_steps(input: &str) -> Vec<(i64, i64, i64)> {
    let mut x = 0;
    let mut y = 0;
    let mut steps = 0;
    let mut points = Vec::new();
    for inst in input.split(",") {
        let num: i64 = inst[1..].parse().unwrap();
        steps += num;
        match inst.chars().next().unwrap() {
            'R' => x += num,
            'L' => x -= num,
            'D' => y -= num,
            'U' => y += num,
            _ => unreachable!(),
        }
        points.push((x, y, steps));
    }
    points
}
