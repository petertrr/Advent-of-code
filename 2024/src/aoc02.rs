use std::fs;

pub fn aoc02(input_file: &String) {
    let result = fs::read_to_string(input_file);
    let data = match result {
        Err(e) => return println!("Couldn't read input from file {input_file}: {e}"),
        Ok(_data) => _data
    };
    let matrix = data.lines().map(|l| 
        l.split_whitespace().map(|w| 
            w.parse::<i32>().unwrap()).collect::<Vec<_>>())
            .collect::<Vec<_>>();
 
    let num_safes_1: i32 = matrix.iter().map(check_line)
        .map(|idx| if idx == -1 { 1 } else { 0 })
        .sum();

    let num_safes_2: i32 = matrix.iter().map(|line| {
        let mut idx = check_line(line);
        if idx != -1 {
            let mut original = line.clone();
            let bad_idx = idx.try_into().unwrap();
            original.remove(bad_idx);
            idx = check_line(&original);
            if idx != -1 {
                original = line.clone();
                original.remove(bad_idx+1);
                idx = check_line(&original);
                if idx != -1 {
                    return 0;
                }
            }
        }
        return 1;
}).sum();
    println!("Number of safe reports in 1st part: {num_safes_1}");
    println!("Number of safe reports in 2nd part: {num_safes_2}");
}

fn check(is_asc: bool, next: i32, cur: i32) -> bool {
    return (is_asc ^ (next < cur)) && 0 < (next - cur).abs() && (next - cur).abs() <= 3; 
}

fn check_line(line: &Vec<i32>) -> i32 {
    let mut is_asc = true;
    for (idx, num) in line.iter().enumerate() {
        if idx == 0 {
            is_asc = match line[idx+1].cmp(num) {
                std::cmp::Ordering::Greater => true,
                std::cmp::Ordering::Less => false,
                std::cmp::Ordering::Equal => return 0,
            };
            continue;
        } else if idx == line.len() - 1 {
            continue;
        }
        
        let cur = *num;
        let next = line[idx+1];
        if check(is_asc, next, cur) {
            continue;
        } else {
            // return 0;
            return idx.try_into().unwrap();
        }
    }
    return -1;
}