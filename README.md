# rust-test-bench

Just a test case showing that cargo test does not run integration tests in parallel.

```
cargo test -- --test-threads=100
```
Should have take around 1 second, but takes 10s.
