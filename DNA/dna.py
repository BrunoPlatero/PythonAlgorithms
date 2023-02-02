import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a new list
    new_database = []
    with open(sys.argv[1]) as file:
        reader_database = csv.DictReader(file)
        # For each row in the file, append it to our new list
        for i in reader_database:
            new_database.append(i)

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        # Use read function to read text file into memory
        sequence = file.read()

    # Find longest match of each STR in DNA sequence

    # Store each subsequence into a list, using list and keys functions, ignoring the name
    # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_dictionary_keys
    # https://stackoverflow.com/questions/40443331/how-to-get-everything-from-the-list-except-the-first-element-using-list-slicing
    # https://www.w3schools.com/python/ref_dictionary_keys.asp
    subsequences = list(new_database[0].keys())[1:]

    # Iterate through the subsequences, assigning to each one the longest match and store the results in a dictionary
    results = {}
    for subsequence in subsequences:
        results[subsequence] = longest_match(sequence, subsequence)

    # Check database for matching profiles
    # Loop over each person on database
    for person in new_database:
        # Keep track of how many subsequences match
        count = 0
        # Loop over every subsequence in subsequences list, updating count when results match
        for subsequence in subsequences:
            if int(person[subsequence]) == results[subsequence]:
                count += 1
        # If count equals all subsequences, we found a match
        if count == len(subsequences):
            print(person["name"])
            return
    # If not match found, print it
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
