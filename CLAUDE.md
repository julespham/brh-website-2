# CLAUDE.md

## Overview

* a static web site generator which converts a series of templates and content and generates a directory of html, js and css that fully represents the web site of the Boston Robot Hackers

## Key Technical Directives

* Use uv for package management not pip. Only use UV
* We use markdown for much of the user supplied content
* Look for and eliminate duplicate code or css
* There should almost never be css or js inside an html file
* Templates represent different types of page on the web site
* Themes represent different styles used to render the web site
* Github actions are used to produce and github page hosted web site

## Key Coding Style REquirements

* Code in python
* Always look for a well supported package to implement a feature
* Look for and eliminate duplicate code
* Use python classes where apporpriate
* No methods or functions longer than 35 lines
* No source files longer than 400 lines


