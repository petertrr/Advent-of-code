use std::fs;
use regex::Regex;

pub fn aoc03(args: &Vec<String>) {
    let instr_re = Regex::new(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))").unwrap();
    let mul_re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();

    let input_file = &args[2];
    let input = fs::read_to_string(input_file).unwrap();

    let part1: usize = mul_re.captures_iter(&input).map(|c| c.extract()).map(|(_, [mul1, mul2])| {
        mul1.parse::<usize>().unwrap() * mul2.parse::<usize>().unwrap()
    }).sum();

    print!("Answer to the 1st part is {part1}");

    let mut mul_enabled = true;
    let part2: usize = instr_re.captures_iter(&input).map(|c| c.extract()).map(|(_, [instr_w_args])| {
        let instr = instr_w_args.split("(").next().unwrap();
        if instr == "do" {
            mul_enabled = true;
        } else if instr == "don't" {
            mul_enabled = false;
        } else if mul_enabled {
            return mul_re.captures_iter(&instr_w_args).map(|c| c.extract()).map(|(_, [mul1, mul2])| {
                mul1.parse::<usize>().unwrap() * mul2.parse::<usize>().unwrap()
            }).next().unwrap();
        }
        return 0;
    }).sum();

    print!("Answer to the 2nd part is {part2}");
}
