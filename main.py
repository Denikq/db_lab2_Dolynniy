import psycopg2

username = 'postgres'
password = '00000000'
database = 'dol01_DB'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT TRIM(book_name) AS book_name, rating_average 
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

def mlx(x):   # максимальна довжина строки
    max_len = 0
    for i in range(len(x)):
        if len(x[i]) > max_len:
            max_len = len(x[i])
    return max_len

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur1 = conn.cursor()
    cur1.execute(query_1)
    b_name = []
    r_average = []

    for row in cur1:
        b_name.append(row[0])
        r_average.append(row[1])

    max_len = mlx(b_name)  # максимальна довжина імені (потрібно для красивого вивода)
    print('Найпопулярніші книги')
    print('-' * (max_len + 9))
    for i in range(len(b_name)):
        print(b_name[i], ' ' * (max_len - len(b_name[i])), '| ', r_average[i])
    print('-' * (max_len + 9))
    print('\n')


    cur2 = conn.cursor()
    cur2.execute(query_2)
    a_id = []
    r_count = []

    for row in cur2:
        a_id.append(row[0])
        r_count.append(row[1])

    print('кількість оцінок роботи кожного автора/групи авторів')
    # (якщо автор писав одну книгу сам, а іншу з кимось, це вважаються різні автори)
    print('-' * 13)
    for i in range(len(a_id)):
        print(a_id[i], ' | ', r_count[i])
    print('-' * 13)
    print('\n')


    cur3 = conn.cursor()
    cur3.execute(query_3)
    year = []
    count = []

    for row in cur3:
        year.append(row[0])
        count.append(row[1])

    print('Кількість книг за кожний рік')
    print('-' * 11)
    for i in range(len(year)):
        print(int(year[i]), '  | ', count[i])
    print('-' * 11)
