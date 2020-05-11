# Weeb image classifier

## Model Installation
Head over to our [release page](https://github.com/weeb-purger/nn-classifier/releases), and download the latest model.

`tar xf weeb_model-003.tar.gz /tmp/weeb_model`

## Python package installation
`pip install git+https://github.com/weeb-purger/nn-classifier.git`

## How to use
```
> weeb -h                                                                                                                                                                                           
usage: weeb [-h] [--separator SEPARATOR] [--confidence-level CONFIDENCE_LEVEL] I [I ...]

positional arguments:
  I                     One or more images to test.

optional arguments:
  -h, --help            show this help message and exit
  --separator SEPARATOR
                        Separator between output results (applicable if testing multiple images), defaults to ' '.
  --confidence-level CONFIDENCE_LEVEL
                        Only deem a picture weeby if confidence level is over this value. Defaults to 500
```

### Example usage
```
> weeb --separator ';' another-weeb.png not-weeb-1.png                                                                                                                                             1;0
```
### Training the model yourself

Set the environment variables `TRAINING_DIR` and `VALIDATION_DIR`.

Where the training directory and validation directory both should include two sub folders titled weeb and not weeb respectively.

The model in the release page was trained on roughly 35000 weeb pictures and 36000 non-weeb pictures.

`> weeb-train`
