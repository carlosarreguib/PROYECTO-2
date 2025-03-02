# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.deepnet import Deepnet
from bigml.api import BigML
# Downloads and generates a local version of the DEEPNET,
# if it hasn't been downloaded previously.
deepnet = Deepnet('deepnet/67a261ef7e6b0ebd374d1989',
                  api=BigML("carregui",
                            "7180113ca69a8bd041228ddd89594f3cb5b842df",
                            domain="bigml.io"))
# To make predictions fill the desired input_data in next line.
input_data = {
    "rooms": 1,
    "bathroom": 1,
    "lift": "True",
    "terrace": "False",
    "square_meters": 1,
    "real_state": "flat",
    "neighborhood": "Eixample"
}
deepnet.predict(input_data, full=True)
#
# input_data: dict for the input values
# full: if set to True, the output will be a dictionary that includes all the
# available information about the prediction. The attributes vary depending
# on the ensemble type. Please check:
# https://bigml.readthedocs.io/en/latest/#local-deepnet-predictions