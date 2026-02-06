# Word Password Generator

This is a command-line password generator written in Python that creates secure, customizable passwords that are easy for humans to remember.  It randomly selects from a list of ~7000 common words and randomly formats them into a password.  If a number is required it can be optionally added; the number will be put randomly in the word list.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

**Author:** Michael C. Hernandez  
**Date:** February 5, 2026  
**Email:** michaelhern@hotmail.com  

---

## Features

- **Cryptographically secure**: Uses Python’s [`secrets`](https://docs.python.org/3/library/secrets.html) module, not [`random`](https://docs.python.org/3/library/random.html)
- **Customizable length**: Default is 5 words, minimum is 1.
- **Includes a special character every time**
  **Includes a number when requested**

---

## Usage

Run the script using Python 3:

```bash
python word_password_generator.py [OPTIONS]
```

---

## Options

| Option                  | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| `-l`, `--num_of_words`  | Number of words to have in your password (default is 5)   |
| `-n`, `--number`        | Include an int in the password                            |

---

## Example: Generate a 4-word password with a number

python word_password_generator.py -l 4 -n

---

## Requirements

  * Python 3.6 or later

---