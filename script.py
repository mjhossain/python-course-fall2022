import csv

with open("deniro.csv", "r") as csv_handle:
    csv_content = csv.DictReader(csv_handle, delimiter=',')

    
    print("\n\nMovies with Score of 70+ from year 1900s\n")
    num_of_movies_1900 = 0
    for line in csv_content:
        if((int(line['Year']) < 2000) and (int(line[' "Score"']) >= 70)):
            num_of_movies_1900 += 1
            print(line[' "Title"'])
    print('\nTotal Movies: ', num_of_movies_1900)
    print("\n___________________________________________________\n")

    # Resets the File Handle
    csv_handle.seek(0)
    next(csv_content)

    print("Movies with Score of 70+ from year 2000s\n")
    num_of_movies_2000 = 0
    for line in csv_content:
        if((int(line['Year']) >= 2000) and (int(line[' "Score"']) >= 70)):
            num_of_movies_2000 += 1
            print(line[' "Title"'])
    print('\n\nTotal Movies: ', num_of_movies_2000)
    print()