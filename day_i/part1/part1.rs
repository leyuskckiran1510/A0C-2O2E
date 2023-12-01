use std::fs;

  fn main() {
    let binding =
        fs::read_to_string("input.txt").expect("File Couldnot be oned");
    let content = binding.split("\n");
    let mut answer = 0;
    for
      pat in content {
        let mut temp : Vec < i32 >= vec ![];
        for
          c in pat.chars() {
            if c
              >= '0' && c <= '9' { temp.push(c as i32 - '0' as i32); }
        }
        let poped = temp.pop();
        if temp.len() > 0 { answer += temp[0] * 10 + poped.unwrap() }
        else {
          if poped.is_some() { answer += poped.unwrap() * 10 + poped.unwrap(); }
        }
      }
    print !("The answer is [{:?}]\n", answer);
  }