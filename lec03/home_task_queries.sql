/*
 Завдання на SQL до лекції 03.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням. */

SELECT
	c.name AS "Category name",
	count(f.film_id) AS "Films count"
FROM
	category c
INNER JOIN film_category fc ON c.category_id = fc.category_id
INNER JOIN film f ON f.film_id = fc.film_id
GROUP BY
	c.name
ORDER BY
	"Films count" DESC,
	c.name;

/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням. */

SELECT
	a.first_name, 
	a.last_name, 
	count(r.rental_id) AS "Rented times"
FROM 
	actor a
INNER JOIN film_actor fa ON fa.actor_id = a.actor_id 
INNER JOIN inventory i ON fa.film_id = i.film_id
INNER JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY
	a.actor_id
ORDER BY
	"Rented times" DESC
LIMIT 10; 

/*
3.
Вивести категорію фільмів, на яку було витрачено найбільше грошей в прокаті */

SELECT 
	c.name AS "Category name",
    SUM(p.amount) AS "Total revenue"
FROM 
	film f 
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN category c ON fc.category_id = c.category_id
INNER JOIN inventory i ON f.film_id = i.film_id
INNER JOIN rental r ON i.inventory_id = r.inventory_id
INNER JOIN payment p ON r.rental_id = p.rental_id
GROUP BY 
	c.name
ORDER BY 
	"Total revenue" DESC
LIMIT 1; 

/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN */

SELECT
	f.title
FROM
	film f
LEFT JOIN inventory i ON f.film_id = i.film_id
WHERE
	i.inventory_id is null
ORDER BY
	f.title;


/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”. */

SELECT
	a.first_name,
	a.last_name,
	count(fc.film_id) as "Appeared in films of Children category"
FROM
	actor a
INNER JOIN film_actor fa ON a.actor_id = fa.actor_id
INNER JOIN film_category fc ON fa.film_id = fc.film_id
WHERE
	fc.category_id = 3
GROUP BY
	a.actor_id
ORDER BY
	count(fc.film_id) DESC
LIMIT 3;