# Entrypoint PostgreSQL

Script de wrapper para executar uma verificação de integridade do serviço PostgreSQL

Para executar o script pasta passar por paramentro o caminho do do arquivo com as variaveis para se conectart no banco de dados, por exemplo:

```
python3 wait-for-it.py "./config/.env/.env"
```

Variaveis necessarias para se conectar no serviço: DB_IP, DB_NAME, DB_USER, DB_PASSWORD, CMD_APP,CONNECT_TIMEOUT
