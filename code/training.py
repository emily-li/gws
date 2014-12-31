from brian import *
import brian_no_units
from network import *
import model, stimuli, synapses

for each_train in training:
	for system_i in xrange(len(modules)):
		reward_signal(each_train[0], each_train[1])

n = Network(modules)
n.run(1*second)