-- Найпопулярніші книги
SELECT TRIM(book_name) AS book_name, rating_average 
FROM book, rating
WHERE book.rating_id = rating.rating_id
ORDER BY rating_average DESC


-- Кількість оцінок роботи кожного автора
-- (якщо автор писав одну книгу сам, а іншу з кимось, 
-- це вважаються різні автори)
SELECT book.author_id, SUM(rating_count) 
FROM book, author, rating
WHERE book.author_id = author.author_id 
AND book.rating_id = rating.rating_id
GROUP BY book.author_id


-- Кількість книг за кожний рік
SELECT EXTRACT(YEAR FROM book_date) AS book_date, COUNT(*) AS number_of_books 
FROM book
GROUP BY EXTRACT(YEAR FROM book_date)
ORDER BY EXTRACT(YEAR FROM book_date)
