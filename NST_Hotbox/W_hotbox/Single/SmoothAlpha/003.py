#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Smooth
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    n.knob('output').setValue("smooth")
