mod utils;
mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod day06;
mod day07;
mod day08;
mod day09;
mod day10;
mod day11;
mod day12;
mod day13;
mod day14;
mod day15;
mod day16;
mod day17;
mod day18;
mod day19;
mod day20;
mod day21;
mod day22;
mod day23;
mod day24;
mod day25;

fn main() {
    let args: Vec<String> = std::env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: cargo run -- <day> [input_file] [part]");
        eprintln!("Example: cargo run -- 1 example.txt 1");
        return;
    }

    let day = &args[1];
    let input_file = args.get(2).map(|s| s.as_str()).unwrap_or("input.txt");
    let part = args.get(3); // optional

    match day.as_str() {
        "1" | "01" => day01::run(input_file, part),
        "2" | "02" => day02::run(input_file, part),
        "3" | "03" => day03::run(input_file, part),
        "4" | "04" => day04::run(input_file, part),
        "5" | "05" => day05::run(input_file, part),
        "6" | "06" => day06::run(input_file, part),
        "7" | "07" => day07::run(input_file, part),
        "8" | "08" => day08::run(input_file, part),
        "9" | "09" => day09::run(input_file, part),
        "10" => day10::run(input_file, part),
        "11" => day11::run(input_file, part),
        "12" => day12::run(input_file, part),
        "13" => day13::run(input_file, part),
        "14" => day14::run(input_file, part),
        "15" => day15::run(input_file, part),
        "16" => day16::run(input_file, part),
        "17" => day17::run(input_file, part),
        "18" => day18::run(input_file, part),
        "19" => day19::run(input_file, part),
        "20" => day20::run(input_file, part),
        "21" => day21::run(input_file, part),
        "22" => day22::run(input_file, part),
        "23" => day23::run(input_file, part),
        "24" => day24::run(input_file, part),
        "25" => day25::run(input_file, part),
        _ => eprintln!("Unknown day '{day}'"),
    }
}
