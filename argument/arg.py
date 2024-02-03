import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description='Argument parsing example')

# Add arguments
parser.add_argument('-f', '--file', help='Path to the file')
parser.add_argument('-n', '--number', type=int, help='A number')

# Parse the arguments
args = parser.parse_args()

# Access the values of the arguments
file_path = args.file
number = args.number

# Use the arguments
print(f'File path: {file_path}')
print(f'Number: {number}')
