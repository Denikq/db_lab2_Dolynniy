import psycopg2
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

username = 'postgres'
password = '00000000'
database = 'dol01_DB'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT TRIM(book_name), rating_average 
FROM book, rating
WHERE book.rating_id = rating.rating_id
ORDER BY rating_average DESC
'''
query_2 = '''
SELECT book.author_id, SUM(rating_count) 
FROM book, author, rating
WHERE book.author_id = author.author_id 
AND book.rating_id = rating.rating_id
GROUP BY book.author_id
'''
query_3 = '''
SELECT EXTRACT(YEAR FROM book_date) AS book_date, COUNT(*) AS number_of_books 
FROM book
GROUP BY EXTRACT(YEAR FROM book_date)
ORDER BY EXTRACT(YEAR FROM book_date)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:
    cur = conn.cursor()

    cur.execute(query_1)
    b_name = []
    r_average = []

    for row in cur:
        b_name.append(row[0])
        r_average.append(row[1])

    fig, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    bar_ax.set_title('Найпопулярніші книги')
    bar = bar_ax.bar(b_name, r_average)
    bar_ax.set_xticks(range(len(b_name)))
    bar_ax.set_xticklabels(b_name, rotation=90)
    bar_ax.yaxis.set_major_locator(ticker.MultipleLocator(1))


    cur.execute(query_2)
    a_id = []
    r_count = []

    for row in cur:
        a_id.append(row[0])
        r_count.append(row[1])

    pie_ax.pie(r_count, labels=a_id, autopct='%1.1f%%')
    pie_ax.set_title('Кількість оцінок роботи кожного автора/групи авторів')

    cur.execute(query_3)
    year = []
    count = []

    for row in cur:
        year.append(int(row[0]))
        count.append(row[1])

    graph_ax.plot(year, count, marker='o')
    graph_ax.set_title('Кількість книг за кожний рік')
    graph_ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    graph_ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

plt.show()
