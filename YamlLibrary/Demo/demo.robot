*** Settings ***
Library                         ../YamlLibrary/YamlLibrary.py
Library                         OperatingSystem


*** Variables ***
${yamlfile}     demo.yaml

*** Test Cases ***
YAML_TESTING
    ${TmpYamlStr}    Get File    ${yamlfile}
    ${Name}    Get Tree    ${TmpYamlStr}    Demo.Key1[0]
    Log To Console      ${Name}
    ${Name}    Get Tree    ${TmpYamlStr}    Demo.Key2
    Log To Console      ${Name}
