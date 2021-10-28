#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Inject New Channel
# TEXTCOLOR: #ff817a
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    n.knob('injectNewChannel').execute()
