#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle Split Path
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    knob = n.knob('splitPath')
    currentState = knob.getValue()
    newState = abs(currentState-1)
    knob.setValue(newState)
