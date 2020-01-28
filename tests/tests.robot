*** Settings ***

Library    SQLess    tests/schema.yml

*** Test Cases ***

Get By Raw Query
    [Tags]    sqlite
    ${query}    Set Variable    SELECT id, username, email, failed_logins FROM user;
    ${result}    Execute SQL String    ${query}
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
    ${posts}   Get By Filter    Posts    content=hello, world!
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

Delete All
    [Tags]    all_dbms
    Delete All    Posts
    ${amount}    Count    Posts
    Should Be Equal As Strings    ${amount}    0

Delete By Filter
    [Tags]    all_dbms
    Delete By Filter    Users    username=TestUser3
    ${amount}    Count    Users
    Should Be Equal As Strings    ${amount}    3

Update All
    [Tags]    all_dbms
    Given Song Is Not In Collection
    When All Songs Are Updated
    Then Song Is In Collection

Update By Filter
    [Tags]    all_dbms
    Given Songs Have Incomplete Album Name
    When Album Names Are Updated
    Then Songs Have Complete Album Name

Update By Filter From Selected Rows
    [Tags]    all_dbms
    ${songs}    Given Songs Have Wrong Artist Name
    When Songs Are Update From Previous Select    ${songs}
    Then Songs Have Correct Artist Names

*** Keywords ***
Song Is Not In Collection
    ${song}   Get By Filter    Songs    artist=Sirenia
    Should Not Be True    ${song[0]['in_collection']}

When All Songs Are Updated
    Update All    Songs    in_collection=True

Song Is In Collection
    ${song}   Get By Filter    Songs    artist=Sirenia
    Should Be True    ${song[0]['in_collection']}

Songs Have Incomplete Album Name
    ${song}    Get By Filter    Songs    artist=Nightwish
    Should Be Equal    ${song[0]['album']}    Decades
    Should Be Equal    ${song[1]['album']}    Decades
    Should Be Equal    ${song[2]['album']}    Decades

Album Names Are Updated
    ${filter}    Create Dictionary    artist=Nightwish
    Update By Filter    Songs    ${filter}    album=Decades: Live in Buenos Aires

Songs Have Complete Album Name
    ${song}    Get By Filter    Songs    artist=Nightwish
    Should Be Equal    ${song[0]['album']}    Decades: Live in Buenos Aires
    Should Be Equal    ${song[1]['album']}    Decades: Live in Buenos Aires
    Should Be Equal    ${song[2]['album']}    Decades: Live in Buenos Aires

Given Songs Have Wrong Artist Name
    ${songs}   Get By Filter    Songs    album=Sons Of Northern Darkness
    Should Be Equal    ${songs[0]['artist']}    Immortal_
    Should Be Equal    ${songs[1]['artist']}    Immortal_
    [Returns]    ${songs}

When Songs Are Update From Previous Select
    [Arguments]    ${songs}
    Update By Filter    Songs    ${songs}    artist=Immortal

Then Songs Have Correct Artist Names
    ${songs}   Get By Filter    Songs    album=Sons Of Northern Darkness
    Should Be Equal    ${songs[0]['artist']}    Immortal
    Should Be Equal    ${songs[1]['artist']}    Immortal
