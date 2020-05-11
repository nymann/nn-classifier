# Weeb image classifier
### Installation
`git clone https://github.com/weeb-purger/nn/classifier`
`cd nn-classifier`
`python3 setup.py install`

### Run
Model is stored in `/tmp/weeb_model`, instead of training the model yourself download it from: https://github.com/weeb-purger/nn-classifier/releases/tag/0.0.1

`weeb image.png` trains the neural network if no model found in `/tmp/weeb_model`.

`weeb-train` trains the neural network if no model found in `/tmp/weeb_model`.
