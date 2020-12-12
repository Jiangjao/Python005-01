ALTER TABLE `table_name` ADD INDEX index_name ( `name` )

ALTER TABLE `table_name` ADD INDEX index_id ( `id` ) 

-- 给数据库增加一个新的查询时，都要评估一下，是不是有索引可以支撑新的查询语句，
-- 如果有必要，就新建索引
-- 但是增加新索引付出的代价是，会降低数据插入、删除和更新的性能。
-- 所以，对于更新频繁并且对更新性能要求较高的表，可以尽量少建所i。
-- source:<后端存储实战课>