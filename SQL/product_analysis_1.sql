SELECT p.product_name, s.price, s.year
FROM Sales s
JOIN Product p ON s.product_id = p.product_id