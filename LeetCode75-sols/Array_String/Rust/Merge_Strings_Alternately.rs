impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut result = String::new();
        let mut iter1 = word1.chars();
        let mut iter2 = word2.chars();

        loop {
            match (iter1.next(), iter2.next()) {
                (None, None) => break,
                (Some(c1), Some(c2)) => {
                    result.push(c1);
                    result.push(c2);
                },
                (Some(c1), None) => {
                    result.push(c1);
                },
                (None, Some(c2)) => {
                    result.push(c2);
                },
            }
        }
        result
    }
}
