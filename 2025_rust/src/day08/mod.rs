use std::{collections::BinaryHeap, usize};

use crate::utils::read_input_file;

pub fn run(input_file: &str, part: Option<&String>) {
    let input = read_input_file("day08", input_file);

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
    let connections = 1000;
    let boxes: Vec<Vec<isize>> = input
        .lines()
        .map(|x| x.split(',').map(|y| y.parse().unwrap()).collect())
        .collect();
    let mut differences: BinaryHeap<(usize, &Vec<isize>, &Vec<isize>)> = BinaryHeap::new();
    for x1 in 0..boxes.len() {
        // Compute differences
        let box1 = &boxes[x1];
        for x2 in x1..boxes.len() {
            if x1 == x2 {
                continue;
            }
            let box2 = &boxes[x2];
            let difference = box1[0].abs_diff(box2[0]).pow(2)
                + box1[1].abs_diff(box2[1]).pow(2)
                + box1[2].abs_diff(box2[2]).pow(2);
            differences.push((difference, box1, box2));

            if differences.len() > connections {
                differences.pop();
            }
        }
    }

    let mut circuts: Vec<Vec<&Vec<isize>>> = boxes.iter().map(|x| vec![x]).collect();
    for (_, box1, box2) in differences.into_sorted_vec().iter() {
        // Merge connections
        for mut x1 in 0..circuts.len() {
            if circuts[x1].contains(box1) {
                for x2 in 0..circuts.len() {
                    if x1 == x2 {
                        continue;
                    }
                    if circuts[x2].contains(box2) {
                        let box2 = circuts.swap_remove(x2);
                        if x1 == circuts.len(){
                            x1 = x2;
                        }
                        circuts[x1].extend(box2);
                        break;
                    }
                }

                break;
            }
        }
    }

    let mut lengths: Vec<usize> = circuts.iter().map(|x| x.len()).collect();
    lengths.sort();
    lengths.iter().rev().take(3).product::<usize>() as i64
}

fn part2(input: &str) -> i64 {
    let boxes: Vec<Vec<isize>> = input
        .lines()
        .map(|x| x.split(',').map(|y| y.parse().unwrap()).collect())
        .collect();
    let mut differences: Vec<(usize, &Vec<isize>, &Vec<isize>)> = Vec::new();
    for x1 in 0..boxes.len() {
        // Compute differences
        let box1 = &boxes[x1];
        for x2 in x1..boxes.len() {
            if x1 == x2 {
                continue;
            }
            let box2 = &boxes[x2];
            let difference = box1[0].abs_diff(box2[0]).pow(2)
                + box1[1].abs_diff(box2[1]).pow(2)
                + box1[2].abs_diff(box2[2]).pow(2);
            differences.push((difference, box1, box2));
        }
    }

    differences.sort();

    let mut circuts: Vec<Vec<&Vec<isize>>> = boxes.iter().map(|x| vec![x]).collect();
    for (_, box1, box2) in differences.iter() {
        // Merge connections
        for mut x1 in 0..circuts.len() {
            if circuts[x1].contains(box1) {
                for x2 in 0..circuts.len() {
                    if x1 == x2 {
                        continue;
                    }
                    if circuts[x2].contains(box2) {
                        let box2 = circuts.swap_remove(x2);
                        if x1 == circuts.len(){
                            x1 = x2;
                        }
                        circuts[x1].extend(box2);
                        break;
                    }
                }

                break;
            }
        }

        if circuts.len() == 1 {
            return (box1[0]*box2[0]) as i64;
        }
    }
    0
}
