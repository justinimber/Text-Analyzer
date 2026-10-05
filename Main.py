from Analyzer import Analyzer
import sys

def main():
# Initialize the Analyzer
  A = Analyzer(sys.argv[1])
  print("Analyzer created successfully.")
  results = A.getResults()
  for key, value in results.items():
    print(f"{key}: {value}")

if __name__ == "__main__":
  main()