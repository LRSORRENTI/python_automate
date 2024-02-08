# Lists Recap:

- Strings can do many of the things lists can do, but strings are immutable

- Immutable values like strings and tuples can never be modified "in place"

- Mutable values like lists can be modified in place

- Variables don't contain lists, they contain references to lists, which when modified does mutate the original list

- You can use copy.deepcopy to create a copy of a list without creating the reference to the original list

- When passing a list argument to a function, you're actually passing in a reference to the list

- Changes made to a list inside of a function body DOES affect the list outside of the function scope

- The \ can be used for line continuation when needing to structure large code blocks for better readability
