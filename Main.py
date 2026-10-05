from Analyzer import Analyzer
import sys

def main():
    # Initialize the Analyzer
    input_file = input("Enter the path to the input file: ")
    A = Analyzer(input_file)
    print("Analyzer created successfully.")
    results = A.getResults()
    for key, value in results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()