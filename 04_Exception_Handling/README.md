# 04: Exception Handling

Exception handling is a crucial aspect of programming that allows us to gracefully manage errors and unexpected situations that may occur during the execution of our code. In this week's topic, we delve into exception handling mechanisms in Python.

## Try-Except Statement:

The `try-except` statement allows us to handle exceptions (errors) that occur within a block of code. We enclose the code that may raise an exception within a `try` block, and specify how to handle the exception(s) in the corresponding `except` block.

### Key Concepts:
- **Handling Specific Exceptions**: We can specify different `except` blocks to handle specific types of exceptions, allowing for tailored error handling.
- **Multiple Except Blocks**: Multiple `except` blocks can be used to handle different types of exceptions that may arise.

## Finally Block:

The `finally` block is used to execute code regardless of whether an exception occurred or not. It is commonly used for cleanup tasks, such as closing files or releasing resources, ensuring that certain actions are always performed.

### Key Concepts:
- **Resource Cleanup**: The `finally` block is especially useful for ensuring that resources are properly released, even if an exception occurs during execution.
- **Guaranteed Execution**: Code in the `finally` block is guaranteed to execute, providing a reliable mechanism for cleanup tasks.

## Combining Try-Except-Finally:

By combining the `try-except` and `finally` blocks, we can handle exceptions gracefully while ensuring that necessary cleanup actions are always performed, regardless of whether an exception occurred.
