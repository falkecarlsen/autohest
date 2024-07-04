# autohest
Markov chain generator fed [heste-nettet](https://www.heste-nettet.dk/).

First unpack the corpus in `hest.zip.part-*` into a directory `./hest/`.

Meant for interactive use:
```sh
$ source venv/bin/activate.fish
$ python
exec(open('./markov.py').read())
model.make_sentence()
model_make_sentence_with_start("Min hest er")
```

## License for `hest.zip`
`hest.zip` is derived of following work: Danish Gigaword Corpus: [license](https://creativecommons.org/licenses/by/4.0/) - [homepage](https://gigaword.dk/)
