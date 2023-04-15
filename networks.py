import pypsa
network=pypsa.Network()
nbus=5
for i in range(nbus):
    network.add("Bus","Bus No{}".format(i),v_nom=132)
network.buses
for i in range(nbus-1):
    network.add("Line","Line No{}".format(i),bus0="Bus No{}".format(i),bus1="Bus No{}".format(i+1),r=0.02,x=0.3)
network.lines
network.add("Generator","slack Gen",bus="Bus No 0",p_set=0,control="slack")
network.add("Generator"," Gen No 1",bus="Bus No 3",p_set=60,q_set=90,control="PV")
network.generators
network.add("Load"," Load No 1",bus="Bus No 4",p_set=90,q_set=40)
network.loads