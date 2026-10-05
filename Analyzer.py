from string import whitespace

class Analyzer:
    def __init__(self, file):
        self.letter_count = {}
        self.word_count = {}
        self.digit_count = {}
        self.number_count = {}
        self.symbol_count = {}
        self.letter_count_total = 0
        self.whitespace_char_count = 0
        self.word_count_total = 0
        self.num_count_total = 0
        self.digit_count_total = 0
        self.symbol_count_total = 0
        self.current = None
        self.final_totals = {}

        try:
            self.file = open(file, 'r')
            self.analyze()
        except FileNotFoundError:
            print(f"ERROR: File '{file}' not found.")
            self.current = "Error"

    def analyze(self):
        if self.current == "Error":
            return

        self.nextChar()
        try:
            while True:
                print(f"Token processing... {self.current}")
                # Checks if current token is whitespace character
                if self.current in whitespace:
                    # Increments the whitespace character counter
                    self.whitespace_char_count += 1
                    # Moves to the next character in the file
                    self.nextChar()
                # Ends the analysis if current token is an error
                elif self.current == "EOS" or self.current == "Error":
                    break
                # Checks if current token is alphabetic character
                elif self.current.isalpha():
                    # Processes current token as a word
                    self.processWord()
                # Checks if current token is a digit
                elif self.current.isdigit():
                    # Increments the digit character counter
                    self.digit_count_total += 1
                    # Processes current token as a number
                    self.processNumber()
                # If current token is none of the above, it is processed as a symbol
                else:
                    self.processSymbol()
                
        # Catches any exceptions that might occur during analysis and prints an error message
        except Exception as e:
            print(f"ERROR: An error occurred during analysis: {e}")
            self.current = "Error"

    def nextChar(self):
        self.current = self.file.read(1)
        if not self.current:
            self.current = "EOS"

    # Processes the current token as a word or string of characters
    def processWord(self):
        word = ""
        while self.current.isalpha() and self.current != "EOS":
            word += self.current
            # Increments the alphabetic character counter
            self.letter_count_total += 1
            # Increments the count for the current letter
            self.letter_count[self.current] = self.letter_count.get(self.current, 0) + 1
            # Proceeds to the next character
            self.nextChar()
        # Increments the alphabetic character counter
        self.word_count_total += 1
        # Increments the count for the current word
        self.word_count[word] = self.word_count.get(word, 0) + 1

    # Processes the current token as a number
    def processNumber(self):
        num = ""
        while self.current.isdigit() and self.current != "EOS":
            num += self.current
            # Increments the digit character counter
            self.digit_count_total += 1
            # Increments the count for the current digit
            self.digit_count[self.current] = self.digit_count.get(self.current, 0) + 1
            # Proceeds to the next character
            self.nextChar()
        # Increments the numeric character counter
        self.num_count_total += 1
        # Increments the count for the current number
        self.number_count[num] = self.number_count.get(num, 0) + 1

    def processSymbol(self):
        symbol = self.current
        # Increments the symbol character counter
        self.symbol_count_total += 1
        # Increments the count for the current symbol
        self.symbol_count[symbol] = self.symbol_count.get(symbol, 0) + 1
        # Proceeds to the next character
        self.nextChar()

    def getResults(self):
        self.final_totals = {
            "letter_count": self.letter_count,
            "word_count": self.word_count,
            "digit_count": self.digit_count,
            "number_count": self.number_count,
            "symbol_count": self.symbol_count,
            "letter_count_total": self.letter_count_total,
            "whitespace_char_count": self.whitespace_char_count,
            "word_count_total": self.word_count_total,
            "num_count_total": self.num_count_total,
            "digit_count_total": self.digit_count_total,
            "symbol_count_total": self.symbol_count_total
        }
        return self.final_totals