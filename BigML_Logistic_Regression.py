# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.logistic import LogisticRegression
from bigml.api import BigML
# Downloads and generates a local version of the logistic regression,
# if it hasn't been downloaded previously.
logisticregression = LogisticRegression('logisticregression/67a261eb54e70fb808f11be9',
                  api=BigML("carregui",
                            "7180113ca69a8bd041228ddd89594f3cb5b842df",
                            domain="bigml.io"))
# To predict probabilities fill the desired input_data
# in next line. Numeric fields are compulsory if the model was not
# trained with missing numerics.
input_data = {
    "price": 1,
    "rooms": 1,
    "bathroom": 1,
    "lift": True,
    "terrace": False,
    "square_meters": 1,
    "real_state": "flat"
}
logisticregression.predict(input_data, full=True)
#
# input_data: dict for the input values
# full: if set to True, the output will be a dictionary that includes the
# distribution of each class in the objective field, the predicted class and
# its probability. Please check:
# https://bigml.readthedocs.io/en/latest/#local-logistic-regression-predictions