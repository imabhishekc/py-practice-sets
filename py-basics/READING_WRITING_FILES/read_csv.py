with open('stocks.csv', 'r') as f, open('output.csv', 'w') as out:
    out.write("Company Name,PE Ratio,PB Ratio\n")

    next(f)

    for line in f:
        tokens = line.strip().split(",")

        stock = tokens[0].strip()
        price = float(tokens[1].strip())
        eps = float(tokens[2].strip())
        book = float(tokens[3].strip())

        # Calculate ratios
        pe = round(price / eps, 2)
        pb = round(price / book, 2)

        out.write(f"{stock},{pe},{pb}\n")