/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    if (str1 + str2 !== str2 + str1) {
      return "";
    }
  // Compute GCD of lengths
  const gcdLength = gcd(str1.length, str2.length);

  // Return substring from 0 to gcdLength
  return str1.substring(0, gcdLength);
};

// Helper function fo rGCD
function gcd(a, b) {
  if (b == 0) {
    return a;
  }
  return gcd(b, a % b);
