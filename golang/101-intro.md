## About Me

* Imam Kurniawan [Software Engineer - Digital - Service Delivery]
* Bina Nusantara University (2001)
* Join Indosat Ooredoo July 2019
* Use Golang for about 1+ year (since July 2019)

---

## What is Golang?

* Golang is a statically typed, high performance, and simple language
* Golang is designed at Google by Robert Griesemer, Rob Pike, and Ken Thompson
* Born out of easy to use programming language with type safety and portabiliy
* Similar to C Programming Language with mostly simplified syntax (no semi-colon, etc.)

---

## Why Golang?

**Simplicity**
* Readability and maintainability is its priority
* Simple visibily control only by upper/lower case of first letter of the identifier
* Fewer typing with considerably simpler syntax
* Simpler programming for large and scalable servers and software systems
* Not OOP
* Functional

---

## Why Golang? (cont.)

**Powerfull Standard Library**
* Has a rich set of library packages
* Has all the essential stuffs
* https://golang.org/pkg/

---

## Why Golang? (cont.)

**Speed**
* Fast compilation to native
* Fast execution
* Portability with single codebase for cross-platform

---

## Why Golang? (cont.)

**Concurrency**
* Was conceived at a time when multi-core processors became widely available across sophisticated hardware
* Easier and cheaper to build and maintain with goroutines (4KB each) than threads (java 1MB each)
* Savely share data among goroutines with channels
* Faster context switching with its own scheduler (not OS kernel to schedule)

---

## Language Design & Syntaxes

* Use `var` when declaring variables, there is also a short way of declaration with `:=`
* Compiler error when something _not used_
* Function as **first-class** citizen
* Package based orginization instead of file/class based
* Basic data types such as `string`,`float32`,`float64`,`int`,`int[8|16|32|64]`,`byte`,etc.
* Can perform type alias via keyword `type` (`byte` is example of a built-in type alias of `int8`)
* Six kinds of source-code **elements** which can be declared such as 
  - package imports
  - defined types and type alias
  - named constants
  - variables
  - functions
  - labels 
* Support local-scoped and closure

---

## Live Code

* Via https://play.golang.org