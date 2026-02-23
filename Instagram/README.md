# Instagram Similar Accounts Crawler

Fetches accounts similar to a given Instagram username via the [RocketAPI](https://rocketapi.io/).

## Usage

Edit `TARGET_USERNAME` and `API_KEY` in `test.py`, then run:

```sh
uv run test.py > out
```

Results are dumped as JSON to `out`.

## Dependencies

- `requests`
