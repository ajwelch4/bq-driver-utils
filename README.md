# BigQuery Driver Utils

## Install

```shell
git clone git@github.com:ajwelch4/bq-driver-utils.git
cd bq-driver-utils
poetry install
```

## Generate Client ID and Client Secret

[https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)

## Generate Refresh Token

[https://developers.google.com/oauthplayground](https://developers.google.com/oauthplayground)

## ODBC

### SQLTables

[https://learn.microsoft.com/en-us/sql/odbc/reference/syntax/sqltables-function](https://learn.microsoft.com/en-us/sql/odbc/reference/syntax/sqltables-function)

<!-- markdownlint-disable -->
```shell
bq-driver odbc tables \
  --connection-catalog "bqms-055" \
  --connection-refresh-token "<REFRESH_TOKEN>" \
  --connection-client-id "<CLIENT_ID>" \
  --connection-client-secret "<CLIENT_SECRET>"
  
2024-02-14 19:47:24,400: INFO: MainThread: bqms-055.bqdw.Customer: TABLE: bqms-055
2024-02-14 19:47:24,400: INFO: MainThread: bqms-055.bqdw.CustomerAgg: TABLE: bqms-055
2024-02-14 19:47:24,401: INFO: MainThread: bqms-055.bqdw.SalesOrderDetail: TABLE: bqms-055
2024-02-14 19:47:24,401: INFO: MainThread: bqms-055.bqdw.SalesOrderHeader: TABLE: bqms-055
2024-02-14 19:47:24,401: INFO: MainThread: bqms-055.bqdw.SalesOrderHeaderSalesReason: TABLE: bqms-055
2024-02-14 19:47:24,401: INFO: MainThread: bqms-055.bqdw.Store: TABLE: bqms-055
```
<!-- markdownlint-enable -->

### SQLTables Pattern Value Catalog Argument

[https://learn.microsoft.com/en-us/sql/odbc/reference/develop-app/pattern-value-arguments](https://learn.microsoft.com/en-us/sql/odbc/reference/develop-app/pattern-value-arguments)

<!-- markdownlint-disable -->
```shell
bq-driver odbc tables \
  --connection-catalog "bqms-055" \
  --connection-refresh-token "<REFRESH_TOKEN>" \
  --connection-client-id "<CLIENT_ID>" \
  --connection-client-secret "<CLIENT_SECRET>" \
  --sql-tables-catalog-name "%"

2024-02-14 19:48:36,296: INFO: MainThread: infa-413503.bqdw.customer: TABLE: infa-413503
2024-02-14 19:48:36,297: INFO: MainThread: infa-413503.bqdw.salesorderdetail: TABLE: infa-413503
2024-02-14 19:48:36,297: INFO: MainThread: infa-413503.bqdw.salesorderheader: TABLE: infa-413503
2024-02-14 19:48:36,297: INFO: MainThread: infa-413503.bqdw.salesorderheadersalesreason: TABLE: infa-413503
2024-02-14 19:48:36,297: INFO: MainThread: infa-413503.bqdw.store: TABLE: infa-413503
2024-02-14 19:48:36,455: INFO: MainThread: pipelines-377521.foo_bar.customers: TABLE: pipelines-377521
2024-02-14 19:48:36,456: INFO: MainThread: pipelines-377521.foo_bar.orders: TABLE: pipelines-377521
2024-02-14 19:48:36,722: INFO: MainThread: dvt-demo-371714.load_test.metrics: TABLE: dvt-demo-371714
2024-02-14 19:48:36,723: INFO: MainThread: dvt-demo-371714.load_test.results: TABLE: dvt-demo-371714
2024-02-14 19:48:36,879: INFO: MainThread: bqms-055.bqdw.Customer: TABLE: bqms-055
2024-02-14 19:48:36,880: INFO: MainThread: bqms-055.bqdw.CustomerAgg: TABLE: bqms-055
2024-02-14 19:48:36,880: INFO: MainThread: bqms-055.bqdw.SalesOrderDetail: TABLE: bqms-055
2024-02-14 19:48:36,880: INFO: MainThread: bqms-055.bqdw.SalesOrderHeader: TABLE: bqms-055
2024-02-14 19:48:36,880: INFO: MainThread: bqms-055.bqdw.SalesOrderHeaderSalesReason: TABLE: bqms-055
2024-02-14 19:48:36,880: INFO: MainThread: bqms-055.bqdw.Store: TABLE: bqms-055

```
<!-- markdownlint-enable -->

### SQLTables Additional Projects

<!-- markdownlint-disable -->
```shell
bq-driver odbc tables \
  --connection-catalog "bqms-055" \
  --connection-refresh-token "<REFRESH_TOKEN>" \
  --connection-client-id "<CLIENT_ID>" \
  --connection-client-secret "<CLIENT_SECRET>" \
  --connection-additional-projects "bigquery-public-data"

2024-02-14 19:49:31,707: INFO: MainThread: bqms-055.bqdw.Customer: TABLE: bqms-055
2024-02-14 19:49:31,708: INFO: MainThread: bqms-055.bqdw.CustomerAgg: TABLE: bqms-055
2024-02-14 19:49:31,708: INFO: MainThread: bqms-055.bqdw.SalesOrderDetail: TABLE: bqms-055
2024-02-14 19:49:31,708: INFO: MainThread: bqms-055.bqdw.SalesOrderHeader: TABLE: bqms-055
2024-02-14 19:49:31,708: INFO: MainThread: bqms-055.bqdw.SalesOrderHeaderSalesReason: TABLE: bqms-055
2024-02-14 19:49:31,708: INFO: MainThread: bqms-055.bqdw.Store: TABLE: bqms-055

```
<!-- markdownlint-enable -->

### SQLTables Additional Projects with Pattern Value Catalog Argument

<!-- markdownlint-disable -->
```shell
bq-driver odbc tables \
  --connection-catalog "bqms-055" \
  --connection-refresh-token "<REFRESH_TOKEN>" \
  --connection-client-id "<CLIENT_ID>" \
  --connection-client-secret "<CLIENT_SECRET>" \
  --connection-additional-projects "bigquery-public-data" \
  --sql-tables-catalog-name "%"

2024-02-14 19:51:11,538: INFO: MainThread: infa-413503.bqdw.customer: TABLE: infa-413503
2024-02-14 19:51:11,538: INFO: MainThread: infa-413503.bqdw.salesorderdetail: TABLE: infa-413503
2024-02-14 19:51:11,538: INFO: MainThread: infa-413503.bqdw.salesorderheader: TABLE: infa-413503
2024-02-14 19:51:11,538: INFO: MainThread: infa-413503.bqdw.salesorderheadersalesreason: TABLE: infa-413503
2024-02-14 19:51:11,538: INFO: MainThread: infa-413503.bqdw.store: TABLE: infa-413503
2024-02-14 19:51:11,668: INFO: MainThread: pipelines-377521.foo_bar.customers: TABLE: pipelines-377521
2024-02-14 19:51:11,668: INFO: MainThread: pipelines-377521.foo_bar.orders: TABLE: pipelines-377521
2024-02-14 19:51:11,834: INFO: MainThread: dvt-demo-371714.load_test.metrics: TABLE: dvt-demo-371714
2024-02-14 19:51:11,834: INFO: MainThread: dvt-demo-371714.load_test.results: TABLE: dvt-demo-371714
2024-02-14 19:51:11,948: INFO: MainThread: bqms-055.bqdw.Customer: TABLE: bqms-055
2024-02-14 19:51:11,949: INFO: MainThread: bqms-055.bqdw.CustomerAgg: TABLE: bqms-055
2024-02-14 19:51:11,949: INFO: MainThread: bqms-055.bqdw.SalesOrderDetail: TABLE: bqms-055
2024-02-14 19:51:11,949: INFO: MainThread: bqms-055.bqdw.SalesOrderHeader: TABLE: bqms-055
2024-02-14 19:51:11,949: INFO: MainThread: bqms-055.bqdw.SalesOrderHeaderSalesReason: TABLE: bqms-055
2024-02-14 19:51:11,949: INFO: MainThread: bqms-055.bqdw.Store: TABLE: bqms-055
2024-02-14 19:51:12,880: INFO: MainThread: bigquery-public-data.america_health_rankings.ahr: TABLE: bigquery-public-data
2024-02-14 19:51:12,881: INFO: MainThread: bigquery-public-data.america_health_rankings.america_health_rankings: TABLE: bigquery-public-data
2024-02-14 19:51:12,891: INFO: MainThread: bigquery-public-data.austin_311.311_service_requests: TABLE: bigquery-public-data
2024-02-14 19:51:12,913: INFO: MainThread: bigquery-public-data.austin_bikeshare.bikeshare_stations: TABLE: bigquery-public-data
2024-02-14 19:51:12,913: INFO: MainThread: bigquery-public-data.austin_bikeshare.bikeshare_trips: TABLE: bigquery-public-data
2024-02-14 19:51:12,913: INFO: MainThread: bigquery-public-data.austin_crime.crime: TABLE: bigquery-public-data
2024-02-14 19:51:12,913: INFO: MainThread: bigquery-public-data.austin_incidents.incidents_2008: TABLE: bigquery-public-data
2024-02-14 19:51:12,914: INFO: MainThread: bigquery-public-data.austin_incidents.incidents_2009: TABLE: bigquery-public-data
...
```
<!-- markdownlint-enable -->