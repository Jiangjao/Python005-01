-- #修改字符集

alter database testdb character set utf8mb4;

-- #验证字符集

show variables like '%character%';

-- 创建用户
CREATE USER 'Dj'@'%' IDENTIFIED BY 'password';

-- 改变密码强度配置
set global validate_password_policy = 0 ;

-- 添加用户权限
grant all privileges on *.* to 'Dj'@'%' IDENTIFIED by 'password';
