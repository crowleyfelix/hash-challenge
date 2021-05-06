# Hash Backend Chalenge

Repository for chalenge based on [this](docs/backend-chalenge.md) doc requirements.

## Requirements
* [docker] >=18.09.6
* [docker-compose] >=1.23.2

## Starting the application

The project uses docker as an engine for the container infrastructure environment and uses docker-compose to manage the container's configuration and i``ntegrations.

Execute the following command to build the environment and start the servers.

```
make build
```

The last output will be a sample of data inserted into database. Use the ids to interact with the API.

## Configuration

Each application loads configurations from environment variables and docker-compose will use the values described in [products/.env](products/.env) and [discounts/.env](discounts/.env) files to apply to containers.

## Resources

### List products

```
# Request
curl "localhost:8081/users/{user_id}/products"
...
# Response
{"limit":1,"offset":0,"data":[{"id":"609345baee6c734cdd6b6063","price_in_cents":1000,"title":"Camiseta Regata","description":"Camiseta Regata","discount":{"percentage":0.05,"value_in_cents":950}}],"error":null}
```



[docker]: https://docs.docker.com/install/
[docker-compose]: https://docs.docker.com/compose/install/