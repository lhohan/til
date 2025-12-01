+++
title = "Option::map vs Option::and_then"
date = 2024-11-18
[taxonomies]
topics = ["rust"]
+++

Both transform `Option` values, but they differ in what the closure returns:

**`map`**: Closure returns a value `T`, result is wrapped in `Some`

```rust
let x: Option<i32> = Some(2);
let y = x.map(|n| n * 2);  // Some(4)
```

**`and_then`**: Closure returns an `Option<T>`, result is flattened

```rust
fn checked_double(n: i32) -> Option<i32> {
    n.checked_mul(2)
}

let x: Option<i32> = Some(2);
let y = x.and_then(checked_double);  // Some(4)
```

Use `and_then` when chaining operations that might fail:

```rust
let result = get_user(id)
    .and_then(|u| get_profile(u.profile_id))
    .and_then(|p| get_avatar(p.avatar_id));
```

Think of `and_then` as flatMap from other languages.
