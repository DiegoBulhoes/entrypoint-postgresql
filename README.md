# Entrypoint PostgreSQL

Script de wrapper para executar uma verificação de integridade do serviço PostgreSQL

Para executar o script pasta passar por parâmetro o caminho do do arquivo com as variáveis para se conectar no banco de dados, por exemplo:

```
python3 wait-for-it.py "./.env/.env"
```

Variaveis necessarias para se conectar no serviço: DB_IP, DB_NAME, DB_USER, DB_PASSWORD, CMD_APP,CONNECT_TIMEOUT, [segue um exemplo de um .env](https://github.com/DiegoBulhoes/entrypoint-postgresql/blob/master/.env/.env.example)
