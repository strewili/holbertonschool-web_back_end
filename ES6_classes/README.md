# ES6 classes

Classes in ES6: defining them, getters and setters, static methods,
inheritance, abstract classes, and the well-known symbols that let a class
control how it is cast to a primitive or cloned.

## Learning objectives

- How to define a class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

## Requirements

- Ubuntu 20.04 LTS, node 20.x.x, npm 9.x.x
- All files use the `.js` extension and end with a new line
- Code is tested with Jest and linted with ESLint (airbnb-base)
- All classes must be exported

## Setup

```
npm install
npm run dev 0-main.js
npm run test
npm run check-lint
```

## Files

| File | Description |
| --- | --- |
| `0-classroom.js` | `ClassRoom` — a first class |
| `1-make_classrooms.js` | `initializeRooms()` — builds three classrooms |
| `2-hbtn_course.js` | `HolbertonCourse` — getters, setters, type checks |
| `3-currency.js` | `Currency` — a method returning a formatted string |
| `4-pricing.js` | `Pricing` — composition plus a static method |
| `5-building.js` | `Building` — abstract class enforcing an override |
| `6-sky_high.js` | `SkyHighBuilding` — inheritance with `super` |
| `7-airport.js` | `Airport` — `Symbol.toStringTag` |
| `8-hbtn_class.js` | `HolbertonClass` — `valueOf` and `toString` casting |
| `9-hoisting.js` | Fixing hoisting and scope mistakes |
| `10-car.js` | `Car` — cloning with `Symbol.species` |
