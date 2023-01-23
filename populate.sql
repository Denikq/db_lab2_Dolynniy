-- ------------------------
-- Populate Author table
-- ------------------------
INSERT INTO Author(author_id, author_name_1, author_name_2, author_name_3)
VALUES(0, 'J.K. Rowling', 'Mary GrandPré', NULL);
INSERT INTO Author(author_id, author_name_1, author_name_2, author_name_3)
VALUES(1, 'J.K. Rowling', NULL, NULL);
INSERT INTO Author(author_id, author_name_1, author_name_2, author_name_3)
VALUES(2, 'Douglas Adams', NULL, NULL);
INSERT INTO Author(author_id, author_name_1, author_name_2, author_name_3)
VALUES(3, 'Bill Bryson', NULL, NULL);
INSERT INTO Author(author_id, author_name_1, author_name_2, author_name_3)
VALUES(4, 'J.R.R. Tolkien', 'Alan Lee', NULL);


-- ------------------------
-- Populate Rating table
-- ------------------------
INSERT INTO Rating(rating_id, rating_count, rating_average)
VALUES(0, 2095690, 4.57);
INSERT INTO Rating(rating_id, rating_count, rating_average)
VALUES(1, 2153167, 4.49);
INSERT INTO Rating(rating_id, rating_count, rating_average)
VALUES(2, 6333, 4.42);
INSERT INTO Rating(rating_id, rating_count, rating_average)
VALUES(3, 4930, 4.42);
INSERT INTO Rating(rating_id, rating_count, rating_average)
VALUES(4, 248558, 4.21);
INSERT INTO Rating(rating_id, rating_count, rating_average)
VALUES(5, 7270, 3.44);
INSERT INTO Rating(rating_id, rating_count, rating_average)
VALUES(6, 1618, 4.50);


-- ------------------------
-- Populate Book table
-- ------------------------
INSERT INTO Book(book_id, book_name, book_pages, book_date, author_id, rating_id)
VALUES(0, 'Harry Potter and the Half-Blood Prince (Harry Potter #6)', 652, '16/09/2006', 0, 0);
INSERT INTO Book(book_id, book_name, book_pages, book_date, author_id, rating_id)
VALUES(1, 'Harry Potter and the Order of the Phoenix (Harry Potter #5)', 870, '01/09/2004', 0, 1);
INSERT INTO Book(book_id, book_name, book_pages, book_date, author_id, rating_id)
VALUES(2, 'Harry Potter and the Chamber of Secrets (Harry Potter #2)', 352, '01/11/2003', 1, 2);
INSERT INTO Book(book_id, book_name, book_pages, book_date, author_id, rating_id)
VALUES(3, 'The Hitchhikers Guide to the Galaxy (Hitchhikers Guide to the Galaxy #1)', 215, '03/08/2004', 2, 3);
INSERT INTO Book(book_id, book_name, book_pages, book_date, author_id, rating_id)
VALUES(4, 'A Short History of Nearly Everything', 544, '14/09/2004', 3, 4);
INSERT INTO Book(book_id, book_name, book_pages, book_date, author_id, rating_id)
VALUES(5, 'Bill Brysons African Diary', 55, '03/12/2002', 3, 5);
INSERT INTO Book(book_id, book_name, book_pages, book_date, author_id, rating_id)
VALUES(6, 'The Lord of the Rings (The Lord of the Rings #1-3)', 1216, '16/09/2006', 4, 6);

