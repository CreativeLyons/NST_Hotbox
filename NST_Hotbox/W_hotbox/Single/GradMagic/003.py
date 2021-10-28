#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Make Live
# COLOR: #3b844b
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    n.knob('makeLive').execute()
