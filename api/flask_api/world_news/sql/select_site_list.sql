WITH tmp AS (
    select * from crawl_urls
)
SELECT to_json(tmp) FROM tmp
