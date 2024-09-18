impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        // Check if concatenation of str1+str2 = str2+str1
        if (str1.clone() + &str2 != str2.clone() + &str1) {
            return String::new();
        }

        let gcd_length = gcd(str1.len(), str2.len());

        // Return substring
        str1[..gcd_length].to_string()
    }
}

// Helper GCD function
fn gcd(a: usize, b: usize) -> usize {
    if (b == 0) {
        a
    } else {
        gcd (b, a % b)
    }
}
