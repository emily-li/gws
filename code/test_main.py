from brian import *
from model import *
from synapses import *
from test import *

testIneuro(120,100)

single_neuron = createNeuronGroup(1)

gSRA_inc = 0.01 * msiemens

#7
#After each spike, the conductance gSRA is increased by a small quantity (here 0.01 * mS), 2005
ISRA_S = Synapses(single_neuron, pre='''gSRA += gSRA_inc''')
					

ISRA_S[:,:] = True
