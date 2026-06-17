# context managers

Context Manager are used to
cleanup the resource

```

Acquire Resource
↓
Use Resource
↓
Release Resource

```


### Context Manager Summary

*A context manager can:*

1. Setup resources `(__enter__)`
2. Cleanup resources `(__exit__)`
3. Inspect exceptions `(exc_type, exc_value)`
4. Optionally suppress exceptions `(return True)`
