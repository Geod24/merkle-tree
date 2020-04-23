# Merkle Tree infrastructure

This is a simple Merkle Tree implementation with Python.  
To be implemented in C++ / D.  
Last updated on 2020-04-23.

## Installation

### Linux

Check if Python is installed.
```bash
$ python --version
```

If not, install Python.
```bash
$ sudo apt-get install python3
```

### macOS

Check if Python is installed.
```bash
$ python 
```

If not, install with Homebrew.
```bash
$ brew install python3
```

## Usage

The `produce` mode produces hashes from strings arguments by appying SHA256 twice.  

```
$ python merkle.py produce "The quick brown fox" "jump over" "the" "lazy dog"
```
The program prints the Merkle tree generated from those values.  
The hash in the Level 0 is the Merkle Root.
```
Level 0:
018FB04252A594A8049CBFE9E34848249040E1FA7E170501E17ADC06393D4DC3
Level 1:
836C2FE675884DB41C49215F8A91E6560B1EA752F683DB793E9B86180CA235F8
49B9A6B1346DC768898A16C2DAD9D554349C9150F8B2809AC7D48B305C4D3650
Level 2:
7743034D22491720B723B68AFD046BE66969409254DC79A153E290C81A8F238A
F51DF418D9D7BAFDCFDC4320409E08E39858D0D686FEE959EA545E6D7C214F71
1E7C521A055F0F08CEA3FADED5923CCA2D8F4366A62AAA8A8B843A842AA656B8
144BEE93D8F6350C6E38C96EEB11DE2CD249A7BD5D23FF4C91EB46573B5AF3BA
```

If there is an error in the arguments or not enough arguments,  the program exits with a `<EXIT_FAILURE>` error.

However, this only works when the number of nodes produces a balanced tree.
This means the number of arguments is a power of 2.
In the event the tree is not balanced, the last value is repeated to balance the tree:

```
$ python merkle.py produce "The quick brown fox" "jump over" "the" "lazy" "dog"
```
```
Level 0:
9AF409C11D320898DA335F82FAC8918014A6589E55F2C98F2B3C468ED83F6ACE
Level 1:
6E76CEB1CBD48BE752949D832B4AB2848E7B9DF6A4286A524C7B134A4A9DF458
156B626C730889C1CD1A1F05D55EC3C16AF6DC5BD6977E0BE2A1935C86A74CCF
Level 2:
836C2FE675884DB41C49215F8A91E6560B1EA752F683DB793E9B86180CA235F8
31A1892ED0C9857597D9D8902E1A05D5A3A99DEAD7FADB9E69BF319FC22C1AE6
CBBC43D5431E285C2770E9F9084663CB6CCF4B23228DD8E90A30B361A80CC57D
CBBC43D5431E285C2770E9F9084663CB6CCF4B23228DD8E90A30B361A80CC57D
Level 3:
7743034D22491720B723B68AFD046BE66969409254DC79A153E290C81A8F238A
F51DF418D9D7BAFDCFDC4320409E08E39858D0D686FEE959EA545E6D7C214F71
1E7C521A055F0F08CEA3FADED5923CCA2D8F4366A62AAA8A8B843A842AA656B8
6CFAC15CDF8A0065DCF55ADC0F9CE57847747EA94D63A276CACCEC6F64A8819D
9DA6BDB1E8A041F1795966F87619385B713E4BEFE723130ED2748939EF791579
9DA6BDB1E8A041F1795966F87619385B713E4BEFE723130ED2748939EF791579
9DA6BDB1E8A041F1795966F87619385B713E4BEFE723130ED2748939EF791579
9DA6BDB1E8A041F1795966F87619385B713E4BEFE723130ED2748939EF791579
```

## Requirements
- [ ] The program MUST run on a recent Linux and/or Mac OS X (we will test on our machines)
> Verify mode not implemented
- [x] You MUST use one of the following languages: D, C++, C, Go, Rust, Python
- [x] You MUST provide us with instructions on how to build your code
- [x] You MUST NOT use any library function, except for hashing and writing to the console
- [x] You MUST handle errors gracefully (e.g. no hard crash)
- [ ] The output SHOULD follow the same format as the provided example
> Hash function outputs different values. Need to try other libraries.
- [ ] Documentation and additional tests CAN be added at your discretion

Not all requirements were met due to time constraints and a lack of knowledge.  

## Things learned
- [x] SHA-2 / SHA-256
- [x] Merkle-Damgard construction / hash function
- [x] Length-extension attacks

## Program-specific improvements needed
- [ ] Verification mode incomplete
  - [x] Understand concept of verification
  - [ ] Convert string input into hash object
- [ ] Use an external dependency, such as libsodium, Crypto++

## New concepts to learn
- [ ] Learn how to work with C++ compiler instead of Python's interpreter
