# 0x01. Python - Async

## Python Back-end

- Weight: 1
- Project duration: Oct 14, 2024 6:00 AM - Oct 15, 2024 6:00 AM

## Resources
Read or watch:
- Async IO in Python: A Complete Walkthrough
- asyncio - Asynchronous I/O
- random.uniform

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- async and await syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module

## Requirements

### General
- A README.md file, at the root of the folder of the project, is mandatory
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- All your files must be executable
- The length of your files will be tested using wc
- The first line of all your files should be exactly #!/usr/bin/env python3
- Your code should use the pycodestyle style (version 2.5.x)
- All your functions and coroutines must be type-annotated
- All your modules should have a documentation
- All your functions should have a documentation
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method

## Tasks

### 0. The basics of async
- Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random
- The coroutine should wait for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it
- Use the random module

Example:

#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

