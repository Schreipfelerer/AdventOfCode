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
        _ => eprintln!("Unknown day '{day}'"),
    }
}
