![Robot Tests](https://github.com/eternalconcert/robotframework-sqless/workflows/Robot%20Tests/badge.svg?branch=master)

# Robot Framework - SQLess

``robotframework-sqless`` is a  SQL abstraction library for [Robot Framework](https://robotframework.org/)

## Usage

```bash
pip install robotframework-sqless
```

## Example testcase
|                     |                           |                     |                     |                       |
| ----------------    | --------------------------| ------------------- | ------------------- | --------------------- |
| *** Settings ***    |                           |                     |                     |                       |
| Library             | SQLess                    | schema.yml          | db_config.yml       |                       |
| *** Test Cases ***  |                           |                     |                     |                       |
| Get Users By Filter |                           |                     |                     |                       |
|                     | ${users}                  | Get By Filter       | Users               | username=TestUser     |
|                     | Length Should Be          | ${users}            | 1                   |                       |

The example presumes there is a database with a user table and at least a column `username`.

## Schema definition
The database schema and the database configuration must be defined in separate .yml files. For the above example, the following files should apply:

db_config.yml
```yaml
dbms: sqlite
db: sqless.db
```

schema.yml
```yaml
users:
  tablename: user
  fields:
    id: integer
    username: char
```
