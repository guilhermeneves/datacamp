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

## Interpreter and Compiled Language

Scala Application must be compiled explicited and run explicited.
Scripts can be executed using scala command and it`ll be interpreted (it`ll be slower than compiled).

Compiled >
- No lag time as application is pre-compiled
- Good for larger applications

```
object Game extends App {
  println("test Game")
}
```

`$scalac Game.scala`

`$scala Game`

Output > test Game

## IDE

You can work with Scala using shell scripting or an IDE, the most preferable IDE for Scala is Intellij IDEA.

## SBT (Simple Build Tool)

Most popular tool for building Scala Application. It compiles, run and test your Scala Application.

## Scala on Jupyter Notebooks

Scala also works on Jupyter Notebooks using Kernel Almond

# Functions

Functions are invoked with a list of arguments to produce a result.

What are the parts of a function?

- Parameter List
- Body
- Result Type

Definition

```
// function body
def bust(hand: Int): Boolean = {
  hand > 21
 }

print(bust(20))
print(bust(21))
print(bust(1+4))
// false
// true
// false
```

**functions in scala can receive other functions as arguments**

# Arrays

## Collections

- Mutable collections
  - can be updated or extended in place
- Immutable collections
  - never change
 
 Array is a mutable sequence of objects that share the same type
 
 `scala> val players = Array("Alex", "Chen", "Marta")`
 OR
 `scala> val players = new Array[String](3)`
 OR
 `scala> val player: Array[String] = new Array[String](3)`
 
 Adding elements to Array:
 ```
 scala> players(0)="Guilherme"
 scala> player(1)="Joao"
 ```
 
 Arrays have order and type defined!
 
 **It`s recommended to use val with Array to be able to update the Array like above, but cannot reassign the variable with a new array like players= new Array[String](5)**
 
 Scala nudges us towards immutability.
 
 **The any supertype**
 `scala> val mixedTypes = new Array[Any](3)`
 `scala> mixedTypes(0) = 1`
 `scala> mixedTypes(1)="Teste"`
 
 ```
 // Initialize player's hand and print out hands before each player hits
hands(0) = tenClubs + fourDiamonds
hands(1) = nineSpades + nineHearts
hands(2) = twoClubs + threeSpades
hands.foreach(println)

// Add 5♣ to the first player's hand
hands(0) = hands(0) + fiveClubs

// Add Q♠ to the second player's hand
hands(1)  = hands(1)  + queenSpades

// Add K♣ to the third player's hand
hands(2)  = hands(2)  + kingClubs

// Print out hands after each player hits
hands.foreach(println)
 
 ```
