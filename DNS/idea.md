
url structure: [url].[domain]

Uses python hash() to convert domain, go to that table(load from disk or ram), hash url to get position. go to position in table. hash string backwards, gets find position, load data from there, compare strings, load final table. Return best IP