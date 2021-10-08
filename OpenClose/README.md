# Open Closed Principle

## Overview

Open–closed principle states classes, modules, functions etc should be open for extension, but closed for modification
**i.e.** the behaviour can be extended without modifying its source code.

The main benefit of this approach is that an interface introduces an additional level of abstraction which enables loose
coupling. The implementations of an interface are independent of each other and don’t need to share any code. If you
consider it beneficial that two implementations of an interface share some code, you can either use inheritance or
composition.
