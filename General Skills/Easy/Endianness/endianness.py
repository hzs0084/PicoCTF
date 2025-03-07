#!/usr/bin/env python3

def find_little_endian(word: str) -> str:
    """
    Reproduces the exact logic of the C version:

        char *find_little_endian(const char *word)
        {
            size_t word_len = strlen(word);
            char *little_endian = (char *)malloc((2 * word_len + 1) * sizeof(char));

            for (size_t i = word_len; i-- > 0;)
            {
                snprintf(&little_endian[(word_len - 1 - i) * 2], 3, "%02X", (unsigned char)word[i]);
            }

            little_endian[2 * word_len] = '\\0';
            return little_endian;
        }
    """

    word_len = len(word)
    # Build the hex string in reverse order
    reversed_hex = []
    for i in reversed(range(word_len)):
        reversed_hex.append(f"{ord(word[i]):02X}")
    return "".join(reversed_hex)


def find_big_endian(word: str) -> str:
    """
    Reproduces the exact logic of the C version:

        char *find_big_endian(const char *word)
        {
            size_t length = strlen(word);
            char *big_endian = (char *)malloc((2 * length + 1) * sizeof(char));

            for (size_t i = 0; i < length; i++)
            {
                snprintf(&big_endian[i * 2], 3, "%02X", (unsigned char)word[i]);
            }

            big_endian[2 * length] = '\\0';
            return big_endian;
        }
    """

    length = len(word)
    # Build the hex string in normal (forward) order
    forward_hex = []
    for i in range(length):
        forward_hex.append(f"{ord(word[i]):02X}")
    return "".join(forward_hex)


if __name__ == "__main__":
    # Example usage:
    test_word = "yrvdy"
    print("Word:       ", test_word)
    print("Little Endian:", find_little_endian(test_word))
    print("Big Endian:   ", find_big_endian(test_word))
