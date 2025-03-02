# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.linear import LinearRegression
from bigml.api import BigML
# Downloads and generates a local version of the linear regression,
# if it hasn't been downloaded previously.
linearregression = LinearRegression('linearregression/67a261991e4fe53008ce3443',
                  api=BigML("carregui",
                            "7180113ca69a8bd041228ddd89594f3cb5b842df",
                            domain="bigml.io"))
# To make predictions fill the desired input_data
# in next line. All fields are compulsory if they don't have
# missing values.
input_data = {
    "rooms": 1,
    "bathroom": 1,
    "lift": "True",
    "terrace": "False",
    "square_meters": 1,
    "real_state": "flat",
    "neighborhood": "Eixample"
}
linearregression.predict(input_data)