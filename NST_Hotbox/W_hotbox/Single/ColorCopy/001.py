#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Copy Hue/Sat
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    n.knob('hue').setValue(1)
    n.knob('sat').setValue(1)
    n.knob('lumaMix').setValue(0)
