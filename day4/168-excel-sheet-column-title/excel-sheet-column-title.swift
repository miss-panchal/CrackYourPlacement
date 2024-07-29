class Solution {
	func convertToTitle(_ columnNumber: Int) -> String {
		let array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
		var result = ""
		var num = columnNumber

		while num > 0 {
			let remainder = num % 26
			if remainder > 0 {
				result.append(array[remainder - 1])
			} else {
				result.append("Z")
				num -= 26
			}
			num /= 26
		}
		return String(result.reversed())
	}
}