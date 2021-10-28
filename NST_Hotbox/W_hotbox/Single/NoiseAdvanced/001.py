#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Caustics
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    n.knob('invert').setValue(1)
    n.knob('type').setValue('turbulance')
    n.knob('speedZ').setValue(0.01)
    n.knob('octaves').setValue(2)
    n.knob('gamma').setValue(3)
    
