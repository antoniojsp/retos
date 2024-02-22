--https://leetcode.com/problems/queries-quality-and-percentage/description/
# Write your MySQL query statement below
SELECT
    q.query_name,
    ROUND(SUM(rating/position)/(SELECT COUNT(*) FROM queries WHERE query_name = q.query_name), 2) AS quality,
    ROUND(((SELECT COUNT(*) FROM queries WHERE query_name = q.query_name AND rating < 3)
            /
           (SELECT COUNT(*) FROM queries WHERE query_name = q.query_name))*100, 2)

    AS poor_query_percentage

FROM queries q
WHERE q.query_name IS NOT NULL
GROUP BY q.query_name;