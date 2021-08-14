WITH tmp AS (
    select t.id,t.original_id,to_char(t.date, 'yyyy-mm-dd') date,t.genre,t.title,t.text, cu.site_name site_name,co.country_ja,t.site_id,t.country_id from news_list_translate t INNER JOIN crawl_urls cu ON t.site_id = cu.id INNER JOIN country co ON t.country_id = co.id
)
SELECT to_json(tmp) FROM tmp
