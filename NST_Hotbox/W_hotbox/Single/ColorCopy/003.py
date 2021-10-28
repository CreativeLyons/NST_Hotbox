#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle LogSpace
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    knob = n.knob('opInLog')
    currentState = knob.getValue()
    newState = abs(currentState-1)
    knob.setValue(newState)
