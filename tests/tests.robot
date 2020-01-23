*** Settings ***

Library    ../src/SQLess/SQLessKeywords.py    schema.yml

*** Test Cases ***

Test Get All By Table Identifier
    ${users}   Get All    Users
    Length Should Be    ${users}    3

Test Get By Filter
    ${users}   Get By Filter    Users    email=someothername@someotherdomain.tld
    Length Should Be    ${users}    1

Test Get By Multiple Filters
    ${users}   Get By Filter    Users    username=TestUser1    failed_logins=0
    Length Should Be    ${users}    1

Test Get By Multiple Filters Negative
    ${users}   Get By Filter    Users    username=TestUser1    failed_logins=1
    Length Should Be    ${users}    0

Test Get By Filter Returned Value
    ${users}   Get By Filter    Users    email=someothername@someotherdomain.tld
    Should Be Equal    ${users[0]['username']}    TestUser2

Test Get By Raw Query
    ${query}    Set Variable    SELECT id, username, email, failed_logins FROM user;
    ${result}    Execute SQL    ${query}
    Length Should Be    ${result}    3
