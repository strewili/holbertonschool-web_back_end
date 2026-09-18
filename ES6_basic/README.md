# ES6 Basics

The features ES6 (ECMAScript 2015) added to JavaScript: block-scoped `const`
and `let`, arrow functions, default and rest parameters, spread syntax,
template literals, object shorthand and computed property names, method
properties, and `for...of` loops.

## Learning objectives

- What ES6 is and what new features it introduced
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameter defaults
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and `for...of` loops

## Requirements

- Ubuntu 20.04 LTS, node 20.x.x, npm 9.x.x
- All files use the `.js` extension and end with a new line
- Code is tested with Jest and linted with ESLint (airbnb-base)
- All functions must be exported

## Setup

```
npm install
npm run dev 0-main.js     # run a file
npm run test              # run the tests
npm run check-lint        # lint
```

## Files

| File | Description |
| --- | --- |
| `0-constants.js` | `const` vs `let` |
| `1-block-scoped.js` | Block scope instead of hoisted `var` |
| `2-arrow.js` | Arrow function keeping `this` |
| `3-default-parameter.js` | Default parameter values |
| `4-rest-parameter.js` | Rest parameter syntax |
| `5-spread-operator.js` | Spread syntax on arrays and strings |
| `6-string-interpolation.js` | Template literals |
| `7-getBudgetObject.js` | Object property shorthand |
| `8-getBudgetCurrentYear.js` | Computed property names |
| `9-getFullBudget.js` | ES6 method properties |
| `10-loops.js` | `for...of` loops |
| `11-createEmployeesObject.js` | Building an object from arguments |
| `12-createReportObject.js` | Spread plus a method property |
