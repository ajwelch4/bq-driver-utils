# BigQuery Driver Utils

## Generate Client ID and Client Secret

[https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)

## Generate Refresh Token

[https://developers.google.com/oauthplayground](https://developers.google.com/oauthplayground)

## ODBC

<!-- markdownlint-disable -->
```shell
bq-driver odbc tables \
  --connection-catalog "bqms-055" \
  --connection-refresh-token "<REFRESH_TOKEN>" \
  --connection-client-id "<CLIENT_ID>" \
  --connection-client-secret "<CLIENT_SECRET>"
```
<!-- markdownlint-enable -->

<!-- markdownlint-disable -->
```shell
bq-driver odbc tables \
  --connection-catalog "bqms-055" \
  --connection-refresh-token "<REFRESH_TOKEN>" \
  --connection-client-id "<CLIENT_ID>" \
  --connection-client-secret "<CLIENT_SECRET>" \
  --sql-tables-catalog "%"
```
<!-- markdownlint-enable -->

<!-- markdownlint-disable -->
```shell
bq-driver odbc tables \
  --connection-catalog "bqms-055" \
  --connection-refresh-token "<REFRESH_TOKEN>" \
  --connection-client-id "<CLIENT_ID>" \
  --connection-client-secret "<CLIENT_SECRET>" \
  --connection-additional-projects "bigquery-public-data"
```
<!-- markdownlint-enable -->

<!-- markdownlint-disable -->
```shell
bq-driver odbc tables \
  --connection-catalog "bqms-055" \
  --connection-refresh-token "<REFRESH_TOKEN>" \
  --connection-client-id "<CLIENT_ID>" \
  --connection-client-secret "<CLIENT_SECRET>" \
  --connection-additional-projects "bigquery-public-data" \
  --sql-tables-catalog "%"
```
<!-- markdownlint-enable -->