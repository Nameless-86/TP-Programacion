csv_listings = open('listings.csv')
for fila in csv_listings:
    print(fila.split(',')[1])