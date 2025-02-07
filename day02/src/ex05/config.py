NUM_OF_STEPS = 3

REPORT = """\
Report

We have made {observations} observations from tossing a coin: {tails} of \
them were tails and {heads} of them were heads. The probabilities are \
{tail_fraction:.2f}% and {head_fraction:.2f}%, respectively. Our forecast \
is that in the next {predictions} observations we will have: \
{predicted_tails} tail and {predicted_heads} heads.\
"""