*** Settings ***

Library    SQLess    schema.yml

*** Test Cases ***

Get By Raw Query
    [Tags]    sqlite
    ${query}    Set Variable    SELECT id, username, email, failed_logins FROM user;
    ${result}    Execute SQL    ${query}
    Length Should Be    ${result}    3

Get All By Table Identifier
    [Tags]    all_dbms
    ${users}   Get All    Users
    Length Should Be    ${users}    3

Get From Mutiple Tables
    [Tags]    all_dbms
    ${users}   Get All    Users
    Length Should Be    ${users}    3
    ${posts}   Get All    Posts
    Length Should Be    ${posts}    2

Get From Mutiple Tables By Filter
    [Tags]    all_dbms
    ${users}   Get By Filter    Users    email=someothername@someotherdomain.tld
    Length Should Be    ${users}    1
    ${posts}   Get By Filter    Posts    user=2
    Length Should Be    ${posts}    1

Get By Filter
    [Tags]    all_dbms
    ${users}   Get By Filter    Users    email=someothername@someotherdomain.tld
    Length Should Be    ${users}    1

Get By Blank Filter
  [Tags]    all_dbms
  ${users_blank_filter}   Get By Filter    Users
  ${users_all}   Get All    Users
  Should Be Equal    ${users_blank_filter}    ${users_all}

Get By Multiple Filters
    [Tags]    all_dbms
    ${users}   Get By Filter    Users    username=TestUser1    failed_logins=0
    Length Should Be    ${users}    1

Get By Multiple Filters Negative
    [Tags]    all_dbms
    ${users}   Get By Filter    Users    username=TestUser1    failed_logins=1
    Length Should Be    ${users}    0

Get By Filter Returned Value
    [Tags]    all_dbms
    ${users}   Get By Filter    Users    email=someothername@someotherdomain.tld
    Should Be Equal    ${users[0]['username']}    TestUser2

Create
    [Tags]    all_dbms
    ${user}   Create    Users    username=AnotherUser    email=name@domain.tld
    Should Be Equal    ${user['email']}    name@domain.tld

Count All
    [Tags]    all_dbms
    ${amount}    Count    Users
    Should Be Equal As Strings    ${amount}    4

Count Filtered
    [Tags]    all_dbms
    ${amount}    Count    Users    username=TestUser2
    Should Be Equal As Strings    ${amount}    1
