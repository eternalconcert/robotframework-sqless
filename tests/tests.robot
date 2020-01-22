*** Settings ***

Library    ../src/SQLess/SQLessKeywords.py    schema.yml

*** Test Cases ***

Test Get All By Table Identifier
    ${users}   Get All    Users
    Length Should Be    ${users}    2

Test Get By Filter
    ${users}   Filter    Users    email=someothername@someotherdomain.tld
    Length Should Be    ${users}    1
