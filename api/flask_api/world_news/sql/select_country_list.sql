WITH tmp AS (
    select * from country
)
SELECT to_json(tmp) FROM tmp
