mod utils;
mod day01;
mod day02;

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
        _ => eprintln!("Unknown day '{day}'"),
    }
}
