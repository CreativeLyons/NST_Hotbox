#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle turbulance/fBm
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    knob = n.knob('type')
    currentState = knob.getValue()
    newState = abs(currentState-1)
    if newState == 0:
        knob.setValue('fBm')
    else:
        knob.setValue('turbulance')
