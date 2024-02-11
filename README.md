# Installation

## Create Docker Image:

When working with MacM1, in order to create an Image to be run locally use:

        docker build -t myfastapiapp .


When working with MacM1, in order to create an Image to be run on X86_64 processors use:

        docker build -t myfastapiapp .


## Run container, exposing api endpoint at local `localhost:8000`:

        docker run -d --name myfastapiapp -p 8000:8000 myfastapiapp

## Test Api endpoint:

        curl -X POST \
            "http://localhost:8000/classify-image/" \
            -F "file=@test/data/bus.jpeg"
