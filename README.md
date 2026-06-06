白泽回测系统的后端

运行前准备：
```bash
# 生成RSA密钥
openssl genpkey -algorithm RSA -out certs/private.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in certs/private.pem -out certs/public.pem

# 迁移数据
python manage.py makemigrations
python manage.py migrate

```

运行命令:
```bash
python manage.py runserver 8000
```