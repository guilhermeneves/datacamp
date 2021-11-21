# A Scalable Language

Scala is a general multi-purpose language providing support for functional programming and a strong static type system.

`Scale source code` is intended to be compiled to Java bytecode, so that the resulting executable code run on a `Java Virtual Machine`

Scala is an flexible and adaptable language, so it's not complete, but very adaptable for your requirements.

![](scala_overview.png)


**Spache Spark was Written in Scala**

[**Scala Official Website**](https://www.scala-lang.org/)


Scala fuses OOP and FP more than any language in the world. -> Scala is scalable

- Every value is an object
- Every operation is a method call
- Functions are first-call calues like int, str
- Operations of a program should map input values to output values rathen than change data in place. (functions should have no side effect)

### Why use Scala

- Concise: reduce the lines in 1/10 compared to Java
- High-Level Language: Won't deal with computer detail
- Advanced Static Type System: avoid bug in complex applications
- It's Compatible: Access to huge ecosystems of libraries due to running in a JVM.

### Scala Interpreter

![](scala_int.png)

```
// Calculate the difference between 8 and 5
val difference = 8.-(5)

// Print the difference
println(difference)

```

### Variables

Mutable: `val`
Immutable: `var`

`scala> val fourHearts: Int = 4`

![](types.png)

`String type is a sequence of Char in Scala`

```
// Define immutable variables for clubs 2♣ through 4♣
val twoClubs: Int = 2
val threeClubs: Int = 3
val fourClubs: Int = 4

val PlayeA: String = "Guilherme"

```
![](immut.png)


**Scala have the Type Inference Feature which detects the type of the object and assign it automatically if not declared, it applies to everything: functions, collections, etc...**
```
val FourHearts: Int = 4
// With Type Inference
val Five Hearts = 5

```

```
// Create a mutable variable for Alex as player A
var playerA: String = "Alex"

// Change the point value of A♦ from 1 to 11
aceDiamonds = 11

// Calculate hand value for J♣ and A♦
println(jackClubs + aceDiamonds)

```

![](scala_script.png)