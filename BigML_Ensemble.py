# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.ensemble import Ensemble
# Downloads and generates a local version of the ensemble, if it
# hasn't been downloaded previously.
from bigml.api import BigML
ensemble = Ensemble('ensemble/67a261271e4fe53008ce343e',
                    api=BigML("carregui",
                              "7180113ca69a8bd041228ddd89594f3cb5b842df",
                              domain="bigml.io"))
# To make predictions fill the desired input_data in next line.
input_data = {}
ensemble.predict(input_data, full=True)
#
# input_data: dict for the input values
# full: if set to True, the output will be a dictionary that includes all the
# available information in the predicted node. The attributes vary depending
# on the ensemble type. Please check:
# https://bigml.readthedocs.io/en/latest/#local-ensemble-s-predictions