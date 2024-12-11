mod aoc02;
mod aoc03;

use std::env;

fn main() {
    let args = env::args().collect::<Vec<_>>();
    let day = &args[1];
    let input_file = &args[2];
    match day.as_ref() {
        "02" => aoc02::aoc02(input_file),
        "03" => aoc03::aoc03(&args),
        &_ => panic!()
    }
}
