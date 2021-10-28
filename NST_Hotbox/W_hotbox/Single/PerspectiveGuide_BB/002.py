#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle Horizon
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    knob = n.knob('horizon')
    currentState = knob.getValue()
    newState = abs(currentState-1)
    knob.setValue(newState)
