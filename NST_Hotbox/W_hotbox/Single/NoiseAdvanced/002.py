#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle Invert
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    knob = n.knob('invert')
    currentState = knob.getValue()
    newState = abs(currentState-1)
    knob.setValue(newState)
