# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""BQ ODBC Driver Utility."""
import logging

import click
import pyodbc

from bq_driver_utils.utils import add_click_options

logger = logging.getLogger(__name__)


@click.group()
def odbc():
    """BQ ODBC Driver Utility."""


_CONNECTION_OPTIONS = (
    click.option(
        "--connection-catalog",
        required=True,
        help="The name of your BigQuery project. This project is the "
        "default project that the Simba Google BigQuery ODBC "
        "Connector queries against, and is also the project that is "
        "billed for queries that are run.",
    ),
    click.option(
        "--connection-refresh-token",
        required=True,
        help="The refresh token that you obtain from Google for authorizing access "
        "to BigQuery.",
    ),
    click.option(
        "--connection-client-id",
        required=True,
        help="The Client ID to use when authenticating the connection to BigQuery.",
    ),
    click.option(
        "--connection-client-secret",
        required=True,
        help="The Client Secret to use when authenticating the connection to BigQuery.",
    ),
    click.option(
        "--connection-additional-projects",
        default="",
        help="A comma-separated list of public BigQuery projects that the "
        "connector can access and use as catalogs. These projects "
        "are available as catalogs in metadata functions.",
    ),
)


def _connect(
    catalog,
    refresh_token,
    client_id,
    client_secret,
    additional_projects,
):
    return pyodbc.connect(
        "DRIVER={Simba ODBC Driver for Google BigQuery 64-bit};"
        "OAuthMechanism=1;"
        f"RefreshToken={refresh_token};"
        f"ClientId={client_id};"
        f"ClientSecret={client_secret};"
        f"Catalog={catalog};"
        f"AdditionalProjects={additional_projects};",
        autocommit=True,
    )


@odbc.command()
@add_click_options(_CONNECTION_OPTIONS)
@click.option(
    "--sql-tables-catalog",
    default=None,
    help="Catalog passed to SQLTables metadata function.",
)
def tables(
    connection_catalog,
    connection_refresh_token,
    connection_client_id,
    connection_client_secret,
    connection_additional_projects,
    sql_tables_catalog,
):
    """Call the SQLTables metadata function.

    https://learn.microsoft.com/en-us/sql/odbc/reference/syntax/sqltables-function
    """
    connection = _connect(
        connection_catalog,
        connection_refresh_token,
        connection_client_id,
        connection_client_secret,
        connection_additional_projects,
    )
    cursor = connection.cursor()
    for row in cursor.tables(catalog=sql_tables_catalog):
        logger.info(
            "%s.%s.%s: %s: %s",
            row.table_cat,
            row.table_schem,
            row.table_name,
            row.table_type,
            row.remarks,
        )
