# LeetCode-Style Interview Questions (Python)

---

## A) Evaluate Division

**Difficulty:** Medium

**Topics:** Graph, Depth-First Search (DFS), Breadth-First Search (BFS), Union-Find, Hash Map

---

### Problem Description

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation $A_i / B_i = \text{values}[i]$. Each $A_i$ or $B_i$ is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the $j$-th query where you must find the answer for $C_j / D_j = ?$.

Return the answers to all queries. If a single answer cannot be determined, return $-1.0$.

**Note:** The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction. Variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

### Examples

**Example 1:**

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

**Example 2:**

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

**Example 3:**

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

### Constraints

- `1 <= equations.length <= 100`
- `equations[i].length == 2`
- `1 <= Ai.length, Bi.length <= 5`
- `values.length == equations.length`
- $0.0 < \text{values}[i] \le 20.0$
- `1 <= queries.length <= 100`
- `queries[j].length == 2`
- `1 <= Cj.length, Dj.length <= 5`
- `Ai, Bi, Cj, Dj` consist of lowercase English letters and digits.

---

## B) Minimum Penalty for Shop Closure

**Difficulty:** Medium

**Topics:** String, Prefix Sum, Array

---

### Problem Description

You are given the customer visit log of a shop, represented by a 0-indexed string `customers` consisting only of characters `'N'` and `'Y'`:

- If the $i$-th character is `'Y'`, it means that customers came at the $i$-th hour.
- If `'N'`, it indicates that no customers came at the $i$-th hour.

If the shop closes at the $j$-th hour ($0 \le j \le n$, where $n$ is the total number of hours/length of the `customers` string), the penalty is calculated as follows:

- For every hour when the shop is open and no customers come, the penalty increases by 1.
- For every hour when the shop is closed and customers come, the penalty increases by 1.

Return the earliest hour at which the shop must be closed to incur a minimum penalty.

**Note:** If a shop closes at the $j$-th hour, it means the shop is closed from the hour $j$.

### Examples

**Example 1:**

Input: customers = "YYNY"
Output: 2

Explanation:

    Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.

    Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.

    Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.

    Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.

    Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
    Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

**Example 2:**

Input: customers = "NNNNN"
Output: 0

Explanation: It is best to close the shop at the 0th hour as no customers arrive.

**Example 3:**

Input: customers = "YYYY"
Output: 4

Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.

### Constraints

- `1 <= customers.length <= 10^5`
- `customers` consists only of characters `'Y'` and `'N'`.

---

## C) Cheapest Flights Within K Stops

**Difficulty:** Medium

**Topics:** Graph, Dynamic Programming, Breadth-First Search (BFS), Dijkstra's Algorithm, Bellman-Ford

---

### Problem Description

There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [fromi, toi, pricei]` indicates that there is a flight from city `fromi` to city `toi` with cost `pricei`.

You are also given three integers `src`, `dst`, and `k`. Return the cheapest price from `src` to `dst` with **at most $k$ stops**. If there is no such route, return `-1`.

### Examples

**Example 1:**

Input:
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

Output:
700

Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

**Example 2:**

Input:
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

Output:
200

Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

**Example 3:**

Input:
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0

Output:
500

Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

### Constraints

- `1 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= fromi, toi < n`
- `fromi != toi`
- `1 <= pricei <= 10^4`
- There will not be any multiple flights between two cities.
- `0 <= src, dst, k < n`
- `src != dst`

---

## D) Brace Expansion

**Difficulty:** Medium

**Topics:** String, Backtracking, Recursion, Permutations

---

### Problem Description

A string `S` represents a list of words. Each letter in the word has one or more options. If there's one option, the letter is represented as is. If there's more than one option, then curly braces delimit the options. For example, `"{a,b,c}"` represents options `["a", "b", "c"]`.

For example, `"{a,b,c}d{e,f}"` represents the list `["ade", "adf", "bde", "bdf", "cde", "cdf"]`.

Return all words that can be formed in this manner, in lexicographical order.

### Examples

**Example 1:**

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]

**Example 2:**

Input: "abcd"
Output: ["abcd"]

### Constraints

- `1 <= S.length <= 50`
- There are no nested curly brackets.
- All characters inside a pair of consecutive opening and ending curly brackets are different.

---

## E) Custom String Sorting

**Difficulty:** Medium

**Topics:** Array, String, Sorting, Custom Comparator

---

### Problem Description

You are given an array of strings `arr`, where each string is in the format `<letters><number>`:

- `<letters>` consists of one or more lowercase English letters (`'a'` to `'z'`).
- `<number>` consists of one or more digits (`'0'` to `'9'`).

The `<letters>` and `<number>` parts are not separated by a delimiter (e.g., `"abc123"`, `"z2"`, `"aa999"`).

Your task is to sort the array with the following rules:

1. First, sort the strings by the **alphabetical order of the letter part**.
2. If two strings have the same letters, sort them by the **numeric part in descending order** (i.e., higher numbers come first).

Return the sorted list of strings.

### Examples

**Example 1:**

Input: arr = ["a3", "a22", "b1", "b11", "a5"]
Output: ["a22", "a5", "a3", "b11", "b1"]

Explanation:

    Group "a": ["a3", "a22", "a5"] → sort by number descending → ["a22", "a5", "a3"]

    Group "b": ["b1", "b11"] → ["b11", "b1"]

**Example 2:**

Input: arr = ["cat20", "dog5", "cat3", "apple100", "apple11"]
Output: ["apple100", "apple11", "cat20", "cat3", "dog5"]

**Example 3:**

Input: arr = ["z9", "z10", "y1"]
Output: ["y1", "z10", "z9"]

### Constraints

- `1 <= arr.length <= 10^4`
- Each string in `arr` contains:
  - 1 to 20 lowercase letters followed by
  - 1 to 10 digits
- It is guaranteed that the format `<letters><number>` is valid for every string.

---

## F) Text Justification

**Difficulty:** Hard

**Topics:** Array, String

---

### Problem Description

Given an array of `words` and a maximum width `maxWidth`, format the text such that each line has exactly `maxWidth` characters.

Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters. Distribute the extra spaces between words as evenly as possible. If the number of spaces on a line does not divide evenly between words, the excess spaces should be placed on the left-hand side of the line. The last line of text should be left-justified, and no extra space is inserted between words.

**Note:**

- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is greater than 0 and will not exceed `maxWidth`.
- The input array `words` contains at least one word.

### Examples

**Example 1:**

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
"This is an",
"example of text",
"justification. "
]

**Example 2:**

Input: words = ["What","must","be","acknowledgment","shall","be","full","and","final","reparation."], maxWidth = 16
Output:
[
"What must be",
"acknowledgment ",
"shall be full ",
"and final ",
"reparation. "
]

**Example 3:**

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do."], maxWidth = 20
Output:
[
"Science is what we",
"understand well",
"enough to explain to",
"a computer. Art is",
"everything else we",
"do. "
]

### Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- `words[i]` consists of only lowercase and uppercase English letters.
- `1 <= maxWidth <= 100`

---

## G) Stopwords Stripper

**Difficulty:** Easy

**Topics:** String, Array, Hash Set

---

### Problem Description

Given a string `text` and a list of `stopwords`, create a function that returns a new string where all occurrences of the stop words from the input text have been removed. The returned string should be entirely in lowercase.

**Note:**

- Stop words are case-insensitive. For example, if `"the"` is a stop word, then `"The"`, `"THE"`, and `"tHe"` should all be removed.
- The order of words in the original text should be preserved for the words that are not stop words.
- Punctuation marks (e.g., `'.'`, `','`, `'!'`, `'?'`) should be treated as part of the words they are attached to, unless they are explicitly in the stopwords list.
- Multiple spaces between words should be reduced to a single space in the output. Leading or trailing spaces should be removed.

### Examples

**Example 1:**

Input:
text = "This is an example sentence with some common words."
stopwords = ["is", "an", "some"]
Output: "this example sentence with common words."

**Example 2:**

Input:
text = "The quick brown fox jumps over the lazy dog."
stopwords = ["the", "over"]
Output: "quick brown fox jumps lazy dog."

**Example 3:**

Input:
text = "Hello, world! How are you?"
stopwords = ["how", "are", "you"]
Output: "hello, world! ."

### Constraints

- `1 <= text.length <= 1000`
- `0 <= stopwords.length <= 100`
- Each word in `stopwords` consists of lowercase English letters.
- `text` consists of English letters, spaces, and common punctuation.

---

## H) Optimal Store Closing Times

**Difficulty:** Medium

**Topics:** String, Array, Simulation, Dynamic Programming (Implicit)

---

### Problem Description

You are tasked with optimizing the closing times for a chain of stores based on their hourly customer traffic logs. For each hour, the log indicates whether a customer visited (`'Y'`) or did not visit (`'N'`). The goal is to minimize a "penalty" score associated with the store's closing time.

The penalty is calculated as follows:

- `+1` penalty if a customer does not come (`'N'`) during an hour when the store is open.
- `+1` penalty if a customer comes (`'Y'`) during an hour when the store is closed.

The store's closing time is an integer representing the hour at which the store closes. If a store closes at hour $H$, it means the store is open during hours $0, 1, \dots, H-1$ and closed during hours $H, H+1, \dots$ until the end of the log. A closing time of $0$ means the store is never open. A closing time equal to the number of hours in the log means the store is always open.

You will implement three functions to address this problem.

---

### Part 1: `computePenalty`

Given a customer log string and a specific `closingTime`, calculate the total penalty. The log string will consist of space-separated `'Y'` and `'N'` characters (e.g., `"Y Y N Y"`).

#### Examples

**Example 1:**

Input: log = "Y Y N Y", closingTime = 2
Output: 1

Explanation:
Log hours: 0, 1, 2, 3 -> ['Y', 'Y', 'N', 'Y']
Shop open (0, 1):
Hour 0: 'Y' (No penalty)
Hour 1: 'Y' (No penalty)
Shop closed (2, 3):
Hour 2: 'N' (No penalty)
Hour 3: 'Y' (+1 penalty for 'Y' when closed)
Total Penalty: 1

**Example 2:**

Input: log = "N Y N", closingTime = 0
Output: 1

Explanation:
Log hours: 0, 1, 2 -> ['N', 'Y', 'N']
Shop open (none): []
Shop closed (0, 1, 2):
Hour 0: 'N' (No penalty)
Hour 1: 'Y' (+1 penalty for 'Y' when closed)
Hour 2: 'N' (No penalty)
Total Penalty: 1

---

### Part 2: `getClosingWithMinPenalty`

Given a customer log string for a single store, find the `closingTime` (0-indexed hour) that results in the minimum possible penalty. If multiple closing times yield the same minimum penalty, return the **smallest** `closingTime`. You should utilize the `computePenalty` function from Part 1.

#### Examples

**Example 1:**

Input: log = "Y Y N Y"
Output: 2

Explanation:
Let's compute penalties for all possible closing times:

    closingTime = 0: computePenalty("Y Y N Y", 0)
    Open: []
    Closed: [Y, Y, N, Y] -> Penalties: Y(+1), Y(+1), N(0), Y(+1) = 3

    closingTime = 1: computePenalty("Y Y N Y", 1)
    Open: [Y] -> Penalties: Y(0)
    Closed: [Y, N, Y] -> Penalties: Y(+1), N(0), Y(+1) = 2

    closingTime = 2: computePenalty("Y Y N Y", 2)
    Open: [Y, Y] -> Penalties: Y(0), Y(0)
    Closed: [N, Y] -> Penalties: N(0), Y(+1) = 1

    closingTime = 3: computePenalty("Y Y N Y", 3)
    Open: [Y, Y, N] -> Penalties: Y(0), Y(0), N(+1) = 1
    Closed: [Y] -> Penalties: Y(+1) = 1

    closingTime = 4: computePenalty("Y Y N Y", 4)
    Open: [Y, Y, N, Y] -> Penalties: Y(0), Y(0), N(+1), Y(0) = 1
    Closed: []
    Minimum penalty is 1, achieved at closingTime = 2, 3, and 4. The smallest among these is 2.
    Return: 2

**Example 2:**

Input: log = "N N N"
Output: 0

Explanation:

    closingTime = 0: Penalty = 0

    closingTime = 1: Open: N, Closed: [N, N] = 1

    closingTime = 2: Open: N, N, Closed: [N] = 2

    closingTime = 3: Open: N, N, N, Closed: [] = 3
    Return: 0

---

### Part 3: `getAllClosingTimes`

You will now process a log string that contains customer data for multiple stores. The log uses `"BEGIN"` to mark the start of a new store's log and `"END"` to mark its end. Your task is to extract each individual store's log and then use the `getClosingWithMinPenalty` function from Part 2 to find the optimal closing time for each store. Return a `List` of these optimal closing times in the order they appear in the input string.

**Note:** A store's log segment within `"BEGIN"` and `"END"` will only contain `'Y'` or `'N'` characters (space-separated). `"BEGIN"` and `"END"` are not part of the customer log for penalty calculation.

#### Examples

**Example 1:**

Input: log = "BEGIN BEGIN BEGIN Y Y N Y END Y Y N N END Y N Y N END"
Output: [2, 2, 1]

Explanation:

    First Store: Log segment after first "BEGIN" up to first "END": "Y Y N Y"
    getClosingWithMinPenalty("Y Y N Y") returns 2.

    Second Store: Log segment after second "BEGIN" up to second "END": "Y Y N N"
    Let's calculate:

        closingTime = 0: Closed: [Y,Y,N,N] -> Y(+1),Y(+1),N(0),N(0) = 2

        closingTime = 1: Open: [Y], Closed: [Y,N,N] -> Y(+1),N(0),N(0) = 1

        closingTime = 2: Open: [Y,Y], Closed: [N,N] -> N(0),N(0) = 0

        closingTime = 3: Open: [Y,Y,N], Closed: [N] -> N(+1) = 1

        closingTime = 4: Open: [Y,Y,N,N], Closed: [] -> N(+1) = 1
        getClosingWithMinPenalty("Y Y N N") returns 2.

    Third Store: Log segment after third "BEGIN" up to third "END": "Y N Y N"
    Let's calculate:

        closingTime = 0: Closed: [Y,N,Y,N] -> Y(+1),N(0),Y(+1),N(0) = 2

        closingTime = 1: Open: [Y], Closed: [N,Y,N] -> N(0),Y(+1),N(0) = 1

        closingTime = 2: Open: [Y,N], Closed: [Y,N] -> N(+1),Y(+1) = 2

        closingTime = 3: Open: [Y,N,Y], Closed: [N] -> N(+1) = 1

        closingTime = 4: Open: [Y,N,Y,N], Closed: [] -> N(+1),N(+1) = 2
        getClosingWithMinPenalty("Y N Y N") returns 1.
        Return: [2, 2, 1]

**Example 2:**

Input: log = "BEGIN N N N END BEGIN Y Y Y END"
Output: [0, 3]

Explanation:

    First Store: "N N N" -> getClosingWithMinPenalty("N N N") returns 0.

    Second Store: "Y Y Y" -> getClosingWithMinPenalty("Y Y Y") returns 3.
    Final Output: [0, 3]

### Constraints (for all parts of Optimal Store Closing Times)

- The input `log` strings for `computePenalty` and `getClosingWithMinPenalty` will consist of space-separated 'Y' and 'N' characters.
- The length of a single store's log (number of hours) will be between 1 and 50.
- The `closingTime` for `computePenalty` will be between 0 and `log.split(" ")`.length.
- For `getAllClosingTimes`, the combined length of the entire input string can be up to 5000 characters.
- The string `"BEGIN"` and `"END"` will always be correctly matched and will not be nested.
- There will be at least one store log segment.
- Characters in the log will only be 'Y', 'N', ' ', 'B', 'E', 'G', 'I', 'N', 'D'.

---

## I) Custom String Compression

**Difficulty:** Medium

**Topics:** String, Parsing, Custom Logic

---

### Problem Description

You are tasked with implementing a custom string compression algorithm that operates in two distinct phases. The input string represents a hierarchical path, similar to a URL or file path, where **major parts** are separated by a forward slash `/` and **minor parts** within a major part are separated by dots `.`.

The compression involves two phases, both relying on a core **Atomic Compression Rule**: If a string segment $S$ has a length $L > 2$, it is compressed to its first character, followed by the integer $(L - 2)$, followed by its last character. (e.g., `"customer"` $\rightarrow$ `"c6r"`, `"payments"` $\rightarrow$ `"p6s"`, `"com"` $\rightarrow$ `"c1m"`). If $L \le 2$, the segment remains unchanged.

The two compression phases are as follows:

---

#### Phase 1: Individual Segment Compression

In this phase, the **Atomic Compression Rule** is applied to every segment identified in the input string.

1. First, the entire input string is split into major parts using `/` as a delimiter.
2. Then, each major part is further split into minor parts using `.` as a delimiter.
3. The Atomic Compression Rule is applied to every resulting minor part.
4. The compressed minor parts are then re-joined with `.` to form compressed major parts.
5. Finally, the compressed major parts are re-joined with `/` to form the Phase 1 compressed string.

**Example of Phase 1:** `str = "stripe.com/payments/checkout/customer.john.doe"`

- **Major parts:** `"stripe.com"`, `"payments"`, `"checkout"`, `"customer.john.doe"`
- **Applying Atomic Compression to each minor part:**
  - `"stripe"` (len 6) $\rightarrow$ `"s4e"`
  - `"com"` (len 3) $\rightarrow$ `"c1m"`
  - `"payments"` (len 8) $\rightarrow$ `"p6s"`
  - `"checkout"` (len 8) $\rightarrow$ `"c6t"`
  - `"customer"` (len 8) $\rightarrow$ `"c6r"`
  - `"john"` (len 4) $\rightarrow$ `"j2n"`
  - `"doe"` (len 3) $\rightarrow$ `"d1e"`
- **Re-joining:** `"s4e.c1m/p6s/c6t/c6r.j2n.d1e"`

---

#### Phase 2: Aggregated Minor Part Compression

This phase takes the string resulting from Phase 1 compression and a given integer `k` (representing `minor_parts_threshold`). For each major part, it may further compress a sequence of its minor parts.

For a major part `M` with `N` minor parts (after Phase 1 compression), say $m'_1.m'_2.\dots.m'_N$, and their corresponding **original** minor parts $m_1.m_2.\dots.m_N$:

- If $N \le k$: No further compression occurs for this major part. It retains its Phase 1 compressed form ($m'_1.m'_2.\dots.m'_N$).
- If $N > k$: The last $k$ original minor parts (from $m_{\text{original}}(N-k+1)$ to $m_{\text{original}}(N)$) are considered for aggregation.
  - Let $P_{\text{first}}$ be the first character of the original $m_{\text{original}}(N-k+1)$.
  - Let $P_{\text{last}}$ be the last character of the original $m_{\text{original}}(N)$.
  - Calculate $L_{\text{combined}}$: The total length of the original string formed by concatenating $m_{\text{original}}(N-k+1)$, a dot, $m_{\text{original}}(N-k+2)$, a dot, ..., $m_{\text{original}}(N)$. (This includes the lengths of the $k$ segments and $k-1$ dots).
  - The aggregated compressed string is $P_{\text{first}} + (L_{\text{combined}} - 2 - (k-1)) + P_{\text{last}}$.
    - **Note:** The $(k-1)$ is subtracted because these dots are not "middle characters" to be counted in the numeric part of the compression.
  - The major part `M` is then formed by concatenating the first $N-k$ Phase 1 compressed minor parts ($m'_1. \dots .m'_{(N-k)}$) followed by a dot, and then this newly aggregated compressed string.

**Example 1:** `str = "stripe.com/payments/checkout/customer.john.doe"`, `k = 2`

- **Input to Phase 2:** `"s4e.c1m/p6s/c6t/c6r.j2n.d1e"`
- **Processing major parts:**
  - `s4e.c1m` (from original `stripe.com`): Has $N=2$ minor parts. Since $N \le k$ (2 $\le$ 2), it remains `"s4e.c1m"`.
  - `p6s` (from original `payments`): Has $N=1$ minor part. Since $N \le k$ (1 $\le$ 2), it remains `"p6s"`.
  - `c6t` (from original `checkout`): Has $N=1$ minor part. Since $N \le k$ (1 $\le$ 2), it remains `"c6t"`.
  - `c6r.j2n.d1e` (from original `customer.john.doe`): Has $N=3$ minor parts. Since $N > k$ (3 > 2), we aggregate the last $k=2$ original minor parts: `"john.doe"`.
    - $P_{\text{first}}$ = `'j'` (from `john`).
    - $P_{\text{last}}$ = `'e'` (from `doe`).
    - $L_{\text{combined}}$ for `"john.doe"`: length of `"john"` (4) + length of `.` (1) + length of `"doe"` (3) = 8.
    - Aggregated count: $(L_{\text{combined}} - 2 - (k-1)) = (8 - 2 - (2-1)) = (6 - 1) = 5$.
    - Aggregated string: `"j5e"`.
    - The major part becomes `c6r.j5e` (since $N-k = 3-2 = 1$, `c6r` is the first Phase 1 part that remains).
- **Final Output:** `"s4e.c1m/p6s/c6t/c6r.j5e"`

**Example 2:** `str = "www.api.stripe.com/checkout"`, `k = 3`

- **Input to Phase 1:** `"www.api.stripe.com/checkout"`
- **Output from Phase 1:** `"w1w.a1i.s4e.c1m/c6t"`
- **Input to Phase 2:** `"w1w.a1i.s4e.c1m/c6t"`
- **Processing major parts:**
  - `w1w.a1i.s4e.c1m` (from original `www.api.stripe.com`): Has $N=4$ minor parts. Since $N > k$ (4 > 3), we aggregate the last $k=3$ original minor parts: `"api.stripe.com"`.
    - $P_{\text{first}}$ = `'a'` (from `api`).
    - $P_{\text{last}}$ = `'m'` (from `com`).
    - $L_{\text{combined}}$ for `"api.stripe.com"`: length of `"api"` (3) + `.` (1) + `"stripe"` (6) + `.` (1) + `"com"` (3) = 14.
    - Aggregated count: $(L_{\text{combined}} - 2 - (k-1)) = (14 - 2 - (3-1)) = (12 - 2) = 10$.
    - Aggregated string: `"a10m"`.
    - The major part becomes `w1w.a10m` (since $N-k = 4-3 = 1$, `w1w` is the first Phase 1 part that remains).
  - `c6t` (from original `checkout`): Has $N=1$ minor part. Since $N \le k$ (1 $\le$ 3), it remains `"c6t"`.
- **Final Output:** `"w1w.a10m/c6t"`

---

## J) Accept-Language Header Matching

**Difficulty:** Easy

**Topics:** String, Set, List, Parsing

---

### Problem Description

In HTTP requests, the Accept-Language header specifies the client's preferred languages for content, ordered by preference. This header is a comma-separated list of language tags (e.g., `en-US`, `fr-CA`, `fr-FR`). The leftmost tag is the most preferred, and preference decreases as you move to the right.

Your task is to implement a function for a server that determines which of the client's requested languages can be served. The server has a predefined set of languages it currently supports. You need to find all language tags from the client's Accept-Language header that are also present in the server's supported languages. The resulting list of acceptable languages must maintain the original order of preference from the client's header.

### Examples

**Example 1:**

Input:
acceptLanguageHeader = "en-US, fr-CA, fr-FR"
supportedLanguages = {"fr-FR", "en-US"}

Output: ["en-US", "fr-FR"]

Explanation:

    Client requests "en-US" (most preferred). Server supports "en-US". Add to result.

    Client requests "fr-CA". Server does NOT support "fr-CA". Skip.

    Client requests "fr-FR" (least preferred). Server supports "fr-FR". Add to result.
    Resulting list respects client's original preference order.

**Example 2:**

Input:
acceptLanguageHeader = "fr-CA, fr-FR"
supportedLanguages = {"en-US", "fr-FR"}

Output: ["fr-FR"]

Explanation:

    Client requests "fr-CA". Server does NOT support "fr-CA". Skip.

    Client requests "fr-FR". Server supports "fr-FR". Add to result.

**Example 3:**

Input:
acceptLanguageHeader = "en-US"
supportedLanguages = {"en-US", "fr-CA"}

Output: ["en-US"]

Explanation:

    Client requests "en-US". Server supports "en-US". Add to result.

**Example 4:**

Input:
acceptLanguageHeader = "es-MX, de-DE"
supportedLanguages = {"en-US", "fr-FR"}

Output: []

Explanation: Neither "es-MX" nor "de-DE" are supported by the server.

**Example 5:**

Input:
acceptLanguageHeader = ""
supportedLanguages = {"en-US", "fr-FR"}

Output: []

Explanation: An empty header string means no languages are requested.

**Example 6:**

Input:
acceptLanguageHeader = "en-US, fr-CA"
supportedLanguages = {}

Output: []

Explanation: The server supports no languages, so no match is possible.

### Constraints

- `acceptLanguageHeader` will be a string with a length between 0 and 2000 characters.
- `acceptLanguageHeader` will consist only of alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), commas (,), and spaces ( ).
- Each language tag in `acceptLanguageHeader` will have a length between 1 and 10 characters (e.g., "en", "en-US", "zh-Hans").
- The `supportedLanguages` set will contain between 0 and 500 unique language tags.
- Each language tag in `supportedLanguages` will have a length between 1 and 10 characters and will consist only of alphanumeric characters and hyphens.
- Language tag comparison should be case-sensitive as presented in the input (e.g., "en-US" is different from "EN-US" unless explicitly normalized).
- Whitespace surrounding commas in `acceptLanguageHeader` should be handled correctly (e.g., `"en-US , fr-CA"` should be parsed as `"en-US"` and `"fr-CA"`).

---

## K) Currency Exchange Rate Calculations

**Difficulty:** Medium

**Topics:** Graph, Hash Map, Depth-First Search (DFS), Breadth-First Search (BFS)

---

### Problem Description

You are given a string `exchangeRatesData` that represents a set of atomic (direct) exchange rates between various currencies. This string is formatted as a comma-separated list of entries, where each entry is `SOURCE_CURRENCY:TARGET_CURRENCY:RATE`. For example, `"USD:AUD:1.4,CAD:USD:0.8,USD:JPY:110"` indicates that 1 USD buys 1.4 AUD, 1 CAD buys 0.8 USD, and 1 USD buys 110 JPY.

Your task is to process this input and identify all possible conversion rates that can be established, considering both direct rates and rates derivable through a single intermediate currency. When multiple paths exist for the same currency pair, you must determine the "best" conversion rate based on the following rules:

1.  **Atomic Conversion Rates:** Rates directly provided in the input string (e.g., `USD:AUD:1.4`).
2.  **Inverse Conversion Rates:** For every atomic rate A:B:R, its inverse B:A:(1/R) is also implicitly available.
3.  **Derived One-Hop Conversion Rates:** A rate A:C can be derived if there exists an intermediate currency B such that both A:B and B:C conversion rates are known (either atomic or inverse). The derived rate A:C would be `Rate(A:B) * Rate(B:C)`.
4.  **"Best Conversion" Principle:** For any given `SOURCE_CURRENCY` to `TARGET_CURRENCY` pair, if multiple direct or one-hop paths allow for conversion, the "best" conversion rate is the one that yields the **maximum amount of TARGET_CURRENCY for 1 unit of SOURCE_CURRENCY**.

Your goal is to return all unique currency pair conversions (in the format `SOURCE:TARGET:RATE`) that can be either atomically looked up or calculated through one intermediate currency, always applying the "Best Conversion" principle where multiple paths exist.

### Examples

**Example 1:**

Input: exchangeRatesData = "USD:AUD:1.4,CAD:USD:0.8,USD:JPY:110"
Output:
[
"AUD:CAD:0.714",
"AUD:JPY:78.571",
"AUD:USD:0.714",
"CAD:AUD:1.120",
"CAD:JPY:88.000",
"CAD:USD:0.800",
"JPY:AUD:0.013",
"JPY:CAD:0.011",
"JPY:USD:0.009",
"USD:AUD:1.400",
"USD:CAD:1.250",
"USD:JPY:110.000"
]
Explanation: Let's trace some conversions:

    USD:AUD:1.4 (Atomic) -> stored as 1.4

    CAD:USD:0.8 (Atomic) -> stored as 0.8

    USD:JPY:110 (Atomic) -> stored as 110
    Implicit Inverses:

    AUD:USD:1/1.4 = 0.714...

    USD:CAD:1/0.8 = 1.25

    JPY:USD:1/110 = 0.009...
    One-Hop Conversions (Examples):

    CAD:AUD: via USD

        CAD:USD:0.8 (Atomic)

        USD:AUD:1.4 (Atomic)

        CAD:AUD = 0.8 * 1.4 = 1.12

    CAD:JPY: via USD

        CAD:USD:0.8 (Atomic)

        USD:JPY:110 (Atomic)

        CAD:JPY = 0.8 * 110 = 88.0

    AUD:JPY: via USD

        AUD:USD: (Inverse of USD:AUD) = 0.714...

        USD:JPY:110 (Atomic)

        AUD:JPY = (1/1.4) * 110 = 78.571…

**Example 2:**

Input: exchangeRatesData = "A:B:2.0, B:C:3.0, A:D:1.0, D:C:7.0"
Output:
[
"A:B:2.000",
"A:C:7.000",
"A:D:1.000",
"B:A:0.500",
"B:C:3.000",
"B:D:0.143",
"C:A:0.143",
"C:B:0.333",
"C:D:0.143",
"D:A:1.000",
"D:B:7.000",
"D:C:7.000"
]
Explanation: Consider A:C:

    Direct Path: A:C (Not given in input)

    One-Hop via B: A:B:2.0, B:C:3.0 => A:C = 2.0 * 3.0 = 6.0

    One-Hop via D: A:D:1.0, D:C:7.0 => A:C = 1.0 * 7.0 = 7.0
    Applying the "Best Conversion" principle, the rate for A:C is max(6.0, 7.0) = 7.0.

**Example 3:**

Input: exchangeRatesData = "EUR:GBP:0.85, CHF:JPY:125"
Output:
[
"CHF:JPY:125.000",
"EUR:GBP:0.850",
"GBP:EUR:1.176",
"JPY:CHF:0.008"
]
Explanation: No intermediate currency connects EUR/GBP rates to CHF/JPY rates within one hop. Only atomic rates and their inverses are returned.

### Constraints

- `exchangeRatesData` will be a string with a length between 0 and 5000 characters.
- `exchangeRatesData` will contain comma-separated entries (`SOURCE:TARGET:RATE`).
- `SOURCE_CURRENCY` and `TARGET_CURRENCY` will be uppercase English letters (A-Z) with lengths between 1 and 5 characters.
- `RATE` will be a positive floating-point number.
- The number of unique currencies will be at most 50.
- Rates are always positive.
- All atomic rates are explicitly given. Implicit rates (e.g., `USD:USD`) are not given and should be derived as 1.0.
- Floating point comparisons should account for precision (e.g., consider values equal if their absolute difference is less than `1e-9`).
- Output rates must be rounded to exactly 3 decimal places.

---

## L) Brace Expansion for Paths

**Difficulty:** Medium

**Topics:** String, Backtracking, Recursion

---

### Problem Description

You are given a string `expression` which consists of several comma-separated tokens enclosed within opening (`'{'`) and closing (`'}'`) curly braces. The string `expression` might or might not have a prefix before the opening curly brace (`'{'`) and a suffix after the closing curly brace (`'}'`).

You have to return a list of strings as output for each comma-separated item as shown below in the examples.

### Examples

**Example 1:**

Input: "/2022/{jan,feb,march}/report"
Output:
"/2022/jan/report"
"/2022/feb/report"
"/2022/march/report"

**Example 2:**

Input: "over{crowd,eager,bold,fond}ness"
Output:
"overcrowdness"
"overeagerness"
"overboldness"
"overfondness"

**Example 3:**

Input: "read.txt{,.bak}"
Output:
"read.txt"
"read.txt.bak"

---

#### Follow-up

If there are less than 2 tokens enclosed within curly braces or an incorrect expression (e.g., opening and closing braces not present, only opening brace present, closing brace present before opening brace, etc.), return the output same as the input string.

**Example 1:**

Input: sun{mars}rotation
Output: sun{mars}rotation

**Example 2:**

Input: minimum{}change
Output: minimum{}change

**Example 3 (Incorrect Input):**

Input: hello-world
Output: hello-world

**Example 4 (Incorrect Input):**

Input: hello-{-world
Output: hello-{-world

**Example 5 (Incorrect Input):**

Input: hello-}-weird-{-world
Output: hello-}-weird-{-world

---

## M) Minimum Shipping Cost

**Difficulty:** Medium

**Topics:** Graph, Dijkstra's Algorithm, Shortest Path, Hash Map

---

### Problem Description

You are given a string `shipping_data_string` that describes various direct shipping routes and their associated costs. This string is formatted as a series of entries separated by colons (`:`). Each entry represents a single direct route and is composed of comma-separated values: `FROM_LOCATION,TO_LOCATION,CARRIER,COST`.

For example, `"US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7"` means:

- A direct route from US to UK via UPS costs 5.
- A direct route from US to CA via FedEx costs 3.
- A direct route from CA to UK via DHL costs 7.

Your task is to implement a function that determines the minimum cost to ship an item from a given source location to a destination location. The calculation of this minimum cost should consider two types of paths:

1.  **Direct Routes:** Paths explicitly provided in the `shipping_data_string`. If multiple carriers offer a direct route between the same `FROM` and `TO` locations, only the route with the lowest cost for that specific `FROM:TO` segment should be considered.
2.  **One-Hop Indirect Routes:** Paths that involve exactly one intermediate stop. For example, to ship from A to C, you can use an intermediate location B, where direct routes A $\rightarrow$ B and B $\rightarrow$ C exist. The total cost for such a path would be `Cost(A -> B) + Cost(B -> C)`.

When evaluating the total cost from source to destination, you must choose the path (either direct or one-hop indirect) that results in the absolute minimum total cost.

### Examples

**Example 1:**

Input:
shipping_data_string = "US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7:US,UK,RoyalMail,12"
source = "US"
destination = "UK"
Output: 5.0

Explanation:
Direct routes from US to UK:

    US -> UK via UPS: Cost 5

    US -> UK via RoyalMail: Cost 12
    Minimum direct cost: 5.0

One-hop route via CA:

    US -> CA via FedEx: Cost 3

    CA -> UK via DHL: Cost 7
    Total one-hop cost: 3 + 7 = 10.0

Comparing all available options (direct vs. one-hop): min(5.0, 10.0) = 5.0

**Example 2:**

Input:
shipping_data_string = "US,FR,AirCargo,20:US,CA,FedEx,3:CA,FR,DHL,15"
source = "US"
destination = "FR"
Output: 18.0

Explanation:
Direct routes from US to FR:

    US -> FR via AirCargo: Cost 20.0

One-hop route via CA:

    US -> CA via FedEx: Cost 3.0

    CA -> FR via DHL: Cost 15.0
    Total one-hop cost: 3.0 + 15.0 = 18.0

Comparing all available options: min(20.0, 18.0) = 18.0

**Example 3:**

Input:
shipping_data_string = "US,CA,FedEx,3:UK,FR,DHL,7"
source = "US"
destination = "DE"
Output: -1.0

Explanation:
There are no direct routes from US to DE.
There are no intermediate locations that connect US to DE.

**Example 4:**

Input:
shipping_data_string = "A,B,C1,10:B,D,C2,5:A,E,C3,4:E,D,C4,12"
source = "A"
destination = "D"
Output: 15.0

Explanation:
Direct routes from A to D: None

One-hop route via B:

    A -> B: Cost 10

    B -> D: Cost 5
    Total cost: 10 + 5 = 15.0

One-hop route via E:

    A -> E: Cost 4

    E -> D: Cost 12
    Total cost: 4 + 12 = 16.0

Comparing all available options: min(15.0, 16.0) = 15.0
